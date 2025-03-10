import re
import json

def validate_email(value):
    email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
    return bool(re.match(email_regex, value))

def validate_min_length(value, length):
    return len(value) >= length

def validate_max_length(value, length):
    return len(value) <= length

def validate_integer(value):
    return isinstance(value, int)

def validate_input(input_data, validation_rules):
    for key, value in input_data.items():
        rules = validation_rules.get(key, {})
        for rule, param in rules.items():
            if rule == "min_length":
                if not validate_min_length(value, param):
                    raise ValueError(f"{key} must be at least {param} characters long.")
            elif rule == "max_length":
                if not validate_max_length(value, param):
                    raise ValueError(f"{key} must be no longer than {param} characters.")
            elif rule == "email":
                if not validate_email(value):
                    raise ValueError(f"{key} must be a valid email address.")
            elif rule == "integer":
                if not validate_integer(value):
                    raise ValueError(f"{key} must be an integer.")
    print("All inputs are valid!")  # Выводим сообщение, если все данные прошли проверку
    return True

# Example usage
input_data = {
    'email': 'user@example.com',
    'password': 'strongpassword123',
    'age': 25
}

validation_rules = {
    'email': {'email': True},
    'password': {'min_length': 8, 'max_length': 20},
    'age': {'integer': True}
}

try:
    validate_input(input_data, validation_rules)
except ValueError as e:
    print(f"Validation error: {e}")
