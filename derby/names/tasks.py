import random
import string

from aitextgen import aitextgen
from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from derby.names.models import Name

logger = settings.LOGGER


@db_periodic_task(crontab(minute="*/1"))
def generate_name(max_length=64, prompt=None, temperature=1.0):
    try:
        model_dir = settings.MODEL_DIR
        logger.debug(f"Loading model from {model_dir.absolute()}")
        ai = aitextgen(
            model_folder=str(model_dir),
            tokenizer_file=str(model_dir / "aitextgen.tokenizer.json"),
        )
        if prompt is None:
            prompt = random.choice(string.ascii_uppercase)
        logger.debug("Generating names")
        generated = ai.generate_one(
            prompt=prompt, temperature=temperature, max_length=max_length
        ).strip()
        print(generated)

        logger.debug("Saving names")
        Name.objects.update_or_create(name=generated)
        logger.debug("Done")
    except Exception as error:
        logger.error(f"Error generating names: {error}")
        raise Exception(error)
