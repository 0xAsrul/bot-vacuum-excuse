"""The Robot Vacuum's Best Excuse — one-line excuse, 140 chars or fewer."""

LINE = "I didn't miss that spot, my sensors classified the dust as a family pet and I refuse to eat a relative."

MAX_CHARS = 140


def main() -> None:
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
