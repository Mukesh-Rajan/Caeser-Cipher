def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():  # Check if character is alphabetic
            # Determine whether to encrypt or decrypt based on mode
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")
            result += shifted_char
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def main():
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer): "))
    
    # Perform encryption or decryption based on user input
    if mode == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, mode)
        print("Encrypted message:", encrypted_message)
    elif mode == 'decrypt':
        decrypted_message = caesar_cipher(message, shift, mode)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
