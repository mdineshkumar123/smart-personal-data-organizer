import os
import shutil

def organize(folder):
    if not os.path.exists(folder):
        print("Folder not found")
        return

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split(".")[-1]
            target = os.path.join(folder, ext)

            os.makedirs(target, exist_ok=True)
            shutil.move(path, os.path.join(target, file))

if __name__ == "__main__":
    organize("downloads")