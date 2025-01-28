

def _add(x, y):
    return x + y

def _subtract(x: float, y: float) -> float:
    return x - y

def _multiply(x: float, y: float) -> float:
    return x * y

def _divide(x: float, y: float):
    if y == 0:
        return ValueError("Division by zero is not allowed.")
    else:
        return x / y

def calculate(x, y, operation: str) -> float:
    result_calculated = 0
    match operation:
        case '+':
            return _add(float(x), float(y))
        case '-':
            return _subtract(float(x), float(y))
        case '*':
            return _multiply(float(x), float(y))
        case '/':
            return _divide(float(x), float(y))
        case _:
            raise ValueError("Invalid operation, use '+', '-', '*', or '/'.")