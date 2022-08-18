from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from derby.names.tasks import generate_name

logger = settings.LOGGER


class Command(BaseCommand):
    help = "Generates name from aitextgen model"

    def handle(self, *args, **options):
        try:
            generate_name()
        except Exception as error:
            logger.error(f"Error generating name: {error}")
            raise CommandError(error)
