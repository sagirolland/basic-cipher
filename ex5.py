import os
import sys
import json
import string
import shutil
class CaesarCipher:
    def __init__(self, key):
        self.key=key
    def encrypt(self, messege):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Capital_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        key = self.key.copy()
        encriptmessege= ''
        for letter in messege:
            char = messege[letter]
            if letter in alphabet:
                char = alphabet[(letter-1 + key)%alphabet.size()]
                encriptmessege +=char
            elif letter in Capital_alphabet:
                char = Capital_alphabet[(letter-1 + key)%Capital_alphabet.size()]
                encriptmessege +=char
            else:
                encriptmessege+=char
        return encriptmessege
    
    def decrypt(self,messege):
        self.key = -self.key
        decoded= self.encrypt(self,messege)
        return decoded
    def key_shift(self,delta):
        self.key = self.key + delta
    


class VigenereCipher(CaesarCipher):
    def __init__(self, key):
        self.key=key
    def encrypt(self, messege):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Capital_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        key = self.key.copy()
        encriptmessege= ''
        for letter in messege:
            char = messege[letter]
            if letter in alphabet:
                char = alphabet[(letter-1 + key)%alphabet.size()]
                encriptmessege +=char
            elif letter in Capital_alphabet:
                char = Capital_alphabet[(letter-1 + key)%Capital_alphabet.size()]
                encriptmessege +=char
            else:
                encriptmessege+=char
        return encriptmessege
    
    def decrypt(self, messege):
        for number in self.key:
            self.key[number]= -self.key[number]
        decoded= VigenereCipher.encrypt(self,messege).copy()
        return decoded
    
def loadEncryptionSystem(dir_path, plaintext_suffix):
    with open('dir_path','r') as f:
        loaded_dict = json.load(f)
    
    entries = os.listdir('dir_path')

    if loaded_dict["type"]=="Vigenere":
        Vigenere_Cipher=VigenereCipher(Vigenere_Cipher,key=loaded_dict["key"])
        
        if loaded_dict["encrypt"]=="True":
            for entry in entries:
                if entry.is_file():
                    shutil.copy2("entry","entry")
                    if entry.name.endswith("plaintext_suffix"):
                        os.rename("entry","entry.enc")
                        entry= Vigenere_Cipher.encrypt("file info")
        if loaded_dict["encrypt"]=="False":
            for entry in entries:
                if entry.is_file():
                    shutil.copy2("entry","entry")
                    if entry.name.endswith(".enc"):
                        os.rename("entry","entry.plaintext_suffix")
                        entry= Vigenere_Cipher.decrypt("file info")

    elif loaded_dict["type"]=="Caesar":
        Caesar_Cipher=CaesarCipher(Caesar_Cipher,key=loaded_dict["key"])

        if loaded_dict["encrypt"]=="True":
            for entry in entries:
                if entry.is_file():
                    shutil.copy2("entry","entry")
                    if entry.name.endswith(plaintext_suffix):
                        os.rename("entry","entry.enc")
                        entry= Caesar_Cipher.encrypt("file info")
        if loaded_dict["encrypt"]=="False":
                    for entry in entries:
                        if entry.is_file():
                            shutil.copy2("entry","entry")
                            if entry.name.endswith(".enc"):
                                os.rename("entry","entry.plaintext_suffix")
                                entry= Caesar_Cipher.decrypt("file info")
                