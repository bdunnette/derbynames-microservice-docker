from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from gdown import download

logger = settings.LOGGER


class Command(BaseCommand):
    help = "Fetches aitextgen model from google drive"

    def handle(self, *args, **options):
        try:
            model_dir = settings.MODEL_DIR
            if not model_dir.exists():
                logger.info(f"{model_dir.absolute()} does not exist, creating")
                model_dir.mkdir(parents=True)
            logger.info(f"Downloading model to {model_dir.absolute()}")
            download(
                id=settings.MODEL_CONFIG_GDRIVE_ID,
                output=str(model_dir / "config.json"),
            )
            download(
                id=settings.MODEL_TOKENIZER_GDRIVE_ID,
                output=str(model_dir / "aitextgen.tokenizer.json"),
            )
            download(
                id=settings.MODEL_GDRIVE_ID, output=str(model_dir / "pytorch_model.bin")
            )
        except Exception as error:
            logger.error(f"Error fetching model: {error}")
            raise CommandError(error)
