"""
For Encryption and Decryption of Folders
Anfu 2021
"""
import shutil
from cryptography.fernet import Fernet
from zipfile import ZipFile 
import os
from rich import print
import time
from tkinter import *
import getpass
#Check Os
def CheckOs():
    if os.name =='nt':
        return "Windows"
    return "Linux"    

class FolderEncryption:
    def EncryptFolder(self,path):
        try:
            #Extracting root dir from path(dir where file is present)
            _root_dir = os.path.dirname(path)
            #Extracting Basename from path
            _File_basename = os.path.basename(path)
            #Adding Folder to zip so we can encrypt the zip
            shutil.make_archive(_File_basename,'zip',path)
            #Generating the Encryption Key
            Encryption_key = Fernet.generate_key()
            #For using the Key
            fernet = Fernet(Encryption_key)
            #Openinig the zip file to encrypt it
            with open(f"{_File_basename}.zip","rb") as ReadContent:
                Content = ReadContent.read()
                ReadContent.close()
            #Encrypting the file content
            EncryptedContent = fernet.encrypt(Content)
            #Writing Encrypted content to File 
            with open(f"{_File_basename}.zip","wb") as WriteEncrypted:
                WriteEncrypted.write(EncryptedContent)
                WriteEncrypted.close()
            #check os and make dirs and save keys
            if CheckOs() == 'Windows':
                if os.path.exists(f'C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS') is False:
                    os.mkdir(f"C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS")
                with open(f"C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_KEYS\\{_File_basename}.DIR.anky","wb") as WriteKey:
                    WriteKey.write(Encryption_key)
                    WriteKey.close()
            else:
                if os.path.exists(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS") is False:
                    os.mkdir(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS")
                with open(f"/home/{getpass.getuser()}/Desktop/ANFU_KEYS/{_File_basename}.DIR.anky","wb") as WriteKey:
                    WriteKey.write(Encryption_key)
                    WriteKey.close()        
            #Removing the directory and moving the zip to that dir
            shutil.rmtree(path)
            shutil.move(f"{_File_basename}.zip",_root_dir)
        except Exception as error:
            if CheckOs() == 'Windows':
                path = f'C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_ERROR_LOG.txt'
            else:
                path = f'/home/{getpass.getuser()}/Desktop/ANFU_ERROR_LOG.txt'
            time_now = time.asctime( time.localtime(time.time()) )
            _error_message = f'''
------------------------ERROR LOG,TIME:{time_now}--------------------------------
{error}
---------------------------------------------------------------------------------
'''            
            with open(path,'a') as write_error_log:
                write_error_log.write(_error_message)
                write_error_log.close()                    
            print(f"[red]An Error Occured.\nError:\n{error}[/red]")

    def DecryptFolder(self,keyfile,Encrypted_Dir):
        try:
            #Extracting root dir where zip file is present
            _root_dir = os.path.dirname(Encrypted_Dir)
            #Extracting Directory name from Encrypted Zip file
            _zip_file_name = os.path.basename(Encrypted_Dir)
            _dir_name = _zip_file_name.split(".")[0]
            with open(keyfile,"rb") as KeyFile:
                Key = KeyFile.read()
                KeyFile.close()
            #Using the Encryption Key
            fernet  = Fernet(Key)
            #Opening the Encrypted File and Read it
            with open(Encrypted_Dir,"rb") as Encrypted_Content:
                Encrypted = Encrypted_Content.read()
                Encrypted_Content.close()
            #Decrypting the content
            Decrypted = fernet.decrypt(Encrypted)
            #Opening the file and writing the decrypted content
            with open(Encrypted_Dir,"wb") as WriteDecrypted:
                WriteDecrypted.write(Decrypted)
                WriteDecrypted.close()
            #Extracting the zip file to directory and deleting the zip
            with ZipFile(Encrypted_Dir,"r") as ZipObj:
                if CheckOs() == "Windows":
                    ZipObj.extractall(f"{_root_dir}\\{_dir_name}")
                else:
                    ZipObj.extractall(f"{_root_dir}/{_dir_name}")
            os.remove(Encrypted_Dir)        
        except Exception as error:
            ErrWindow = Tk()
            ErrWindow.title("ERROR")
            Label(ErrWindow,text="An Error Occured While Decrypting the Directory").pack()
            Label(ErrWindow,text="Possible Reasons might be:").pack()
            Label(ErrWindow,text="1:Folder wasn't Encrypted,or was corrupted").pack()
            Label(ErrWindow,text="2:Invalid Decryption Key").pack()
            Label(ErrWindow,text="3:Permission Error").pack()
            Label(ErrWindow,text=f"ERROR:\n{error}").pack()
            ErrWindow.mainloop()
            if CheckOs() == 'Windows':
                path = f'C:\\Users\\{getpass.getuser()}\\Desktop\\ANFU_ERROR_LOG.txt'
            else:
                path = f'/home/{getpass.getuser()}/Desktop/ANFU_ERROR_LOG.txt'
            time_now = time.asctime( time.localtime(time.time()) )
            _error_message = f'''
------------------------ERROR LOG,TIME:{time_now}--------------------------------
{error}
---------------------------------------------------------------------------------
'''            
            with open(path,'a') as write_error_log:
                write_error_log.write(_error_message)
                write_error_log.close()                                
            print("[red]An Error Occured.Possible Reasons:\n1:Permission Error\n2:Invalid Encryption Key[/red]")            

# Tests
#op = FolderEncryption()
#op.EncryptFolder('C:\\Users\\Administrator\\Desktop\\My Work')
#op.DecryptFolder('C:\\Users\\Administrator\\Desktop\\ANFU_KEYS\\pp.DIR.anky','C:\\Users\\Administrator\\Desktop\\Programming\\Anfu\\core\\pp.zip')