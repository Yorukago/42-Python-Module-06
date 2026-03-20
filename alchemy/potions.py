from .elements import (
    create_fire,
    create_water,
    create_earth,
    create_air
)


def healing_potion() -> str:
    """Brew a healing potion."""
    # Use the results from elements.py [cite: 179]
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    """Brew a strength potion."""
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    """Brew an invisibility potion."""
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    """Brew a wisdom potion using all elements."""
    res = (f"{create_fire()}, {create_water()}, "
           f"{create_earth()}, {create_air()}")
    return f"Wisdom potion brewed with all elements: {res}"
