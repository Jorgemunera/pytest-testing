def suma(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('tipo de valor no adecuado')
    return x + y

def is_greater_than(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('tipo de valor no adecuado')
    return x > y

def login(username, password):
    if((username == "jorge") and (password == "jorge123")):
        return True
    else:
        return False