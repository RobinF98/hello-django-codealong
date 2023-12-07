from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_default_done_status_is_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
