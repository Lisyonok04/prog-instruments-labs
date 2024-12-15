import os
import logging
from typing import List


logging.basicConfig(
    filename="logging.txt",
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
            logging.info(f"The iterator for the {class_name} class has been initialized")
        except Exception as e:
            logging.error(f"Error initializing the iterator for the class {class_name}: {e}")

    def __next__(self):
        try:
            if self.counter < self.limit:
                path: str = os.path.join(
                    "dataset", self.class_name, self.data[self.counter]
                )
                self.counter += 1
                logging.info(f"Path returned {path}")
                return path
            else:
                logging.info(f"The end of the iteration for the {self.class_name} class has been reached")
                raise StopIteration
        except Exception as e:
            logging.error(f"Error during iteration for the {self.class_name} class: {e}")
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
        logging.error(f"Error when executing the main code: {e}")
