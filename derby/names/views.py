import random

from django.conf import settings
from django.db.models import Max
from rest_framework import viewsets

from derby.names.models import Name
from derby.names.serializers import NameSerializer

logger = settings.LOGGER


def get_random_name():
    max_id = Name.objects.all().aggregate(max_id=Max("id"))["max_id"]
    logger.debug(f"max_id: {max_id}")
    while True:
        pk = random.randint(1, max_id)
        logger.debug(f"pk: {pk}")
        name = Name.objects.filter(id=pk).first()
        if name:
            return name


class NameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class RandomName(viewsets.ReadOnlyModelViewSet):
    queryset = Name.objects.none()
    serializer_class = NameSerializer

    def get_queryset(self):
        name = get_random_name()
        logger.debug(f"name: {name}")
        return Name.objects.filter(id=name.id)
