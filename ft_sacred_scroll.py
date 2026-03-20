import alchemy
import alchemy.elements


def main() -> None:
    """Demonstrate Sacred Scroll mastery with clean formatting."""
    print("=== Sacred Scroll Mastery ===")

    fire_msg = alchemy.elements.create_fire()
    earth_msg = alchemy.elements.create_earth()

    print(f"alchemy.elements.create_fire(): {fire_msg}")
    print(f"alchemy.elements.create_earth(): {earth_msg}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        # Split long error strings using parentheses
        print("alchemy.create_earth(): AttributeError "
              "- not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
