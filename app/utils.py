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
