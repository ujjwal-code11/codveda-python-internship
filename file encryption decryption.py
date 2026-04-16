def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as f:
        content = f.read()

    choice = input("Encrypt or Decrypt (e/d): ").lower()
    shift = int(input("Enter shift value: "))

    if choice == "e":
        result = encrypt(content, shift)
        with open("encrypted.txt", "w") as f:
            f.write(result)
        print("✅ File encrypted as encrypted.txt")

    elif choice == "d":
        result = decrypt(content, shift)
        with open("decrypted.txt", "w") as f:
            f.write(result)
        print("✅ File decrypted as decrypted.txt")

    else:
        print("Invalid choice")

except FileNotFoundError:
    print("❌ File not found")