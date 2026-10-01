import os
import shutil
from pathlib import Path
from typing import Union, List

def cleanup_directory(path: Union[str, Path], extension: str = None) -> int:
    """Removes files from directory optionally filtered by extension."""
    target_dir = Path(path)
    if not target_dir.exists():
        return 0

    count = 0
    for item in target_dir.iterdir():
        if item.is_file():
            if extension is None or item.suffix == extension:
                item.unlink()
                count += 1
    return count

def reorganize_files(source: str, target: str, mapping: dict) -> None:
    """Moves files into subdirectories based on extension mapping."""
    src_path = Path(source)
    dst_path = Path(target)
    dst_path.mkdir(parents=True, exist_ok=True)

    for file_path in src_path.iterdir():
        if file_path.is_file() and file_path.suffix in mapping:
            subdir = dst_path / mapping[file_path.suffix]
            subdir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(subdir / file_path.name))

def get_disk_usage(path: str) -> dict:
    """Calculates total files and size of directory."""
    total_size = 0
    count = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            total_size += os.path.getsize(fp)
            count += 1
    return {"files": count, "bytes": total_size}