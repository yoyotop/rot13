def rot13(message):
    result = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():  # Check if the letter is lowercase
                shifted = ord(char) + 13  # Shift the character by 13 positions
                if shifted > ord('z'):  # Wrap around if necessary
                    shifted -= 26
                result += chr(shifted)  # Append the shifted character to the result
            elif char.isupper():  # Check if the letter is uppercase
                shifted = ord(char) + 13  # Shift the character by 13 positions
                if shifted > ord('Z'):  # Wrap around if necessary
                    shifted -= 26
                result += chr(shifted)  # Append the shifted character to the result
        else:
            result += char  # Append non-letter characters unchanged
    return result
