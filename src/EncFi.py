"""
For Encryption and Decryption of Files
Anfu 2021
*This file is a part of Anfu
"""
from cryptography.fernet import Fernet
import os
from rich import print
import time
import getpass
from tkinter import *

def CheckOs():
    if os.name =='nt':
        return "Windows"
    return "Linux"    
class FileEncryption:
    def EncryptFile(self,path):
        try:
            self.path = path
            FileName = os.path.basename(self.path)
            #Generating an Fernet Encryption Key
            Encryption_key = Fernet.generate_key()
            with open(self.path,"rb")as ReadFile:
                FileContent = ReadFile.read()
                ReadFile.close()
            #Using the Encryption Key
            fernet = Fernet(Encryption_key)
            #Encrypting the FileContent
            Encrypted_Content = fernet.encrypt(FileContent)
            #Writing the Encrypted Content into Orignal File
            with open(self.path,"wb") as WriteFile:
                WriteFile.write(Encrypted_Content)
                WriteFile.close()
            #print Message
            #check os and make dirs and save keys
            if CheckOs() == 'Windows':
                if os.path.exists(f'C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS') is False:
                    os.mkdir(f"C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS")
                with open(f"C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS\\{FileName}.FILE.anky","wb") as WriteKey:
                    WriteKey.write(Encryption_key)
                    WriteKey.close()
            else:
                if os.path.exists(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS") is False:
                    os.mkdir(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS")
                with open(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS/{FileName}.FILE.anky","wb") as WriteKey:
                    WriteKey.write(Encryption_key)
                    WriteKey.close()
            print("[green]Encryption Key File Available at /Desktop/ANFU_KEYS.Keep the Encryption Key safe or you [red]won't[/red] be able to Decrypt Files again[/green]\n") 
        except:
            print("An Error Occured.Possible Reasons:\n1:Permission Error\n2:File was a Directory\nInvalid Encoding")                       
    def DecryptFile(self,keyfile,Encrypted_File):
        try:
            self.keyfile = keyfile
            self.Encrypted_File = Encrypted_File
            #Openining File and Reading Key
            with open(self.keyfile,"rb") as ReadKey:
                Key = ReadKey.read()
                ReadKey.close()
            #Using key file 
            fernet = Fernet(Key)
            #Opening Encrypted file and Reading it
            with open(self.Encrypted_File,"rb") as encrypted_file:
                EncryptedContent = encrypted_file.read()
                encrypted_file.close()
            #Decrypting the content
            Decrypted = fernet.decrypt(EncryptedContent)
            #Opening the file and writing the Decrypted content again
            with open(self.Encrypted_File,"wb") as WriteDecrypted:
                WriteDecrypted.write(Decrypted)
                WriteDecrypted.close()
        except:
            ErrWindow = Tk()
            ErrWindow.title("ERROR")
            Label(ErrWindow,text="An Error Occured While Decrypting the File").pack()
            Label(ErrWindow,text="Possible Reasons might be:").pack()
            Label(ErrWindow,text="1:File wasn't Encrypted,or was corrupted").pack()
            Label(ErrWindow,text="2:Invalid Decryption Key").pack()
            Label(ErrWindow,text="3:File Permission Error").pack()
            ErrWindow.mainloop()
            print("[red]An Error occured.Possible Reasons:\n1:Invalid Key\n2:File wasn't Encrypted\n3:File Permission Error\n4:File was a Directory[/red]")  


