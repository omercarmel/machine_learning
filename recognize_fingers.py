import os
import shutil
import random
from pathlib import Path

def organize_finger_images(base_dir):
    base_path = Path(base_dir)
    if not base_path.is_dir():
        raise ValueError(f"{base_dir} is not a valid directory.")

    # Create output directories for 0-5 fingers
    for i in range(6):
        (base_path / str(i)).mkdir(exist_ok=True)

    # Group files by finger count
    files_by_count = {i: [] for i in range(6)}
    for file in base_path.glob("*.png"):
        try:
            # Filename pattern: <uuid>_<num><R/L>.png
            num = int(file.stem.split("_")[-1][0])
            if num in files_by_count:
                files_by_count[num].append(file)
        except (ValueError, IndexError):
            # Skip files not matching expected format
            continue

    # Randomly copy 10 files for each finger count
    for count, files in files_by_count.items():
        selected = random.sample(files, min(10, len(files)))
        for f in selected:
            shutil.copy(f, base_path / str(count))

if __name__ == "__main__":
    dir_path = input("Enter directory path: ").strip()
    organize_finger_images(dir_path)

    import os
    import shutil
    import random
    from pathlib import Path


    def organize_finger_images(base_dir):
        base_path = Path(base_dir)
        if not base_path.is_dir():
            raise ValueError(f"{base_dir} is not a valid directory.")

        # Create output directories for 0-5 fingers
        for i in range(6):
            (base_path / str(i)).mkdir(exist_ok=True)

        # Group files by finger count
        files_by_count = {i: [] for i in range(6)}
        for file in base_path.glob("*.png"):
            try:
                # Filename pattern: <uuid>_<num><R/L>.png
                num = int(file.stem.split("_")[-1][0])
                if num in files_by_count:
                    files_by_count[num].append(file)
            except (ValueError, IndexError):
                # Skip files not matching expected format
                continue

        # Randomly copy 10 files for each finger count
        for count, files in files_by_count.items():
            selected = random.sample(files, min(10, len(files)))
            for f in selected:
                shutil.copy(f, base_path / str(count))


    if _name_ == "_main_":
        dir_path = input("Enter directory path: ").strip()
        organize_finger_images(dir_path)