from django.conf import settings

from users.models import User

import re


def userDataValidation(field, value):
    errors = []

    match field:
        case 'email':
            if re.search(settings.REGEXES['email'], value) is None:
                errors.append('Incorrect E-Mail')

            try:
                User.objects.get(email=value)
                errors.append('This E-Mail is already occupied')
            except User.DoesNotExist:
                pass

        case 'password':
            if len(value) < 8:
                errors.append('Password is too short')
        
        case 'timezone':
            error_text = 'The hour is specified incorrectly. Required format: number from 0 to 23'
            try:
                if 0 > int(value) or int(value) > 23:
                    errors.append(error_text)
            except ValueError:
                errors.append(error_text)


    return errors