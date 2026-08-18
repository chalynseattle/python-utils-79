import re

class ValidationError(Exception):
    pass


def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    if len(email) > 254:
        raise ValidationError('Email is too long')
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError('Invalid email format')
    return True


def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer')
    if age < 0:
        raise ValidationError('Age cannot be negative')
    if age > 130:
        raise ValidationError('Age is not realistic')
    return True


def validate_phone(phone: str) -> bool:
    if not isinstance(phone, str):
        raise ValidationError('Phone number must be a string')
    if not re.match(r'^\+?\d{10,15}$', phone):
        raise ValidationError('Invalid phone number format')
    return True
