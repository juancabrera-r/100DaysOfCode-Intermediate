alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(text, shift):
    text_encrypted = ""
    for letter in text:
        print(letter)
        if letter in alphabet:
            index = alphabet.index(letter)
            if index+shift > len(alphabet):
                index = (index+shift) - (len(alphabet))
                text_encrypted += alphabet[index]
            else:
                text_encrypted += alphabet[index+shift]
        else:
            text_encrypted += letter
    return text_encrypted

continuar = True
while continuar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" or direction != "decode":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt_word = encrypt(text = text, shift = shift)
        print(encrypt_word)
    elif direction == 'decode':
        decrypt_word = encrypt(text = text, shift = -shift)
        print(decrypt_word)
    else:
        pass
    cont = input("Do you want continue? (Y/N):").lower()
    if cont == "y":
        pass
    else:
        continuar = False
