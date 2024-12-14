import csv
import shutil
import os
import logging
from typing import List

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def copy_in_file(old: str, new: str, name: str) -> None:
    try:
        abs_path: str = os.path.abspath(new)
        rel_path: str = os.path.relpath(new)
        path: str = os.path.join(os.path.abspath(old), name)
        list_images: name = os.listdir(path)
        for img in list_images:
            shutil.copy(os.path.join(path, img),
                        os.path.join(new, f"{name}_{img}"))
            with open("Annotasion2.csv", "a") as f:
                printer = csv.writer(f, delimiter=" ")
                printer.writerow(
                    [
                        os.path.join(abs_path, f"{name}_{img}"),
                        os.path.join(rel_path, f"{name}_{img}"),
                        name,
                    ]
                )
        logging.info(f"Файлы класса {name} скопированы в dataset2")
    except Exception as e:
        logging.error(f"Ошибка при копировании файлов класса {name}: {e}")


def creating_csvfile(namecsv: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the column headers.
    """
    try:
        with open("Annotasion2.csv", "w", newline="") as f:
            filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
            filewriter.writerow(["Absolute path", "Relative path", "Class name"])
        logging.info("Заголовок Annotasion2.csv создан")
    except Exception as e:
        logging.error(f"Ошибка при создании заголовка Annotasion2.csv: {e}")


def create_another_relative_way(name_class: str, number: int) -> str:
    return f"dataset2/{name_class}_{str(number).zfill(4)}.jpg"


if __name__ == "__main__":
    try:
        creating_csvfile("Annotasion2.csv")
        copy_in_file("dataset", "dataset2", "tulip")
        copy_in_file("dataset", "dataset2", "rose")
    except Exception as e:
        logging.error(f"Ошибка при выполнении основного кода: {e}")
