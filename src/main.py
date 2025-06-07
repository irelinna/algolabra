from utilities import generate_keys, encrypt, decrypt

def main():
    print("Generating keys....")
    public_key, private_key = generate_keys(2048)

    # Key generation
    # To view private key, put 'private_key[0]' in place of <hidden>
    print(f"\nPublic key: (e={public_key[0]}, n=<{len(str(public_key[1]))} digits>)")
    print(f"\nPrivate key: (d=<hidden>, n=<{len(str(private_key[1]))} digits>)\n")

    message = input("Enter a message to encrypt: ")

    try:
        ciphertext = encrypt(message, public_key)
        print(f"\nEncrypted: {ciphertext}")

        decrypted = decrypt(ciphertext, private_key)
        print(f"Decrypted: {decrypted}")

        if decrypted == message:
            print("\nDecryption succeeded!")
        else:
            print("\nDecryption failed.")

    except ValueError as error:
        print(f"\nError: {error}")

if __name__ == "__main__":
    main()
