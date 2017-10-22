from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def required(value):
    if not value:
        raise ValidationError(_('Fill out this field'), 'req')


def string(value):
    validator = RegexValidator(r'', _('Enter a valid string value'), 'invalid')
    validator(value)
