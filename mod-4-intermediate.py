'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_len = len(alphabet)

    letter_index = alphabet.index(letter)

    shifted_index = (letter_index + shift) % alphabet_len
    
    return alphabet[shifted_index]

print(shift_letter("L", 3))
print(shift_letter("S", 4)) 
print(shift_letter("A", 2))
print(shift_letter("Z", 8)) 
print(shift_letter("X", 8))


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    alphabet_len = len(alphabet)

    encoded_message = ''

    for char in message:
        char_index = alphabet.index(char)

        shifted_index = (char_index + shift) % alphabet_len

        encoded_message += alphabet[shifted_index]

    return encoded_message
    
print(caesar_cipher("HELLOSTEPH", 5))


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    alphabet_len = len(alphabet)

    shift_index = alphabet.index(letter_shift)

    letter_index = alphabet.index(letter)

    shifted_index = (letter_index + shift_index) % alphabet_len

    return alphabet[shifted_index]

print(shift_by_letter("A", "B"))
print(shift_by_letter("S", "W"))
print(shift_by_letter("C", "W"))
    

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key * ((len(message) // len(key)) + 1) # extend the key to match the length of the message
    ciphered_message = ''
    for i in range(len(message)):
        if message[i] == ' ': # ignore spaces
            ciphered_message += ' '
        else:
            message_letter_index = alphabet.find(message[i])
            key_letter_index = alphabet.find(key[i])
            ciphered_letter_index = (message_letter_index + key_letter_index) % len(alphabet)
            ciphered_message += alphabet[ciphered_letter_index]
    return ciphered_message

print(vigenere_cipher("A C", "KEY"))
