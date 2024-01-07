from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Enter details to create a regular user'

    def handle(self, *args, **options):
        username = input('Enter username: ')
        email = input('Enter email: ')
        password = input('Enter password: ')

        user = User.objects.create_user(username, email, password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
