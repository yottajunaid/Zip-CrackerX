import os.path
import os
import zipfile
import itertools

# ASCII art banner
# ANSI escape code for green colour
GREEN = '\033[92m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

# Banner for Zip-Cracker
print(f"""{RED}
 
$$$$$$$$\$$$$$$\$$$$$$$\         $$$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\ $$\   $$\$$$$$$$$\$$$$$$$\  
\____$$  \_$$  _$$  __$$\       $$  __$$\$$  __$$\$$  __$$\$$  __$$\$$ | $$  $$  _____$$  __$$\ 
    $$  /  $$ | $$ |  $$ |      $$ /  \__$$ |  $$ $$ /  $$ $$ /  \__$$ |$$  /$$ |     $$ |  $$ |
   $$  /   $$ | $$$$$$$  $$$$$$\$$ |     $$$$$$$  $$$$$$$$ $$ |     $$$$$  / $$$$$\   $$$$$$$  |
  $$  /    $$ | $$  ____/\______$$ |     $$  __$$<$$  __$$ $$ |     $$  $$<  $$  __|  $$  __$$< 
 $$  /     $$ | $$ |            $$ |  $$\$$ |  $$ $$ |  $$ $$ |  $$\$$ |\$$\ $$ |     $$ |  $$ |
$$$$$$$$\$$$$$$\$$ |            \$$$$$$  $$ |  $$ $$ |  $$ \$$$$$$  $$ | \$$\$$$$$$$$\$$ |  $$ |
\________\______\__|             \______/\__|  \__\__|  \__|\______/\__|  \__\________\__|  \__|

""")


# Function to Open the Zip file with the password
def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception:
        return False


# Function to BruteForce the Zip file , While taking data from the extract_zip function
def brute_force(zip_file_path, wordlist_path):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        with open(wordlist_path, 'r', encoding='utf-8') as f:  # Specify encoding if needed
            passwords = f.readlines()
        print(f"{GREEN}Attempting to bruteforce the zip file{RESET}")

        for password in passwords:
            password = password.strip()  # Remove newline characters
            print(f"Trying Password: {RED}{password}{RESET}")
            if extract_zip(zip_file, password):
                print(f"\n{GREEN}Password found: {PURPLE}{password}{RESET}")
                return
        print("Password not found in wordlist.")


# Main function to give the visuals to the CLI version , and taking inputs from the brute_force function
def main():
    print(
        f"{PURPLE}NOTE : {RESET}{GREEN}This Tool only works with {PURPLE}.ZIP{RESET}{GREEN} file Protected with {RED}'ZIP Legacy Encryption'{RESET}")
    print(f"{GREEN}Welcome to Zip File Brute Force! Developer: {RED}@YOTTAJUNAID{RESET}")
    print(f"{GREEN}Please provide the path to the zip file and the wordlist.{RESET}")

    while True:
        print(
            f"{GREEN}({RED}For Testing Purpose you can try a Default {PURPLE}.ZIP{RED} file. For this type: {PURPLE}testing.zip{GREEN})")
        zip_file_path = input(f"{PURPLE}Enter the path to the zip file: {RESET}")
        print(f"{GREEN}({RED}To Use the Default Wordlist type:{PURPLE}  100000_wordlist.txt{GREEN})")
        wordlist_path = input(f"{PURPLE}Enter the path to the wordlist: {RESET}")

        if not os.path.exists(zip_file_path) or not os.path.exists(wordlist_path):
            print(f"{PURPLE}Please specify a valid path. {RESET}")
        else:
            break

    print(f"{RED}\nStarting brute force attack...\n{RED}")
    brute_force(zip_file_path, wordlist_path)


# returning the main() function
if __name__ == "__main__":
    main()
