import string


def encrypt(input_str: str, password: str):
    index = 0
    new_string = ""
    for c in input_str:
        if c not in string.ascii_letters:
            new_string += c
            continue
        char_index = string.ascii_letters.find(c)
        password_index = string.ascii_letters.find(password[index % len(password)])
        letter = string.ascii_letters[(char_index + password_index) % len(string.ascii_letters)]
        new_string += letter
        index += 1
    return new_string


def decrypt(input_str: str, password: str):
    index = 0
    new_string = ""
    for c in input_str:
        if c not in string.ascii_letters:
            new_string += c
            continue
        char_index = string.ascii_letters.find(c)
        password_index = string.ascii_letters.find(password[index % len(password)])
        letter = string.ascii_letters[(char_index - password_index) % len(string.ascii_letters)]
        new_string += letter
        index += 1
    return new_string


if __name__ == "__main__":
    pwd = "password"
    print("Password: " + pwd)
    encrypted = encrypt("This is a test", pwd)
    print("Encrypted: " + encrypted)
    print("Decrypted: " + decrypt(encrypted, pwd))
