import re

EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def reviewValidation(grade, comment) -> bool:
    """Sprawdza poprawność opinii."""
    if not isinstance(grade, int) or grade < 1 or grade > 5:
        return False
    
    if not isinstance(comment, str) or len(comment) > 400:
        return False
    
    return True


def loginValidation(email, password) -> bool:
    """Sprawdza poprawność logowania."""
    if not isinstance(email, str) or len(email) > 100 or not EMAIL_REGEX.match(email):
        return False
    
    if not isinstance(password, str) or len(password) < 4 or len(password) > 64:
        return False
    
    return True


def registerValidation(email, password, first_name, last_name) -> bool:
    """Sprawdza poprawność rejestracji."""
    if loginValidation(email, password) == False:
        return False
    
    if not isinstance(first_name, str) or len(first_name) < 3 or len(first_name) > 35:
        return False
    
    if not isinstance(last_name, str) or len(last_name) < 3 or len(last_name) > 35:
        return False
    
    if not first_name.strip().isalpha() or not last_name.strip().isalpha():
        return False 

    return True



