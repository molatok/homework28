from django.core.exceptions import ValidationError


def check_user_email(value):
    if 'rambler.ru' in value:
        raise ValidationError(
            f'{value} регистрация с mail.ru запрещена.'
        )