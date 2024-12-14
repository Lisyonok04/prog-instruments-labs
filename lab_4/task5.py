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

class Iterator:
    def __init__(self, class_name: str, dir: str):
        self.class_name: str = class_name
        self.counter: int = 0
        self.dir: str = dir
        try:
            self.data: List[str] = os.listdir(os.path.join(dir, class_name))
            self.limit: int = len(self.data)
            logging.info(f"Инициализирован итератор для класса {class_name}")
        except Exception as e:
            logging.error(f"Ошибка при инициализации итератора для класса {class_name}: {e}")

    def __next__(self):
        try:
            if self.counter < self.limit:
                path: str = os.path.join(
                    "dataset", self.class_name, self.data[self.counter]
                )
                self.counter += 1
                logging.info(f"Возвращен путь {path}")
                return path
            else:
                logging.info(f"Достигнут конец итерации для класса {self.class_name}")
                raise StopIteration
        except Exception as e:
            logging.error(f"Ошибка при итерации для класса {self.class_name}: {e}")
            raise StopIteration


if __name__ == "__main__":
    try:
        class_name: Iterator = Iterator("rose", "dataset")

        for _ in range(5):
            print(next(class_name))

        class_name: Iterator = Iterator("tulip", "dataset")

        for _ in range(5):
            print(next(class_name))
    except Exception as e:
        logging.error(f"Ошибка при выполнении основного кода: {e}")
