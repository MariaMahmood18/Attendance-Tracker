import validate_user
import project
from unittest.mock import patch



def test_hash_password():
    assert validate_user.hash_password("maria") == "94aec9fbed989ece189a7e172c9cf41669050495152bc4c1dbf2a38d7fd85627"
    assert validate_user.hash_password("ali") == "94419b99b12c11133a4dfeccc3e17885974beb48f7827c48239aabfbcad238d8"


def test_menu():
    with patch("builtins.input", side_effect=["1"]):
        assert project.menu() == 1

    with patch("builtins.input", side_effect=["2"]):
        assert project.menu() == 2

    with patch("builtins.input", side_effect=["3"]):
        assert project.menu() == 3

    with patch("builtins.input", side_effect=["4"]):
        assert project.menu() == 4

def test_welcome():
    assert project.welcome("Maria Mahmood") == "\nWelcome Maria Mahmood! to attendance dashboard.\n"
    assert project.welcome("Charlie Puth") == "\nWelcome Charlie Puth! to attendance dashboard.\n"