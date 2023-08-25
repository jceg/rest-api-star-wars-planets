from django.core.management.base import BaseCommand
import requests
from planets_api.models import Planet, Terrain, Climate


class Command(BaseCommand):
    help = "Fetches data from external API and inserts it into the database"

    def handle(self, *args, **options):
        # TODO: improve error handling
        headers = {"content-type": "application/json"}
        url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
        payload = {
            "query": """
                query Query {
                    allPlanets {
                        planets {
                        name
                        population
                        terrains
                        climates
                        }
                    }
                }
            """
        }
        response = requests.post(url, json=payload, headers=headers)
        if not response.ok:
            self.stdout.write(self.style.ERROR("Error fetching data from external API"))

        data = response.json()
        try:
            data = data.get("data").get("allPlanets").get("planets")
        except AttributeError:
            self.stdout.write(self.style.ERROR("Error parsing data from external API"))

        for item in data:
            planet = Planet.objects.create(
                name=item.get("name"), population=item.get("population")
            )
            for terrain_name in item.get("terrains", []):
                terrain, _ = Terrain.objects.get_or_create(name=terrain_name)
                planet.terrains.add(terrain)
            for climate_name in item.get("climates", []):
                climate, _ = Climate.objects.get_or_create(name=climate_name)
                planet.climates.add(climate)

        self.stdout.write(self.style.SUCCESS("Data fetched and inserted successfully"))
