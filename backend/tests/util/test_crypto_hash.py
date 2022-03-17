from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])

    assert crypto_hash('Blood') == '83f9999f1fc0e2ee3dfe346e6cf35c3581a409ece0d0eb04c6a6218219757c88'