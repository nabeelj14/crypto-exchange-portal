from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-register/', views.user_register, name='user_register'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('buy-crypto/<int:agent_id>/', views.buy_crypto, name='buy_crypto'),
    path('agent-login/', views.agent_login, name='agent_login'),
    path('agent-register/', views.agent_register, name='agent_register'),
    path('agent-dashboard/', views.agent_dashboard, name='agent_dashboard'),
    
    # Admin & Approval Routes
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('approve-agent/<int:agent_id>/', views.approve_agent, name='approve_agent'),
]