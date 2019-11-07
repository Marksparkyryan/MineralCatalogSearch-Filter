from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral
from .views import pagination


class ViewTests(TestCase):

    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Abelsonite",
            image_filename="Abelsonite.jpg",
            image_caption="Abelsonite from the Green River Formation, "
            "Uintah County, Utah, US",
            category="Organic",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification="10.CA.20",
            crystal_system="Triclinic",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, "
            "\u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = "
                    "79.99\u00b0Z = 1",
            color="Pink-purple, dark greyish purple, pale purplish red, "
            "reddish brown",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            mohs_scale_hardness="2\u20133",
            luster="Adamantine, sub-metallic",
            streak="Pink",
            diaphaneity="Semitransparent",
            optical_properties="Biaxial",
            group="Organic Minerals",
        )
        self.mineral2 = Mineral.objects.create(
            name="Abernathyite",
            image_filename="Abernathyite.jpg",
            image_caption="Pale yellow abernathyite crystals and green "
            "heinrichite crystals",
            category="Arsenate",
            formula="K(UO<sub>2</sub>)(AsO<sub>4</sub>)\u00b7"
            "<sub>3</sub>H<sub>2</sub>O",
            strunz_classification="08.EB.15",
            crystal_system="Tetragonal",
            unit_cell="a = 7.176\u00c5, c = 18.126\u00c5Z = 4",
            color="Yellow",
            crystal_symmetry="H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
            cleavage="Perfect on {001}",
            mohs_scale_hardness="2.5\u20133",
            luster="Sub-Vitreous, resinous, waxy, greasy",
            streak="Pale yellow",
            diaphaneity="Transparent",
            optical_properties="Uniaxial (-)",
            refractive_index="n\u03c9 = 1.597 \u2013 1.608n\u03b5 = 1.570",
            group="Arsenates",
        )

    def test_pagination_function(self):
        """make sure etters are provided but not too many"""
        result = pagination()
        self.assertLessEqual(len(result), 26)
        self.assertGreater(len(result), 0)

    def test_index_response(self):
        """make sure list view is found and rendered"""
        resp = self.client.get(reverse('mineralsearch:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')

    def test_index_query(self):
        """make sure entire list of minerals is displayed on list view"""
        resp = self.client.get(reverse('mineralsearch:index'))
        self.assertEqual(len(resp.context['minerals']), 2)

    def test_letter_response(self):
        """make sure letter view is found and rendered"""
        resp = self.client.get(
            reverse('mineralsearch:firstletter', kwargs={'letter': 'a'})
            )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')

    def test_letter_query(self):
        """make sure letter view is found and rendered"""
        resp = self.client.get(
            reverse('mineralsearch:firstletter', kwargs={'letter': 'a'})
            )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mineralsearchapp/index.html')
        self.assertEqual(len(resp.context['minerals']), 2)
