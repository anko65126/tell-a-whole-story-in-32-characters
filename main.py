"""Entry program for 'Tell a Whole Story in 32 Characters'.

The whole entry is one Wi-Fi network name of at most 32 characters:
the funniest name that hints at a whole story in the few words a
passer-by sees in a phone's network list. This program writes
the name to /output/entry.txt (an optional first argument overrides
the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = "SheTookTheRouterToo"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) <= 32, "name exceeds the 32 character limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
