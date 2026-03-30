from django.test import TestCase
from django.urls import reverse

from .models import MensajeContacto


class ContactoViewTests(TestCase):
    def test_contacto_get_renderiza_formulario(self):
        response = self.client.get(reverse('contacto'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enviar mensaje')

    def test_contacto_post_valido_guarda_y_redirige(self):
        response = self.client.post(reverse('contacto'), {
            'nombre': 'Raul Ortega',
            'email': 'raul@example.com',
            'mensaje': 'Hola, me interesa conversar sobre un proyecto.',
        })

        self.assertRedirects(response, reverse('contacto_exito'))
        self.assertEqual(MensajeContacto.objects.count(), 1)

        mensaje = MensajeContacto.objects.get()
        self.assertEqual(mensaje.nombre, 'Raul Ortega')
        self.assertEqual(mensaje.email, 'raul@example.com')

    def test_contacto_post_invalido_muestra_errores(self):
        response = self.client.post(reverse('contacto'), {
            'nombre': '',
            'email': 'correo-invalido',
            'mensaje': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(MensajeContacto.objects.count(), 0)
        self.assertTrue(response.context['form'].errors)
