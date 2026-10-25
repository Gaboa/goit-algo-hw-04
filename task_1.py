

import shutil
import sys
from pathlib import Path


def process_paths(src_path, dist_path):
    dist_path = dist_path.resolve()
    src_path = src_path.resolve()

    if not src_path.exists():
        print(f"Source path does not exist: {src_path}")
        return

    if src_path.is_dir():
        for item in src_path.iterdir():
            process_paths(item, dist_path)
    else:
        extension = src_path.suffix[1:] or "no_extension"
        target_dir = dist_path / extension
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(src_path, target_dir / src_path.name)

def main():
    args = sys.argv[1:]
    if not args:
        print("No input provided.")
        return
    
    src_path = Path(args[0])
    if len(args) == 1:
        dist_path = Path("dist")
    else:
        dist_path = Path(args[1])

    process_paths(src_path, dist_path)


if __name__ == "__main__":
    main()