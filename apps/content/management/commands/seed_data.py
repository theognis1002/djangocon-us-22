from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django_seed import Seed

User = get_user_model()
Profile = apps.get_model("users", "Profile")

class Command(BaseCommand):
    """seed_data command"""

    help = "Makes the current database have the same data as the fixture(s), no more, no less."
    args = "fixture [fixture ...]"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--skip-remove",
            action="store_false",
            dest="remove",
            default=True,
            help="Avoid remove any object from db",
        )
        parser.add_argument(
            "--remove-before",
            action="store_true",
            dest="remove_before",
            default=False,
            help="Remove existing objects before inserting and updating new ones",
        )

    def handle(self, *args, **options):
        self.style = no_style()
        try:
            self.seed_data()
        except Exception as exc:
            raise CommandError(exc)

    def seed_data(self):
        seeder = Seed.seeder()
        
        seeder.add_entity(User, 100)
        seeder.add_entity(Profile, 100)

        seeder.execute()
