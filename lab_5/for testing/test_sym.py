import pytest
import os

from unittest.mock import patch, MagicMock
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from algoritms.symmetrical import TripleDES
from algoritms.files import Io


@pytest.mark.parametrize("key_size", [8, 16, 24])
def test_symmetric_key_generation(key_size):
    key = TripleDES.generation_key(key_size * 8)
    assert len(key) == key_size

@pytest.mark.parametrize("invalid_key_size", [63, 65, 191])
def test_symmetric_key_generation_invalid(invalid_key_size):
    with pytest.raises(ValueError):
        TripleDES.generation_key(invalid_key_size)

def test_symmetric_key_serialization():
    key = TripleDES.generation_key(64)
    simmetric_key_file = "keys/symmetric/symmetric.txt"
    Io.serialize_public_key(key, simmetric_key_file)
    assert os.path.exists(simmetric_key_file)