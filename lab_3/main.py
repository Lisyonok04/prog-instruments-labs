import csv
import re

from json import load
from typing import Dict, List, Optional

from info import PATH_TO_DATA, PATH_TO_REG, VAR
from checksum import serialize_result, calculate_checksum

def read_json(path: str) -> Optional[dict]:
    """The function reads data from .json file
    Args:
        path(str): path to json file
    Returns:
        Data as dictionary
    """
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return load(file)
    except Exception as e:
        print(f"There is an error while reading the file: {e}")
        return None

def read_csv(path: str) -> Optional[list[list[str]]]:
    """The function reads data from a CSV file
    Args:
        path(str): path to CSV file
    Returns:
        A list of lists
    """
    data = []
    try:
        with open(path, "r", encoding="utf-16") as file:
            for_help = csv.reader(file, delimiter=';')
            for row in for_help:
                data.append(row)
        return data
    except Exception as e:
        print(f"There is an error while reading the file: {str(e)}.")
        return None

def regular_check(row: list[str], patterns: dict[str, str]) -> bool:
    """The function checks if the row matches a regular expressions.
    Args:
        row(List[str]): A list of values.
        patterns(Dict[str, str]): A dictionary with field names as keys and regular expressions as values.
    Returns:
        False if there is even one wrong value in the row, otherwise True.
    """
    for val, pattern in zip(row, patterns.values()):
        if not re.match(pattern, val):
            return False
    return True

def get_invalid(patterns: dict[str, str], data: list) -> list[int]:
    """The function finds indexes of all invalid rows
    Args:
        patterns(Dict[str, str]): A dictionary with field names as keys and regular expressions as values.
        data (list): csv file
    Returns:
        List of indexes of all invalid rows
    """
    
    invalid_indexes = []
    for index, value in enumerate(data[1:]):
        if not regular_check(value, patterns):
            invalid_indexes.append(index)
    return invalid_indexes


if __name__ == "__main__":
    pattern = read_json(PATH_TO_REG)
    data = read_csv(PATH_TO_DATA)
    invalid = get_invalid(pattern, data)
    check_sum = calculate_checksum(invalid)
    serialize_result(VAR, check_sum)
