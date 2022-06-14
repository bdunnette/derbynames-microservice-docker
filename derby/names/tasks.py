from aitextgen import aitextgen
from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from derby.names.models import Name

logger = settings.LOGGER


@db_periodic_task(
    crontab(
        day=settings.GENERATE_NAMES_DAY,
        hour=settings.GENERATE_NAMES_HOUR,
        minute=settings.GENERATE_NAMES_MINUTE,
    ),
    retries=3,
)
def generate_names():
    try:
        model_dir = settings.MODEL_DIR
        logger.info(f"Loading model from {model_dir.absolute()}")
        ai = aitextgen(model_folder=str(model_dir))

        logger.info("Generating names")
        generated = ai.generate_one()
        names = [Name(name=name.strip()) for name in str(generated).split("\n")]
        logger.info(f"Generated names: {names}")

        logger.info("Saving names")
        Name.objects.bulk_create(names, ignore_conflicts=True)
        logger.info("Done")
    except Exception as error:
        logger.error(f"Error generating names: {error}")
        raise Exception(error)
