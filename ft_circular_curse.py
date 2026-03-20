from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f"validate_ingredients('fire'): {validate_ingredients('fire')}")
    print("validate_ingredients('dragon scales'): ",
          validate_ingredients('dragon scales'))

    print("\nTesting spell recording with validation:")

    valid_rec = record_spell("Fireball", "fire air")
    invalid_rec = record_spell("Dark Magic", "shadow")

    print(f"record_spell('Fireball', 'fire air'): {valid_rec}")
    print(f"record_spell('Dark Magic', 'shadow'): {invalid_rec}")

    print("\nTesting Late import technique:")
    print("record_spell('Lightning', 'air'): ",
          record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
