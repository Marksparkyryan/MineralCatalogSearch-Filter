from django.test import TestCase

from ..models import Mineral

class MineralTests(TestCase):
    fixtures = ['test_data.json']

    def test_str_method(self):
        mineral = Mineral.objects.get(pk=1)
        self.assertEqual(str(mineral), mineral.name)

    def test_fields_lower_method(self):
        mineral = Mineral.objects.get(pk=1)
        field_names = mineral._meta.get_fields()
        verbose_list = [field.verbose_name for field in field_names]
        cleaned_field_names = mineral.fields_lower
        fields_lower_list = [field for field in cleaned_field_names]
        for name in fields_lower_list:
            self.assertIn(name, verbose_list)
