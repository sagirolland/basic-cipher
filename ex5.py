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
                shift =( alphabet.index(char)+self.key[keyindex])% len(alphabet)
                encriptmessage += alphabet[shift]
                keyindex += 1
                if keyindex==len(self.key):
                    keyindex=0
            elif char in Capital_alphabet:
                shift =( Capital_alphabet.index(char)+self.key[keyindex])% len(Capital_alphabet)
                encriptmessage += Capital_alphabet[shift]
                keyindex += 1
                if keyindex==len(self.key):
                    keyindex=0
            else:
                encriptmessage+=char
        return encriptmessage
    
    def decrypt(self, message):
        for i, e in enumerate(self.key):
            self.key[i]= -e
        decoded= self.encrypt(message)
        return decoded
    
class CaesarCipher(VigenereCipher):
    def __init__(self, key):
        arrkey = [key]
        super().__init__(arrkey)

    def encrypt(self, message):
        
        encriptmessage=super().encrypt(message)
        return encriptmessage
            
    def decrypt(self,message):
        
        encriptmessage=super().decrypt(message)
        return encriptmessage
    
    def key_shift(self,delta):
        self.key[0] = self.key[0] + delta
            
def loadEncryptionSystem(dir_path, plaintext_suffix):
    with open(os.path.join(dir_path,"config.json"),'r') as f:
        loaded_dict = json.load(f)
    
    entries = os.listdir(dir_path)

    if loaded_dict["type"]=="Vigenere":
        cipher=VigenereCipher(key=loaded_dict["key"])
    elif loaded_dict["type"]=="Caesar":
        cipher=CaesarCipher(key=loaded_dict["key"])
    
    for entry in entries:
        entry_path = os.path.join(dir_path, entry)
        if os.path.isfile(entry_path):
            if loaded_dict["encrypt"]== "True":
                if entry.endswith(plaintext_suffix):
                    destpath=entry_path.replace(plaintext_suffix,"enc")
                    shutil.copy2(entry_path, destpath)
                    
                    with open(entry_path, 'r+') as source:
                        content = source.read()
                        encrypted_content = cipher.encrypt(content)
                        with open(destpath,"w") as dest:
                            dest.seek(0)
                            dest.write(encrypted_content)
                            dest.truncate()

            if loaded_dict["encrypt"]== "False":            
                if entry.endswith(".enc"):
                    destpath=entry_path.replace("enc",plaintext_suffix)
                    shutil.copy2(entry_path, destpath)
                    with open(entry_path, 'r+') as source:
                        content = source.read()
                        decrypted_content = cipher.decrypt(content)
                        with open(destpath,"w") as dest:
                            dest.seek(0)
                            dest.write(decrypted_content)
                            dest.truncate()

if __name__ == '__main__':
    caesar = CaesarCipher(1)
    caesar.key_shift(2)
    print( 'd' == caesar.encrypt('a'))