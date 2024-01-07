from django.core.management.base import BaseCommand
from animal_app.models import AnimalModel


class Command(BaseCommand):
    help = 'Enter details to create AnimalModel instance'

    def handle(self, *args, **options):
        animal_data = {
            'name': input('Enter name: '),
            'sound': input('Enter sound: '),
            'type': input('Enter type (1: Herbivore, 2: Carnivore, 3: Omnivore): '),
            'species': input('Enter species: '),
            'habitat': input('Enter habitat: '),
        }

        AnimalModel.objects.create(**animal_data)
        self.stdout.write(self.style.SUCCESS(f'Successfully created Animal: {animal_data["name"]}'))
