import pytest
import os

from algoritms.symmetrical import TripleDES
from algoritms.files import Io

def test_symmetric_key():
    key_length = 64
    key = TripleDES.generation_key(key_length)
    assert len(key) == key_length // 8

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
    simmetric_key_path = "test_symmetric.txt"
    Io.serialize_symmetric_key(key, simmetric_key_path)
    assert os.path.exists(simmetric_key_path)
    os.remove(simmetric_key_path)

@pytest.mark.parametrize("origin_text", [
    "We've made a choice, go fight against your fate!"
    "Pain will come with the blade"
    "Pain will wake up the despondent crowd"
    "In this dormant world somehow"
])
def test_text_decryption(origin_text):

    simmetric_key = TripleDES.generation_key(64)
    path_to_origin_text = "test_text.txt"
    simmetric_key_path = "test_symmetric_key.txt"
    path_to_encrypt_text = "test_encrypted_text.txt"
    path_to_decrypt_text = "test_decrypted_text.txt"

    with open(path_to_origin_text, "w") as f:
        f.write(origin_text)
    
    Io.serialize_symmetric_key(simmetric_key, simmetric_key_path)
    TripleDES.encrypt(path_to_origin_text, simmetric_key_path, path_to_encrypt_text)
    TripleDES.decrypt(simmetric_key_path, path_to_encrypt_text, path_to_decrypt_text)

    with open(path_to_decrypt_text, "r") as f:
        decrypted_text = f.read()
    assert decrypted_text == origin_text
    os.remove(path_to_origin_text)
    os.remove(simmetric_key_path)
    os.remove(path_to_encrypt_text)
    os.remove(path_to_decrypt_text)
