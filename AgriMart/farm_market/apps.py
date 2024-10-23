from django.apps import AppConfig


class FarmMarketConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "farm_market"

    def ready(self):
        import farm_market.signals



    
