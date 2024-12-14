import pytest
import os

from algoritms.symmetrical import TripleDES
from algoritms.files import Io

def test_reading_bytes():
    generated_key = TripleDES.generation_key(64)
    test_key_path = "test_key.txt"
    Io.write_bytes(test_key_path, generated_key)
    test_read_key = Io.read_bytes(test_key_path)
    assert test_read_key == generated_key
    os.remove("test_key.txt")
