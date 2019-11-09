import re

from django.test import TestCase
from django.core.urlresolvers import reverse


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
    pass    
    



