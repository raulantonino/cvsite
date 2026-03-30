from django.test import TestCase
from django.urls import reverse

from cv.models import Perfil


class InicioViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Perfil.objects.create(
            nombre='Raul Ortega',
            titulo='Desarrollador Django',
            email='raul@example.com',
            sobre_mi='Perfil de prueba para la pagina de inicio.',
            url_portafolio_creativo='https://example.com/portfolio',
        )

    def test_inicio_carga_datos_basicos_del_perfil(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Raul Ortega')
        self.assertContains(response, 'Desarrollador Django')
