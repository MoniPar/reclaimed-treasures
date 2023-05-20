from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'


    def ready(self):
        """
        Lets Django know there's a new signals module with listeners
        """
        import checkout.signals
