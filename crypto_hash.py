import hashlib
import json

def crypto_hash(data):
    stringified_data = json.dumps(data)

    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('Blood'): {crypto_hash('Blood')}")

if __name__ == '__main__':
    main()

