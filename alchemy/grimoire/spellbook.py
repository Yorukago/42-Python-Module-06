def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell only if ingredients are valid."""
    from .validator import validate_ingredients

    res = validate_ingredients(ingredients)
    if "VALID" in res:
        return f"Spell recorded: {spell_name} ({res})"
    return f"Spell rejected: {spell_name} ({res})"
