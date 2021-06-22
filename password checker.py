import pikepdf
from tqdm import tqdm
passwords=[line.strip() for line in open("wordlist.txt")]
for passwords in tqdm(passwords,"Decrypting PDF"):
    try:
        with pikepdf.open("sample.pdf", password=password) as pdf:
            print("\n [+] Password Found:",password)
            break
    except pikepdf ._qpdf.PasswordError as e:
        continue
