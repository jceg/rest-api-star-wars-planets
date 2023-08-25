from django.contrib import admin

from .models import Planet, Terrain, Climate

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'population')

admin.site.register(Planet, PlanetAdmin)
admin.site.register(Terrain)
admin.site.register(Climate)
