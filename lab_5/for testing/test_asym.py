import pytest
import os

from unittest.mock import patch, MagicMock
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa

from algoritms.asymmetrical import RSA
from algoritms.files import Io


def test_asymmetric_key_generation():
    public_key, private_key = RSA.generate_key()
    assert isinstance(public_key, rsa.RSAPublicKey)
    assert isinstance(private_key, rsa.RSAPrivateKey)

def test_asymmetric_key_serialization():
    public_key, private_key = RSA.generate_key()
    public_key_file = "keys/asymmetric/public.pem"
    private_key_file = "keys/asymmetric/private.pem"

    Io.serialize_public_key(public_key_file, public_key)
    Io.serialize_private_key(private_key_file, private_key)
 
    assert os.path.exists(public_key_file)
    assert os.path.exists(private_key_file)