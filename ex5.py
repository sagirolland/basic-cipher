import os
import sys
import json
import string
import shutil

class VigenereCipher:
    def __init__(self, key):
        self.key=key

    def encrypt(self, message):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        Capital_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keyindex = 0
        encriptmessage= ''
        for char in message:
            if char in alphabet:
                shift = alphabet.index(self.key[keyindex % len(self.key)])
                encrypted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
                encriptmessage += encrypted_char
                keyindex += 1
                if keyindex==len(self.key):
                    keyindex=0
            elif char in Capital_alphabet:
                shift = Capital_alphabet.index(self.key[keyindex % len(self.key)])
                encrypted_char = Capital_alphabet[(Capital_alphabet.index(char) + shift) % len(Capital_alphabet)]
                encriptmessage += encrypted_char
                keyindex += 1
                if keyindex==len(self.key):
                    keyindex=0
            else:
                encriptmessage+=char
        return encriptmessage
    
    def decrypt(self, message):
        for number in self.key:
            self.key[number]= -self.key[number]
        decoded= self.encrypt(self,message).copy()
        return decoded
    
class CaesarCipher(VigenereCipher):
    def __init__(self, key):
        super().__init__(key)

    def encrypt(self, message):
        encriptmessage= message.copy()
        encriptmessage=self.encrypt(message,self.key)
        return encriptmessage
            
    def decrypt(self,message):
        key = -self.key
        encriptmessage= message.copy()
        encriptmessage=self.decrypt(message,key)
        return encriptmessage
    
    def key_shift(self,delta):
        self.key = self.key + delta
            
def loadEncryptionSystem(dir_path, plaintext_suffix):
    with open(dir_path,'r') as f:
        loaded_dict = json.load(f)
    
    entries = os.listdir(dir_path)

    if loaded_dict["type"]=="Vigenere":
        Vigenere_Cipher=VigenereCipher(Vigenere_Cipher,key=loaded_dict["key"])
        
        for entry in entries:
            entry_path = os.path.join(dir_path, entry)
            if os.path.isfile(entry_path):
                shutil.copy2(entry_path, entry_path)
                if loaded_dict("encrypt")== "True":
                    if entry.endswith(plaintext_suffix):
                        os.rename(entry_path, entry_path + ".enc")
                        with open(entry_path, 'r+') as file:
                            content = file.read()
                            encrypted_content = Vigenere_Cipher.encrypt(content)
                            file.seek(0)
                            file.write(encrypted_content)
                            file.truncate()

                if loaded_dict("encrypt")== "False":            
                    if entry.endswith(".enc"):
                        os.rename(entry_path, entry_path.replace(".enc", plaintext_suffix))
                        with open(entry_path, 'r+') as file:
                            content = file.read()
                            decrypted_content = Vigenere_Cipher.decrypt(content)
                            file.seek(0)
                            file.write(decrypted_content)
                            file.truncate()

    elif loaded_dict["type"]=="Caesar":
        Caesar_Cipher=CaesarCipher(Caesar_Cipher,key=loaded_dict["key"])

        for entry in entries:
            entry_path = os.path.join(dir_path, entry)
            if os.path.isfile(entry_path):
                shutil.copy2(entry_path, entry_path)
                if loaded_dict("encrypt")== "True":
                    if entry.endswith(plaintext_suffix):
                        os.rename(entry_path, entry_path + ".enc")
                        with open(entry_path, 'r+') as file:
                            content = file.read()
                            encrypted_content = Caesar_Cipher.encrypt(content)
                            file.seek(0)
                            file.write(encrypted_content)
                            file.truncate()
                            
                if loaded_dict("encrypt")== "False":            
                    if entry.endswith(".enc"):
                        os.rename(entry_path, entry_path.replace(".enc", plaintext_suffix))
                        with open(entry_path, 'r+') as file:
                            content = file.read()
                            decrypted_content = Caesar_Cipher.decrypt(content)
                            file.seek(0)
                            file.write(decrypted_content)
                            file.truncate()