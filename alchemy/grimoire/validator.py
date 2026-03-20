def validate_ingredients(ingredients: str) -> str:
    """Check if ingredients contain fire, water, earth, or air."""
    valid = ["fire", "water", "earth", "air"]
    if any(el in ingredients.lower() for el in valid):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
