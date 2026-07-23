from django.db import models
from django.utils import timezone

# --- ADMIN MODELS ---
class CryptCurrencyRateModel(models.Model):
    currencytype = models.CharField(max_length=100, primary_key=True)
    doller = models.DecimalField(max_digits=12, decimal_places=2)
    rupee = models.DecimalField(max_digits=12, decimal_places=2)
    originalprice = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.currencytype

    class Meta:
        db_table = 'currencyrate'


class CurrencyUpdateModel(models.Model):
    id = models.AutoField(primary_key=True)
    currencyname = models.CharField(max_length=100)
    conversionRate = models.FloatField()
    newCurrencyValue = models.DecimalField(max_digits=12, decimal_places=2)
    originalCurrencyValue = models.DecimalField(max_digits=12, decimal_places=2)
    chnageValue = models.DecimalField(max_digits=12, decimal_places=2)
    profitorloss = models.CharField(max_length=50)
    changedate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.currencyname} - {self.changedate.strftime('%Y-%m-%d')}"

    class Meta:
        db_table = 'currencychnagetable'


# --- AGENT MODELS ---
class BitAgentRegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    pswd = models.CharField(max_length=128)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    pan = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cryptcurrency = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='waiting')
    authkey = models.CharField(max_length=100, default='waiting')
    cdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'agentregister'


class AgentHadCrypto(models.Model):
    id = models.AutoField(primary_key=True)
    currencyName = models.CharField(max_length=100)
    useremail = models.EmailField()
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "agentscryptoquantity"
        unique_together = ('currencyName', 'useremail')


class AgentBuyCryptoModel(models.Model):
    id = models.AutoField(primary_key=True)
    agentName = models.CharField(max_length=100)
    agentemail = models.EmailField()
    currencyname = models.CharField(max_length=100)
    currentprice = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    payableammount = models.DecimalField(max_digits=12, decimal_places=2)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'AgentBuyedTransactions'


# --- USER MODELS ---
class BitUserRegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    pswd = models.CharField(max_length=128)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    pan = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='waiting')
    authkey = models.CharField(max_length=100, default='waiting')
    cdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'userregister'


class CustomerHadCoins(models.Model):
    id = models.AutoField(primary_key=True)
    currencyName = models.CharField(max_length=100)
    customeremail = models.EmailField()
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "CustomerContainCoins"
        unique_together = ('currencyName', 'customeremail')


class UserBuyingCryptoModel(models.Model):
    id = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=100)
    email = models.EmailField()
    currencyname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    agentemail = models.EmailField()
    singlecoingamount = models.DecimalField(max_digits=12, decimal_places=2)
    payableammount = models.DecimalField(max_digits=12, decimal_places=2)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UserBuyingCryptoModel'


class BlockChainLedger(models.Model):
    id = models.AutoField(primary_key=True)
    customeremail = models.EmailField()
    agentemail = models.EmailField()
    currencyname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    paidammout = models.DecimalField(max_digits=12, decimal_places=2)
    blockchainmoney = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "BlockChainLedger"