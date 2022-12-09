import shutil
import os
import glob


def rename_files():
    os.makedirs("./renamed", exist_ok=True)
    filelist = glob.glob("./submitted/*.py")
    for file in filelist:
        new_file = file.split("_")[-1]
        new_file = os.path.join("./renamed", new_file)
        shutil.copyfile(file, new_file)


if __name__ == "__main__":
    rename_files()
