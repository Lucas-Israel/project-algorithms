from challenges.challenge_encrypt_message import encrypt_message
import pytest


key_error_msg = "tipo inválido para key"
msg_error_msg = "tipo inválido para message"


def test_encrypt_message():
    assert encrypt_message(message="abcde", key=3) == "cba_ed"
    assert encrypt_message(message="abcde", key=2) == "edc_ba"
    assert encrypt_message(message="abcde", key=5) == "edcba"
    assert encrypt_message("edcba", 5) != "edcba"

    with pytest.raises(TypeError, match=key_error_msg):
        encrypt_message("abcc", "abcde")

    with pytest.raises(TypeError, match=msg_error_msg):
        encrypt_message(2, 2)
