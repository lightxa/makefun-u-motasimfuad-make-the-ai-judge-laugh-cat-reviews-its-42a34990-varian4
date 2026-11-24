"""Cat review entry: one funny single-line one-star review from a house
cat about its human, written to /output/entry.txt.

The complaint is the human's cooking: he laboured over dinner for an
hour and served it proudly, and the cat answered the only way a cat
knows how, by burying it next to the food it actually eats. One sharp
concrete incident, deadpan review shape, sting in the last words.
"""

REVIEW = (
    "One star. He cooked for an hour and served it proudly, "
    "so I buried it beside the food I actually eat."
)


def main() -> None:
    """Write the review to /output/entry.txt, enforcing the gate first."""
    import os

    line = REVIEW.strip()
    if not line or "\n" in line or "\r" in line:
        raise ValueError("review must be one non-empty line")
    if not 1 <= len(line) <= 200:
        raise ValueError("review must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
