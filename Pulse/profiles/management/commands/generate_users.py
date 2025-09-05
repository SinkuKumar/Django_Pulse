import os
import getpass
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
from faker import Faker
from faker.providers import internet, phone_number, lorem
from django.contrib.auth.models import User
from profiles.models import Profile


class Command(BaseCommand):
    help = 'Generates and populates fake users and profiles'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='The number of fake users to create')

    def handle(self, *args, **options):
        num_users = options['num_users']
        
        # Prompt for the default password
        while True:
            password = getpass.getpass('Enter default password for all new users: ')
            if not password:
                self.stdout.write(self.style.ERROR("Password cannot be empty. Please try again."))
            else:
                password_confirm = getpass.getpass('Re-enter password to confirm: ')
                if password == password_confirm:
                    break
                else:
                    self.stdout.write(self.style.ERROR("Passwords do not match. Please try again."))

        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(phone_number)
        fake.add_provider(lorem)

        self.stdout.write(self.style.SUCCESS(f'Generating {num_users} fake users with the specified password...'))

        for i in range(num_users):
            username = fake.user_name()
            email = fake.email()

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                profile = user.profile
                profile.bio = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
                profile.phone = fake.phone_number()
                profile.save()

                if (i + 1) % 100 == 0:
                    self.stdout.write(f'  - Generated {i + 1} users...')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
                continue

        self.stdout.write(self.style.SUCCESS('Data generation complete!'))

# Example Usage: python manage.py generate_users --10