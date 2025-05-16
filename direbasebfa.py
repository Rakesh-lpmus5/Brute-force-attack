import zipfile
from tqdm import tqdm

def brute_force_zip(zip_file_path, wordlist_path):
    zip_file = zipfile.ZipFile(zip_file_path)

    with open(wordlist_path, 'r') as wordlist:
        passwords = wordlist.readlines()

    for password in tqdm(passwords, desc="Trying passwords"):
        password = password.strip()
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"[+] Password found: {password}")
            return
        except:
            continue

    print("[-] Password not found in wordlist.")

# Example usage
brute_force_zip("protected.zip", "wordlist.txt")
