from .utilities import generate_keys, encrypt, decrypt

def main():
    print("Generating keys....")
    public_key, private_key = generate_keys(2048)

    # Key generation
    print(f"\nPublic key:(e={public_key[0]},n=<{len(str(public_key[1]))} digits>)")
    print(f"\nPrivate key:(secret number={private_key[0]},n=<{len(str(private_key[1]))} digits>)\n")

    message = ''

    while True:

        userinput = input("Do you want to encrypt or decrypt message? (q to quit): ")

        if userinput == "q":
            break

        if userinput.lower() == "encrypt":
            message = input("Enter a message to encrypt: ")

            try:
                ciphertext = encrypt(message, public_key)
                print(f"\nEncrypted message: {ciphertext}")

            except ValueError as error:
                print(f"\nError: {error}")


        elif userinput.lower() == "decrypt":

            ciphertext = input("Please put the encrypted message here: ")
            private_input = input("What is the private key's secret number? ")

            if int(private_input) == private_key[0]:
                try:
                    decrypted = decrypt(int(ciphertext), private_key)
                    print(f"Decrypted message: {decrypted}")

                    if decrypted == message:
                        print("\nDecryption succeeded!")
                        break
                    print("\nDecryption failed.")
                    break

                except ValueError as error:
                    print(f"\nError: {error}")
            else:
                print("Private keys do not match. Try again with correct private key.")
                print(private_input)
                print(private_key[0])

        else:
            print("Please enter a valid command.")



if __name__ == "__main__":
    main()
