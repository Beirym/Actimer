from users.models import User

from .security import encrypt


def signupValidation(auth_data):
    errors = []

    email = auth_data['email']
    try:
        User.objects.get(email=email)
        errors.append({'field': 'email', 'error': 'This E-Mail is already occupied'})
    except User.DoesNotExist:
        pass

    return errors

def loginValidation(auth_data):
    errors = []

    email = auth_data['email']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
        errors.append({'field': 'email', 'error': 'The account with this E-Mail was not found'})

    if user:
        password = auth_data['password']
        if encrypt(password) != user.password:
            errors.append({'field': 'password', 'error': 'Invalid password'})

    return errors


def forgotPasswordValidation(email):
    errors = []

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
        errors.append({'field': 'email', 'error': 'The account with this E-Mail was not found'})

    return errors