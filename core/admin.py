from django.contrib import admin
from .models import (
    CryptCurrencyRateModel,
    CurrencyUpdateModel,
    BitAgentRegisterModel,
    AgentHadCrypto,
    AgentBuyCryptoModel,
    BitUserRegisterModel,
    CustomerHadCoins,
    UserBuyingCryptoModel,
    BlockChainLedger
)

@admin.register(CryptCurrencyRateModel)
class CryptCurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('currencytype', 'doller', 'rupee', 'originalprice')
    search_fields = ('currencytype',)

@admin.register(BitUserRegisterModel)
class BitUserRegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile', 'status', 'cdate')
    list_filter = ('status',)
    search_fields = ('username', 'email')

@admin.register(BitAgentRegisterModel)
class BitAgentRegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cryptcurrency', 'status', 'cdate')
    list_filter = ('status', 'cryptcurrency')
    search_fields = ('username', 'email')

@admin.register(UserBuyingCryptoModel)
class UserBuyingCryptoAdmin(admin.ModelAdmin):
    list_display = ('customername', 'email', 'currencyname', 'quantity', 'payableammount', 'cdate')
    search_fields = ('customername', 'email', 'currencyname')

# Register remaining models for simple backend access
admin.site.register(CurrencyUpdateModel)
admin.site.register(AgentHadCrypto)
admin.site.register(AgentBuyCryptoModel)
admin.site.register(CustomerHadCoins)
admin.site.register(BlockChainLedger)