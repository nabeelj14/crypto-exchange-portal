from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    CryptCurrencyRateModel,
    BitUserRegisterModel,
    BitAgentRegisterModel,
    CustomerHadCoins,
    UserBuyingCryptoModel
)

# --- HOME VIEW ---
def home(request):
    rates = CryptCurrencyRateModel.objects.all()
    return render(request, 'index.html', {'rates': rates})


# --- USER VIEWS ---
def user_register(request):
    if request.method == 'POST':
        BitUserRegisterModel.objects.create(
            username=request.POST.get('username') or request.POST.get('name'),
            email=request.POST.get('email') or request.POST.get('loginid'),
            pswd=request.POST.get('pswd') or request.POST.get('password'),
            mobile=request.POST.get('mobile', ''),
            pan=request.POST.get('pan', ''),
            state=request.POST.get('state', ''),
            location=request.POST.get('location', '')
        )
        return redirect('user_login')
    return render(request, 'user_register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email') or request.POST.get('loginid') or request.POST.get('username')
        pswd = request.POST.get('pswd') or request.POST.get('password')
        
        user = BitUserRegisterModel.objects.filter(email=email, pswd=pswd).first() or \
               BitUserRegisterModel.objects.filter(username=email, pswd=pswd).first()
               
        if user:
            request.session['user_id'] = user.id
            return redirect('user_dashboard')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid Email or Password'})
            
    return render(request, 'user_login.html')


def user_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
        
    user = BitUserRegisterModel.objects.get(id=user_id)
    agents = BitAgentRegisterModel.objects.filter(status='Activated')
    owned_coins = CustomerHadCoins.objects.filter(customeremail=user.email)

    return render(request, 'user_dashboard.html', {
        'username': user.username,
        'email': user.email,
        'status': user.status,
        'agents': agents,
        'owned_coins': owned_coins
    })


def buy_crypto(request, agent_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
        
    user = BitUserRegisterModel.objects.get(id=user_id)
    agent = get_object_or_404(BitAgentRegisterModel, id=agent_id)
    rate = CryptCurrencyRateModel.objects.filter(currencytype=agent.cryptcurrency).first()
    
    unit_price = rate.doller if rate else 100.00

    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        total_price = unit_price * qty

        # Record Transaction
        UserBuyingCryptoModel.objects.create(
            customername=user.username,
            email=user.email,
            currencyname=agent.cryptcurrency,
            quantity=qty,
            agentemail=agent.email,
            singlecoingamount=unit_price,
            payableammount=total_price
        )

        # Update User Wallet Balance
        coin, created = CustomerHadCoins.objects.get_or_create(
            currencyName=agent.cryptcurrency,
            customeremail=user.email,
            defaults={'quantity': 0}
        )
        coin.quantity += qty
        coin.save()

        return redirect('user_dashboard')

    return render(request, 'buy_crypto.html', {
        'user': user,
        'agent': agent,
        'rate': rate
    })


# --- AGENT VIEWS ---
def agent_register(request):
    if request.method == 'POST':
        password = request.POST.get('pswd') or request.POST.get('password') or request.POST.get('pwd') or ''
        
        BitAgentRegisterModel.objects.create(
            username=request.POST.get('username') or request.POST.get('name') or 'Agent',
            email=request.POST.get('email') or request.POST.get('loginid') or '',
            pswd=password,
            mobile=request.POST.get('mobile', ''),
            pan=request.POST.get('pan', ''),
            state=request.POST.get('state', ''),
            location=request.POST.get('location') or request.POST.get('locality') or '',
            cryptcurrency=request.POST.get('cryptcurrency', 'Bitcoin')
        )
        return redirect('agent_login')
    return render(request, 'agent_register.html')


def agent_login(request):
    if request.method == 'POST':
        login_id = request.POST.get('email') or request.POST.get('loginid') or request.POST.get('username')
        pswd = request.POST.get('pswd') or request.POST.get('password')
        
        agent = BitAgentRegisterModel.objects.filter(email=login_id, pswd=pswd).first() or \
                BitAgentRegisterModel.objects.filter(username=login_id, pswd=pswd).first()
                
        if agent:
            request.session['agent_id'] = agent.id
            return redirect('agent_dashboard')
        else:
            return render(request, 'agent_login.html', {'error': 'Invalid Agent Credentials'})
            
    return render(request, 'agent_login.html')


def agent_dashboard(request):
    agent_id = request.session.get('agent_id')
    if not agent_id:
        return redirect('agent_login')
        
    agent = BitAgentRegisterModel.objects.get(id=agent_id)
    orders = UserBuyingCryptoModel.objects.filter(agentemail=agent.email)

    return render(request, 'agent_dashboard.html', {
        'username': agent.username,
        'email': agent.email,
        'cryptcurrency': agent.cryptcurrency,
        'status': agent.status,
        'orders': orders
    })


# --- ADMIN VIEWS ---
def admin_dashboard(request):
    users = BitUserRegisterModel.objects.all()
    agents = BitAgentRegisterModel.objects.all()
    return render(request, 'admin_dashboard.html', {
        'users': users,
        'agents': agents
    })


def approve_user(request, user_id):
    user = get_object_or_404(BitUserRegisterModel, id=user_id)
    user.status = 'Activated'
    user.authkey = f"AUTH-{user.id}99"
    user.save()
    return redirect('admin_dashboard')


def approve_agent(request, agent_id):
    agent = get_object_or_404(BitAgentRegisterModel, id=agent_id)
    agent.status = 'Activated'
    agent.authkey = f"AGENT-KEY-{agent.id}88"
    agent.save()
    return redirect('admin_dashboard')