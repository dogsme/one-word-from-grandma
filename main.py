"""One Word From Grandma — entrypoint.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word is "contraption": what Grandma has always called any clever
machine she does not quite trust. One word, UTF-8, nothing else — no
trailing newline, no extra output.
"""

from pathlib import Path

WORD = "contraption"
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
