import little_helper

passphrases = little_helper.get_input(4).split("\n")

def is_valid(passphrase):
    passwords = [''.join(sorted(password)) for password in passphrase.split()]
    return len(set(passwords)) == len(passwords)

valid_passphrases = [passphrase for passphrase in passphrases if is_valid(passphrase)]

print(len(valid_passphrases))