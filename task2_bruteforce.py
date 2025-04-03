'''
Forage AIG Cybersecurity Program
Bruteforce script to decrypt a ZIP file using a password list.
'''
from zipfile import ZipFile
import sys
# Function to attempt extraction
def attempt_extract(zf_handle, password):
   try:
       zf_handle.extractall(pwd=password.encode('utf-8'))  # Try to extract using password
       print(f"[+] Password found: {password}")
       return True
   except:
       return False  # Incorrect password
def main():
   print("[+] Beginning bruteforce...")
   # Open the encrypted ZIP file
   try:
       with ZipFile('enc.zip') as zf:
           with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
               for password in f:
                   password = password.strip()  # Remove any whitespace/newline
                   if attempt_extract(zf, password):
                       print("[+] Successfully extracted the file!")
                       return
   except FileNotFoundError:
       print("[-] ZIP file not found. Make sure 'enc.zip' is in the same directory.")
       sys.exit(1)
   print("[-] Password not found in list.")
if __name__ == "__main__":
   main()