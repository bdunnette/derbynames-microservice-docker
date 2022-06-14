from django.db import IntegrityError
from django.test import TestCase

from derby.names.models import Name


class NameTestCase(TestCase):
    def test_produces_integrity_error_on_duplicate_name(self):
        Name.objects.create(name="a")
        self.assertRaises(IntegrityError, Name.objects.create, name="a")
