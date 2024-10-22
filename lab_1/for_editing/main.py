import os
import argparse

from algoritms.asymmetrical import RSA
from algoritms.files import Io
from algoritms.symmetrical import TripleDES


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", type = str, help = "Choose generate_key/encrypt/decrypt"
    )
    args = parser.parse_args()
    setting = Io.read_json("setting.json")
    match args.mode:
        case "generate_key":
            key = int(input("Enter your key length (64, 128 or 192): "))
            while key not in [64, 128, 192]:
                if key not in [64, 128, 192]:
                    print("Try again. You've entered wrong length.")
                    key = int(input("Enter your key length (64, 128 or 192): "))
            symmetric_key = TripleDES.generation_key(key)
            Io.serialize_symmetric_key(symmetric_key, setting["symmetric_key"])
            public_key, private_key = RSA.key_generation()
            Io.serialize_public_key(setting["public_key"], public_key)
            Io.serialize_private_key(setting["private_key"], private_key)
        case "encrypt":
            encrypted = TripleDES.encrypt(
                setting["initial_file"],
                setting["symmetric_key"],
                setting["encrypted_file"],
            )
            RSA.encrypt(
                setting["public_key"],
                setting["symmetric_key"],
                setting["encrypted_symmetric_key"],
            )
        case "decrypt":
            RSA.decrypt(
                setting["private_key"],
                setting["encrypted_symmetric_key"],
                setting["decrypted_symmetric_key"],
            )
            decrypted = TripleDES.decrypt(
                setting["symmetric_key"],
                setting["encrypted_file"],
                setting["decrypted_file"],
            )
        case _:
            print(
                "No such function. Try again and enter << key_generation OR encryption OR decryption >>"
            )

if __name__ == "__main__":
    main()
 