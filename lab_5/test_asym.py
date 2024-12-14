import pytest
import os

from cryptography.hazmat.primitives.asymmetric import rsa

from algoritms.asymmetrical import RSA
from algoritms.files import Io


def test_asymmetric_key_generation():
    public_key, private_key = RSA.generate_key()
    assert isinstance(public_key, rsa.RSAPublicKey)
    assert isinstance(private_key, rsa.RSAPrivateKey)

def test_asymmetric_key_serialization():
    public_key, private_key = RSA.generate_key()
    test_public_key_file = "test_public.pem"
    test_private_key_file = "test_private.pem"

    Io.serialize_public_key(test_public_key_file, public_key)
    Io.serialize_private_key(test_private_key_file, private_key)
 
    assert os.path.exists(test_public_key_file)
    assert os.path.exists(test_private_key_file)
    os.remove(test_public_key_file)
    os.remove(test_private_key_file)
