from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Client  # Import your model
import random

class Command(BaseCommand):
    help = 'Populate your database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Adjust the range based on how many fake records you want
            Client.objects.create(
                client_name=fake.name(),
                email=fake.email(),
                phone_number = fake.phone_number(),
                dob = fake.date(),
                address = fake.address(),
                gender = '',
                age = random.randint(10,99),
                account_status = '',
                client_password = '',
                client_confirm_password = '',
                role = 'user'

                # Add other fields and fake data as needed
            )

        self.stdout.write(self.style.SUCCESS('Fake data populated successfully'))
