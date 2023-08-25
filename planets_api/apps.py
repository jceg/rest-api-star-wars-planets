from django.apps import AppConfig


class PlanetsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "planets_api"

    def ready(self):
        # Import and register the command
        from .management.commands import fetchdata
