import zipfile
from tqdm import tqdm

def brute_force_zip(zip_file_path, wordlist_path):
    zip_file = zipfile.ZipFile(zip_file_path)

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
        passwords = [line.strip() for line in wordlist if line.strip()]  # remove empty lines

    print(f"[i] Trying {len(passwords)} passwords...")

    for password in tqdm(passwords, desc="Brute-forcing", unit="pw"):
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"\n[+] Password found: {password}")
            return
        except:
            continue

    print("[-] Password not found in wordlist.")

# Example usage
brute_force_zip("protected.zip", "wordlist.txt")
