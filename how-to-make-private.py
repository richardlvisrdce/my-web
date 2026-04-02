# pip install pycryptodome (pokud nemáš) nebo použij online AES encryptor
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import SHA256

def encrypt_data(plain_text, password):
    # Tohle simuluje dešifrování, které dělá CryptoJS na webu
    # Pro jednoduchost doporučuji použít online nástroj:
    # 1. Jdi na: https://www.devglan.com/online-tools/aes-encryption-decryption
    # 2. Vlož text tvých kartiček (Pojem:Definice)
    # 3. Zvol AES Mode: CBC, Key Size: 256
    # 4. Heslo vlož jako "Secret Passphrase"
    # 5. Výsledek ulož jako soubor .txt do složky /data/
    pass

print("Použij online AES nástroj pro nejlepší kompatibilitu s webem!")
