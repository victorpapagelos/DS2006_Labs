import argparse
import random
from typing import List


def roll_die(num_sides: int) -> int:
    """Return a single roll of a die with the given number of sides."""
    if num_sides < 2:
        raise ValueError("A die must have at least 2 sides.")
    return random.randint(1, num_sides)


def roll_dice(num_dice: int, num_sides: int) -> List[int]:
    """Roll `num_dice` dice of `num_sides` sides and return the list of results."""
    if num_dice < 1:
        raise ValueError("You must roll at least one die.")
    return [roll_die(num_sides) for _ in range(num_dice)]


def format_roll(rolls: List[int], num_sides: int) -> str:
    """Format a roll result for display, including total for multiple dice."""
    if len(rolls) == 1:
        return f"You rolled a {rolls[0]} on a D{num_sides}."
    total = sum(rolls)
    rolls_str = ", ".join(str(value) for value in rolls)
    return f"You rolled [{rolls_str}] on {len(rolls)}xD{num_sides} (total={total})."


def main() -> None:
    parser = argparse.ArgumentParser(description="Roll virtual dice from the command line.")
    parser.add_argument("--sides", "-s", type=int, default=6, help="Number of sides on the die (default: 6)")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of dice to roll (default: 1)")
    parser.add_argument("--times", "-t", type=int, default=1, help="How many times to roll (default: 1)")
    parser.add_argument("--seed", type=int, default=None, help="Optional RNG seed for reproducible rolls")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    for _ in range(max(1, args.times)):
        rolls = roll_dice(num_dice=max(1, args.count), num_sides=max(2, args.sides))
        print(format_roll(rolls, max(2, args.sides)))


if __name__ == "__main__":
    main()
