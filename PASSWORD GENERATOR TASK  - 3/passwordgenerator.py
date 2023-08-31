import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_unique(password, existing_passwords):
    return password not in existing_passwords

def main():
    num_passwords = int(input("Enter the number of passwords you want to generate: "))
    length = int(input("Enter the length of each password: "))

    existing_passwords = set()

    for _ in range(num_passwords):
        while True:
            password = generate_password(length)
            if is_unique(password, existing_passwords):
                existing_passwords.add(password)
                break

        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
