import re

from django.db.models import Max
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Mineral
from ..forms import MineralSearchForm
from ..templatetags.mineral_extras import GROUPS, COLOURS, ALPHABET


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
        resp = self.client.get(
            reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(
            reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertTemplateUsed(resp, 'mineralsearchapp/detail.html')

    def test_single_mineral_is_retrieved(self):
        """This asserts a class not a queryset so we know that the count 
        is one
        """
        resp = self.client.get(
            reverse('mineralsearch:detail', kwargs={'pk': 1}))
        self.assertIsInstance(resp.context['mineral'], Mineral)


class RandomViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_mineral_count(self):
        minerals = Mineral.objects.aggregate(
            number_of_minerals=Max('id')
        )
        number = minerals['number_of_minerals']
        self.assertGreater(number, 0)
        mineral = Mineral.objects.get(
            id=number
        )
        self.assertIsInstance(mineral, Mineral)

    def test_hard_url_with_arg(self):
        resp = self.client.get('/random/')
        self.assertEqual(resp.status_code, 200)

    def test_named_url(self):
        resp = self.client.get(reverse('mineralsearch:random'))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(reverse('mineralsearch:random'))
        self.assertTemplateUsed(resp, 'mineralsearchapp/detail.html')

    def test_single_mineral_is_retrieved(self):
        """This asserts a class not a queryset so we know that the count 
        is one
        """
        resp = self.client.get(reverse('mineralsearch:random'))
        self.assertIsInstance(resp.context['mineral'], Mineral)


class LetterViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_hard_url_with_arg(self):
        resp = self.client.get('/letter/z')
        self.assertEqual(resp.status_code, 200)

    def test_hard_url_without_arg(self):
        resp = self.client.get('/letter/')
        self.assertEqual(resp.status_code, 404)

    def test_hard_url_without_doublearg(self):
        resp = self.client.get('/letter/ff')
        self.assertEqual(resp.status_code, 404)

    def test_named_url(self):
        resp = self.client.get(
            reverse('mineralsearch:letter', kwargs={'letter': 'z'}))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(
            reverse('mineralsearch:letter', kwargs={'letter': 'z'}))
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')
    
    c_elements = ['cacoxenite', 'cadmoindite', 'cafarsite', 'cahnite', 
    'calaverite', 'calcite', 'calderite', 'caledonite', 'calumetite', 
    'cancrinite', 'canfieldite', 'carletonite', 'carlsbergite', 'carminite', 
    'carnallite', 'carnotite', 'carpathite', 'carpholite', 'carrollite', 
    'caryopilite', 'cassiterite', 'cavansite', 'celadonite', 'celestine', 
    'celsian', 'cerite', 'cerussite', 'cervantite', 'chabazite', 
    'chalcanthite', 'chalcocite', 'chalcophyllite', 'chalcopyrite', 
    'chambersite', 'chamosite', 'chapmanite', 'charoite', 'chesterite', 
    'childrenite', 'chlorargyrite', 'chlorite group', 'chloritoid', 
    'chlormayenite', 'chloroxiphite', 'chondrodite', 'chromite', 'chrysoberyl', 
    'chrysocolla', 'chrysotile', 'cinnabar', 'claudetite', 'clausthalite', 
    'clinoclase', 'clinodehrite', 'clinohumite', 'clinoptilolite', 
    'clinozoisite', 'clintonite', 'cobaltite', 'coccinite', 'coesite', 
    'coffinite', 'colemanite', 'collinsite', 'coloradoite', 'columbite-(fe)', 
    'conichalcite', 'connellite', 'copiapite', 'copper', 'corderoite', 
    'cordierite', 'cornubite', 'cornwallite', 'corundum', 'cotunnite', 
    'covellite', 'creedite', 'cristobalite', 'crocoite', 'cronstedtite', 
    'crossite', 'cryolite', 'cryptomelane', 'cubanite', 'cummingtonite', 
    'cuprite', 'cuprosklodowskite', 'curite', 'cyanotrichite', 'cylindrite', 
    'cyrilovite'
    ]
    c_elements.sort()
    
    def test_alpha_order(self):
        resp = self.client.get(
            reverse('mineralsearch:letter', kwargs={'letter': 'c'})
        )
        context = [x['name'] for x in resp.context['minerals']]
        elements = self.c_elements
        self.assertSequenceEqual(context, elements)
        
    def test_content_contains_context(self):
        resp = self.client.get(
            reverse('mineralsearch:letter', kwargs={'letter': 'c'})
        )
        self.assertInHTML(
            '<a class="minerals__anchor" href="/detail/148">Cacoxenite</a>',
            resp.content.decode('utf-8')
        )


class SearchViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_hard_url_with_arg(self):
        resp = self.client.get('/search/', data={'q': 'gold'})
        self.assertEqual(resp.status_code, 200)

    def test_hard_url_without_arg(self):
        """An empty q in form is ok, it will just return all minerals
        """
        resp = self.client.get('/search/', data={'q': ''})
        self.assertEqual(resp.status_code, 200)

    def test_named_url(self):
        resp = self.client.get(reverse('mineralsearch:search'),
                               data={'q': 'gold'})
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(reverse('mineralsearch:search'),
                               data={'q': 'gold'})
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')

    def test_one_mineral_is_retrieved(self):
        """We know there is only one mineral with the q of Zunyite
        """
        resp = self.client.get(reverse('mineralsearch:search'),
                               data={'q': 'Zunyite'})
        self.assertEqual(len(resp.context['minerals']), 1)


class GroupViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_hard_url_with_arg(self):
        resp = self.client.get('/group/Oxides')
        self.assertEqual(resp.status_code, 200)

    def test_hard_url_without_arg(self):
        resp = self.client.get('/group/')
        self.assertEqual(resp.status_code, 404)

    def test_named_url(self):
        resp = self.client.get(
            reverse('mineralsearch:group', kwargs={'group': 'Oxides'}))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(
            reverse('mineralsearch:group', kwargs={'group': 'Oxides'}))
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')

    def test_6_minerals_retrieved_by_group_filter(self):
        """There are only 6 minerals in the Native Elements group
        """
        resp = self.client.get(
            reverse('mineralsearch:group',
                    kwargs={'group': 'Native Elements'})
        )
        self.assertEqual(len(resp.context['minerals']), 6)


class ColourViewTests(TestCase):
    fixtures = ['test_data.json']

    def test_hard_url_with_arg(self):
        resp = self.client.get('/colour/gold')
        self.assertEqual(resp.status_code, 200)

    def test_hard_url_without_arg(self):
        resp = self.client.get('/colour/')
        self.assertEqual(resp.status_code, 404)

    def test_named_url(self):
        resp = self.client.get(
            reverse('mineralsearch:colour', kwargs={'colour': 'gold'}))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(
            reverse('mineralsearch:colour', kwargs={'colour': 'gold'}))
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')

    def test_correct_minerals_are_retrieved(self):
        """This asserts a class not a queryset so we know that the count 
        is one
        """
        resp = self.client.get(
            reverse('mineralsearch:colour', kwargs={'colour': 'gold'}))
        self.assertEqual(len(resp.context['minerals']), 9) 
