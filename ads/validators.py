from django.core.exceptions import ValidationError


def check_published_status(value):
    if value != "draft":
        raise ValidationError(f"Измените статус {value} на \"draft\".")

