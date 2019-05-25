import datetime
import decimal
import logging
import random

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from clients.models import Client
from cards.models import Card
from institutions.models import Institution

fake = Faker()
logger = logging.getLogger(__name__)



class Command(BaseCommand):
    help = "Seed data to get started"

    def add_arguments(self, parser):
        parser.add_argument("--size", type=int)

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self)
        self.stdout.write("** completed seeding.")


def clear_data():
    """Deletes all the table data"""
    print("** clear data...")
    User.objects.all().delete()
    Client.objects.all().delete()
    Card.objects.all().delete()
    Institution.objects.all().delete()


def create_users():
    for n in range(0, 5):
        new_user = User.objects.create(
            username=f"test_{n}.ubausa.com",
            first_name=f"test_{n}",
            last_name=f"test_{n}",
            email=f"test_{n}.ubausa.com",
        )

        new_user.save()
        new_user.set_password("test")
        new_user.is_active = True
        new_user.save()


def create_institutions():
    print("** creating institutions")

    for n in range(0, 5):
        new_institution = Institution.objects.create(
            user=User.objects.all()[n],
            name=fake.company(),
            phone_number='824-075-85583',
            address_line_1=fake.secondary_address(),
            address_line_2=fake.street_address(),
            address_lat_long=str(fake.latitude()),
            email_address=fake.ascii_email(),
            surburb=fake.state(),
            city=fake.state()
        )
        new_institution.save()

def create_clients():
    print("** creating clients")

    for n in range(0, 5):
        new_client = Client.objects.create(
            user=User.objects.all()[n],
            institution=Institution.objects.all()[n],
            phone_number='824-075-85583',
            whatsapp_number='867-075-85456',
            address_line_1=fake.secondary_address(),
            address_line_2=fake.street_address(),
            address_lat_long=str(fake.latitude()),
            email_address=fake.ascii_email(),
            surburb=fake.state(),
            city=fake.city(),
            gender="Female",
            national_id=fake.itin(),
            student_id=fake.itin(),
            birthday=fake.future_date(end_date="+30d", tzinfo=None),
        )
        new_client.card.add(Card.objects.all()[n])
        new_client.save()


def create_cards():
    print("** creating cards")

    for n in range(0, 5):
        new_card = Card.objects.create(
            card_number=fake.company(),
            card_limit =200,
            card_status = "active",
            provider=fake.credit_card_provider(card_type=None),
            expiry_date=fake.future_date(end_date="+30d", tzinfo=None),

        )
        new_card.save()


def run_seed(self):  # pylint: disable=unused-argument
    print("** seeding ubausa application")
    clear_data()
    create_users()
    create_cards()
    create_institutions()
    create_clients()
