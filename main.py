"""Entry for make.fun bounty "The One-Line Cat Joke That Lands".

Entry text (147 characters, limit: under 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = 'My cat sat on my keyboard, typed a better password than mine, then deleted it, because some art is meant to be experienced once, then lost forever.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
