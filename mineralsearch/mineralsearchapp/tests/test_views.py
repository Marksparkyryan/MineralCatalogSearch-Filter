import re

from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Mineral
from ..views import GROUPS, COLOURS, ALPHABET

class GlobalsTests(TestCase):
    def test_groups_list(self):
        """assert that the GROUPS list has groups in it"""
        self.assertGreater(len(GROUPS), 0)
    
    def test_colours_list(self):
        """assert that the COLOURS list has colours in it"""
        self.assertGreater(len(COLOURS), 0)
    
    def test_alpha_list(self):
        """assert that the ALPHABET list has all letters in it"""
        self.assertEqual(len(ALPHABET), 26)
    
    def test_alpha_list_valid(self):
        """assert that the ALPHABET list has valid single letters in 
        it
        """
        for letter in ALPHABET:
            self.assertRegex(letter, re.compile(r'^[a-z]$'))


class DetailViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_hard_url_with_arg(self):
        resp = self.client.get('/detail/1')
        self.assertEqual(resp.status_code, 200)
    
    def test_hard_url_without_arg(self):
        resp = self.client.get('/detail/')
        self.assertEqual(resp.status_code, 404)
    
    def test_named_url(self):
        resp = self.client.get(reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
    
    def test_template_used(self):
        resp = self.client.get(reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertTemplateUsed(resp, 'mineralsearchapp/detail.html')

    def test_single_mineral_is_retrieved(self):
        """This asserts a class not a queryset so we know that the count 
        is one
        """
        resp = self.client.get(reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertIsInstance(resp.context['mineral'], Mineral)

    def test_mineral_info_is_rendered(self):
        resp = self.client.get(reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertIn(resp.context['mineral']._meta.fields, resp.content)
            





