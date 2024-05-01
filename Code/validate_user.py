import hashlib

def hash_password(password):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Convert the password to bytes and hash it
    hash_object.update(password.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    return hash_password


def main():
    print(hash_password("admin"))
    print(hash_password("admin") == hash_password("admin"))


if __name__=="__main__":
    main()