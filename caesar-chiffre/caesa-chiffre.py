import string


def encrypt(input_string, index):
    new_string = ""     # String to return

    # For each char in the string
    for c in input_string:
        # Chars to ignore --> we don't encrypt these chars
        if c in " .1234567890!§$%&/()=?\"'*_:;-,{[]}\\~":
            new_string += c
            continue

        used_index = 0

        # Set the used index corresponding to the uppercase index or lowercase index from an ascii table
        if c in string.ascii_lowercase:
            used_index = 97
        elif c in string.ascii_uppercase:
            used_index = 65

        # Get index from alphabet
        # map this value over to 0 - 26 range and add index
        # Return ascii code from alphabet index
        new_string += chr(((ord(c) - used_index + index) % 26) + used_index)
    return new_string


if __name__ == "__main__":
    # To decrypt any caesar message just use the a negative index
    print(encrypt("This is a test", 3))
    print(encrypt("Wklv lv d whvw", -3))
