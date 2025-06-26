from django.test import TestCase
from django.contrib.auth import get_user_model
from core.forms import LoginForm

UserModel = get_user_model()

class LoginFormTest(TestCase):
    def setUp(self):
        self.valid_user = UserModel.objects.create_user(
            username='teste',
            email='teste@teste.com',
            password='senha123',
            is_active=True
        )
        self.inactive_user= UserModel.objects.create_user(
            username='userInativo',
            email='ina@tivo.com',
            password='123456',
            is_active=False
        )

    def test_form_has_fields(self):
        form = LoginForm()
        expected = ['username', 'password']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_username_field_required(self):
        form = self.make_validated_form(username='')
        self.assertIn('username', form.errors)

    def test_invalid_username_not_found(self):
        form = self.make_validated_form(username='naoexiste')
        self.assertIn('__all__', form.errors)
        self.assertIn('Usuário não encontrado.', form.errors['__all__'])

    def test_wrong_password(self):
        form = self.make_validated_form(password='senhaerrada')
        self.assertIn('__all__', form.errors)
        self.assertIn('Senha incorreta para o usuario informado.', form.errors['__all__'])

    def test_inactive_user(self):
        form = self.make_validated_form(username='userInativo', password='123456')
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Usuário inativo, entre em contato com o administrador.',
            form.errors['__all__']
        )


    def test_authenticates_user(self):
        form = self.make_validated_form()
        self.assertTrue(form.is_valid())
        self.assertEqual(form.user, self.valid_user)

    def make_validated_form(self, **kwargs):
        valid = dict(username='teste', password='senha123')
        data = dict(valid, **kwargs)
        form = LoginForm(data=data)
        form.is_valid()
        return form