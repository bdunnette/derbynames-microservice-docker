from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from derby.names.tasks import generate_names

logger = settings.LOGGER


class Command(BaseCommand):
    help = "Generates names from aitextgen model"

    def handle(self, *args, **options):
        try:
            generate_names()
        except Exception as error:
            logger.error(f"Error generating names: {error}")
            raise CommandError(error)
