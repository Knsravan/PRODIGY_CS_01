def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = shift % 26  # normalize shift

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # leave non-alphabetical characters unchanged
    return result

def main():
    print("Caesar Cipher Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice.startswith('e'):
        result = caesar_cipher(text, shift, mode='encrypt')
        print("Encrypted message:", result)
    elif choice.startswith('d'):
        result = caesar_cipher(text, shift, mode='decrypt')
        print("Decrypted message:", result)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
