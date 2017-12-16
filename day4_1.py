import little_helper

passphrases = little_helper.get_input(4).split("\n")

def is_valid(passphrase):
    return len(set(passphrase.split())) == len(passphrase.split())

valid_passphrases = [passphrase for passphrase in passphrases if is_valid(passphrase)]

print(len(valid_passphrases))