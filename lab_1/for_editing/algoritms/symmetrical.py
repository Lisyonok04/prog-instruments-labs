import os
import logging

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from algoritms.files import Io

logger = logging.getLogger()
logger.setLevel("INFO")


class TripleDES:
    """
    Class for TripleDES cipher

    Args:
        None

    Methods:
        generation_key(key_size: int) -> bytes:
        Generate a key for TripleDES
        encrypt(
            text_path: str, path_to_key: str, path_to_encrypted: str
        ) -> bytes:
        Encrypts the text
        decrypt(
            symmetric: str, path_to_encripted: str, path_to_decripted: str
        ) -> str:
        Decrypts the text
    """

    def __init__(self):
        pass

    def generation_key(key_size: int) -> bytes:
        """The funtion lets the user to choose length of key and generates a key
        Args:
            key_size(int): size of the key
        Returns:
            bytes: The generated key for triple DES
        """
        try:
            if key_size not in [64, 128, 192]:
                raise ValueError("Invalid key length. Please enter 64, 128, or 192.")
            logging.info("Symmetric keys have been generated")
            return os.urandom(key_size // 8)
        except ValueError as e:
            print("Invalid input.")

    def encrypt(
        text: str,
        path_to_key: str,
        path_to_encrypted: str,
    ) -> bytes:
        """The function encrypts text by symmetric key

        Args:
            text(str): path to origin text
            path_to_key(str): path to symmetric key
            path_to_encrypted(str): path to save encrypted text

        Returns:
            bytes: encrypted text
        """
        text = Io.read_txt(text)
        symmetric_key = Io.deserialize_symmetric_key(path_to_key)
        cipher = Cipher(
            algorithms.TripleDES(symmetric_key), modes.ECB(), default_backend()
        )
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        byte = bytes(text, "UTF-8")
        padded = padder.update(byte) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(padded) + encryptor.finalize()
        Io.write_bytes(path_to_encrypted, encrypted)
        logging.info("The text has been successfully encrypted")
        return encrypted

    def decrypt(
        symmetric: str,
        path_to_encrypted: str,
        path_to_decrypted: str,
    ) -> str:
        """The function encrypts text by symmetric key

        Args:
            symmetric(str): path to symmetric key
            path_to_encripted(str): path to encrypted text
            path_to_decripted(str): path to decrypted text

        Returns:
            str: decrypted text
        """
        encrypted = Io.read_bytes(path_to_encrypted)
        symmetric_key = Io.deserialize_symmetric_key(symmetric)
        cipher = Cipher(
            algorithms.TripleDES(symmetric_key), modes.ECB(), default_backend()
        )
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        unpadded = unpadder.update(decrypted) + unpadder.finalize()
        unpaded_text = unpadded.decode("UTF-8")
        Io.write_txt(unpaded_text, path_to_decrypted)
        logging.info("The text has been successfully decrypted")
        return unpaded_text
