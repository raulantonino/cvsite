from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Perfil


class PanelCvTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='admin',
            password='clave-segura-123',
        )

    def test_panel_cv_redirige_si_no_hay_login(self):
        response = self.client.get(reverse('panel_cv'))

        self.assertRedirects(response, f"{reverse('login')}?next={reverse('panel_cv')}")

    def test_usuario_autenticado_puede_guardar_el_perfil(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('editar_perfil'), {
            'nombre': 'Raul Ortega',
            'titulo': 'Desarrollador Full Stack',
            'email': 'raul@example.com',
            'telefono': '+56 9 1234 5678',
            'sobre_mi': 'Perfil actualizado desde tests.',
            'url_portafolio_creativo': 'https://example.com/portfolio',
            'linkedin_url': 'https://linkedin.com/in/raul',
            'github_url': 'https://github.com/raul',
        }, follow=True)

        self.assertRedirects(response, reverse('editar_perfil'))
        self.assertEqual(Perfil.objects.count(), 1)

        perfil = Perfil.objects.get()
        self.assertEqual(perfil.nombre, 'Raul Ortega')
        self.assertEqual(perfil.url_portafolio_creativo, 'https://example.com/portfolio')
