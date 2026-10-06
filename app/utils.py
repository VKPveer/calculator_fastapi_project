def clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp a number into the inclusive [minimum, maximum] range."""
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum")
    return max(minimum, min(value, maximum))


def percentage_change(old_value: float, new_value: float) -> float:
    """Return percentage change from old_value to new_value."""
    if old_value == 0:
        raise ValueError("old_value cannot be zero")
    return ((new_value - old_value) / old_value) * 100


def normalize(value: float, minimum: float, maximum: float) -> float:
    """Normalize value to the 0..1 range using the supplied bounds."""
    if minimum >= maximum:
        raise ValueError("minimum must be less than maximum")
    return (value - minimum) / (maximum - minimum)


def round_result(value: float, digits: int = 4) -> float:
    """Return a consistently rounded API result."""
    return round(value, digits)
