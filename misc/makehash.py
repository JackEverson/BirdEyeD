from werkzeug.security import generate_password_hash


def make_hash(password_string):
    hash = generate_password_hash(password_string)
    return hash


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--password", required=True, help="Password to be hashed")
    args = vars(ap.parse_args())

    hash = make_hash(args["password"])
    print(hash)
