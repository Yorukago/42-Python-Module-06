import alchemy.transmutation as trans


def main() -> None:

    print("=== Pathway Debate Mastery ===")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {trans.lead_to_gold()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {trans.philosophers_stone()}")
    print(f"elixir_of_life(): {trans.elixir_of_life()}")

    print("\nBoth pathways work!")
    print("Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
