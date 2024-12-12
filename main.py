from dict import MORSE_CODE_DICT, REVERSE_MORSE_CODE_DICT


intro = print('Welcome to morse code generator app!!!')
choices = input('What do you want this app to do (encrypt/decrypt)?:')


def encrypt(x):
    char_list = list(x.upper())
    morse_list = []
    for char in char_list:
        if char in MORSE_CODE_DICT:
            morse_list.append(MORSE_CODE_DICT[char])
        else:
            morse_list.append(char)
    morse_sentence = ' '.join(morse_list)

    return morse_sentence


def decrypt(y):
    morse_words = y.split(' ')
    text_list = []
    for morse_char in morse_words:
        if morse_char in REVERSE_MORSE_CODE_DICT:
            text_list.append(REVERSE_MORSE_CODE_DICT[morse_char])
        else:
            text_list.append(morse_char)
    text_sentence = ''.join(text_list)

    return text_sentence


if choices == 'encrypt':
    text1 = input('Please enter a phrase or a sentence:')
    answer = encrypt(text1)
    print(answer)
elif choices == 'decrypt':
    text2 = input('Please enter a morse code')
    answer = decrypt(text2)
    print(answer)
else:
    print('Invalid choice. Please choose either "encrypt" or "decrypt".')



