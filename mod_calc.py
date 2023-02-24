def sum_data(a, b):
    return a + b


def sub_data(a, b):
    return a - b


def mul_data(a, b):
    return a * b


def div_data(a, b, par="/"):
    if b:
        if par == "%":
            return a % b
        elif par == "//":
            return a // b
        return a / b
    else:
        return "Деление на 0!"


def pow_data(a, b=None):
    if not b:
        return a ** 0.5
    return a ** b
