from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("Testing ingredient validation:")
    print(f"validate_ingredients('fire'): {validate_ingredients('fire')}")

    print("\nTesting spell recording:")

    valid_rec = record_spell("Fireball", "fire air")
    invalid_rec = record_spell("Dark Magic", "shadow")

    print(f"record_spell('Fireball', 'fire air'): {valid_rec}")
    print(f"record_spell('Dark Magic', 'shadow'): {invalid_rec}")

    print("\nCircular dependency curse avoided using late imports!")


if __name__ == "__main__":
    main()
