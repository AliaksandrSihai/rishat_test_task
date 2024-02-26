from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для создания админа"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="test@mail.ru",
            first_name="test",
            last_name="test",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("123qwe456asd")
        user.save()
