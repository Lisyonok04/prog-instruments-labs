import os
import shutil
import csv
import random
import logging
from typing import List

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def copy_images(old_dir: str, new_dir: str, name: str) -> None:
    """
    The function copies one image from the old directory to the new one,
    changing the name, and writes its absolute, relative paths and class name to the .csv file.
    """
    try:
        abs_path: str = os.path.abspath(new_dir)
        rel_path: str = os.path.relpath(new_dir)
        random_number: name = random.sample((range(0, 10000)), 2000)
        count: int = 0
        path: str = os.path.join(os.path.abspath(old_dir), name)
        list_images: name = os.listdir(path)
        for img in list_images:
            new_name: str = f"{random_number[count]}".zfill(5)
            shutil.copy(
                os.path.join(path, img), os.path.join(new_dir, f"{new_name}.jpg")
            )
            with open("Annotasion3.csv", "a") as f:
                filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
                filewriter.writerow(
                    [
                        os.path.join(abs_path, f"{new_name}.jpg"),
                        os.path.join(rel_path, f"{new_name}.jpg"),
                        name,
                    ]
                )
            count += 1
        logging.info(f"Файлы класса {name} скопированы в dataset3")
    except Exception as e:
        logging.error(f"Ошибка при копировании файлов класса {name}: {e}")


def creating_csvfile(namecsv: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the layout template of the elements. 
    """
    try:
        with open("Annotasion3.csv", "w", newline="") as f:
            filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
            filewriter.writerow(["Absolute path", "Relative path", "Class name"])
        logging.info("Заголовок Annotasion3.csv создан")
    except Exception as e:
        logging.error(f"Ошибка при создании заголовка Annotasion3.csv: {e}")


if __name__ == "__main__":
    try:
        creating_csvfile("Annotasion3")
        copy_images("dataset", "dataset3", "tulip")
        copy_images("dataset", "dataset3", "rose")
    except Exception as e:
        logging.error(f"Ошибка при выполнении основного кода: {e}")
