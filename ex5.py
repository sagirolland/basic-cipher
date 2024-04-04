import os
import sys
import json
class CaesarCipher:
    def __init__(self, key):
        self.key=key
    def encrypt(self, messege):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Capital_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        key = self.key.copy()
        encriptmessege= messege.copy()
        for letter in messege:
            if letter in alphabet:
                encriptmessege[letter] = alphabet[letter-1 + key]
            elif letter in Capital_alphabet:
                encriptmessege[letter] = Capital_alphabet[letter-1 + key]
            else:
                encriptmessege[letter]=letter
        return encriptmessege
    
    def decrypt(self,messege):
        self.key = -self.key
        decoded= self.encrypt(self,messege)
        return decoded
    def key_shift(self,delta):
        self.key = self.key + delta
    


class VigenereCipher(CaesarCipher):
    def encrypt(self, messege):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Capital_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        key = self.key.copy()
        encriptmessege= messege.copy()
        for letter in messege:
            if letter == key.size():
                key = self.key.copy()
            if letter in alphabet:
                encriptmessege[letter] = alphabet[letter-1 + key[letter]]
            elif letter in Capital_alphabet:
                encriptmessege[letter] = Capital_alphabet[letter-1 + key[letter]]
            else:
                encriptmessege[letter]=letter
        return encriptmessege
    
    def decrypt(self, messege):
        for number in self.key:
            self.key[number]= -self.key[number]
        decoded= VigenereCipher.encrypt(self,messege).copy()
        return decoded
    
def loadEncryptionSystem(dir_path, plaintext_suffix):
    with open('dir_path','r') as f:
        loaded_dict = json.load(f)
    