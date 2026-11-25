from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_password_hash_roundtrip():
    hashed = hash_password("segredo")
    assert verify_password("segredo", hashed)
    assert not verify_password("errado", hashed)


def test_access_token_roundtrip():
    token = create_access_token("user-1")
    assert decode_access_token(token)["sub"] == "user-1"
