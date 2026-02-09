#!/usr/bin/env python3
"""
Simple poll-based watcher that watches `src/` for newly added `.py` files
and runs `scripts/update_readme.py` when a new file appears.

This avoids an external dependency; run it during development with:

    python3 scripts/watcher.py

It checks every 5 seconds by default.
"""
import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
SEEN_FILE = ROOT / '.scripts_seen_files'


def load_seen():
    if SEEN_FILE.exists():
        return set(SEEN_FILE.read_text(encoding='utf-8').splitlines())
    return set()


def save_seen(seen):
    SEEN_FILE.write_text('\n'.join(sorted(seen)), encoding='utf-8')


def run_updater():
    print('Detected change — running update_readme.py')
    subprocess.run(['python3', str(ROOT / 'scripts' / 'update_readme.py')])


def main(poll_interval=5):
    seen = load_seen()
    # initial snapshot
    if SRC.exists():
        for p in SRC.iterdir():
            if p.suffix == '.py':
                seen.add(p.name)
    save_seen(seen)

    try:
        while True:
            current = set()
            if SRC.exists():
                for p in SRC.iterdir():
                    if p.suffix == '.py':
                        current.add(p.name)
            new = current - seen
            if new:
                print('New files:', ', '.join(sorted(new)))
                run_updater()
                seen |= new
                save_seen(seen)
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        print('Stopping watcher')


if __name__ == '__main__':
    main()
