"""
░█████╗░███╗░░██╗███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔════╝██║░░░██║
███████║██╔██╗██║█████╗░░██║░░░██║
██╔══██║██║╚████║██╔══╝░░██║░░░██║
██║░░██║██║░╚███║██║░░░░░╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v0.3.10
©Justaus3r 2021
Distributed under GPLV3
  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


This is My First Project with curses so prolly gonna be messy,also too many comments,lol
"""
import curses
import time
import sys
import os
import time
from core.EncFo import FolderEncryption
from core.EncFi import FileEncryption
from tkinter import *
from tkinter import filedialog
from rich import print
import shutil
import ctypes
import threading
from plyer import notification as notify_onichan
from zipfile import ZipFile
from getpass import getuser

# Func for Checkin Os,iggggnoooorrrreee maccc
def CheckOs():
    if os.name == "nt":
        return "Windows"
    else:
        return "Linux"
# settinf the font type used by anfu
try:
    with open('_config_font_type','r') as read_font_type:
        font_type = read_font_type.read()
        read_font_type.close()
except FileNotFoundError:
    with open('_config_font_type','w') as write_font_type:
        write_font_type.write('0')
        write_font_type.close()
    font_type = '0'    

# Defining All the menu lists
_menu_list_1 = ["Encrypt", "Decrypt", "Help","About", "Exit"]
_sub_menu_list_encrypt = ["Encrypt a File", "Encrypt a Folder", "Back"]
_sub_menu_list_decrypt = ["Decrypt a File", "Decrypt a Folder", "Back"]
if font_type == '0':
    _menu_list_2 = [".>Encrypt", ".>Decrypt", ".>Help",".>About", ".>Exit"]
    _sub_menu_list_encrypt2 = [".>Encrypt a File", ".>Encrypt a Folder", ".>Back"]
    _sub_menu_list_decrypt2 = [".>Decrypt a File", ".>Decrypt a Folder", ".>Back"]
elif font_type == '1':    
    _sub_menu_list_encrypt2 = ["𝓔𝓷𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓲𝓵𝓮", "𝓔𝓷𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓸𝓵𝓭𝓮𝓻", "𝓑𝓪𝓬𝓴"]
    _menu_list_2 = ["𝓔𝓷𝓬𝓻𝔂𝓹𝓽", "𝓓𝓮𝓬𝓻𝔂𝓹𝓽","𝓗𝓮𝓵𝓹","𝓐𝓫𝓸𝓾𝓽", "𝓔𝔁𝓲𝓽"]
    _sub_menu_list_decrypt2 = ["𝓓𝓮𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓲𝓵𝓮", "𝓓𝓮𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓸𝓵𝓭𝓮𝓻", "𝓑𝓪𝓬𝓴"]
else:
    with open('_config_font_type','w') as write_font_type:
        write_font_type.write('0')
        write_font_type.close()
    _menu_list_2 = [".>Encrypt", ".>Decrypt", ".>Help",".>About", ".>Exit"]
    _sub_menu_list_encrypt2 = [".>Encrypt a File", ".>Encrypt a Folder", ".>Back"]
    _sub_menu_list_decrypt2 = [".>Decrypt a File", ".>Decrypt a Folder", ".>Back"]

# Defining a text list,that is to be animated
textlist = [
    "B",
    "By",
    "By ",
    "By J",
    "By Ju",
    "By Jus",
    "By Just",
    "By Justa",
    "By Justau",
    "By Justaus",
    "By Justaus3",
    "By Justaus3r",
    "By Justaus3r ",
]

# version no
VERSION = '0.3.10'
# title
TITLE = f"Anfuv{VERSION}"
# Defining the Banner
Banner = f"""
░█████╗░███╗░░██╗███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔════╝██║░░░██║
███████║██╔██╗██║█████╗░░██║░░░██║
██╔══██║██║╚████║██╔══╝░░██║░░░██║
██║░░██║██║░╚███║██║░░░░░╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v{VERSION}
An open source File/Folder Encryption Program
"""

if CheckOs() == 'Windows':
    ctypes.windll.kernel32.SetConsoleTitleW(f"{TITLE}")
else:
    os.system(f"python3 -c \"print(f'\33]0;{TITLE}\a', end='', flush=True)\"")


# custumizing the Esc key delay to 25 millisecs,as normally it takes roughly 1 second to respond which is slower
os.environ.setdefault("ESCDELAY", "25")

# Main Menu
def Menu(stdscr, _current_row_index):
    
    # Clearing the screen
    stdscr.clear()
    # Getting Height and Width of console
    _height, _width = stdscr.getmaxyx()
    # Using For loop to find x and y of every element
    for index, Element in enumerate(_menu_list_1):
        # Formulas to find x and y
        x_main_menu = _width // 2 - len(Element) // 2
        y_main_menu = _height // 2 - len(_menu_list_1) // 2 + index
        global x_of_main_menu
        global y_of_main_menu
        global first_element_of_menu 
        x_of_main_menu = x_main_menu
        y_of_main_menu = y_main_menu
        first_element_of_menu = _height // 2 - len(_menu_list_1) // 2

        # printing the Elements
        # Checking if the  index is equal to _current_row_index and using elements from _menu_list_2 to print the selected element
        if index == _current_row_index:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y_main_menu, x_main_menu, _menu_list_2[index])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y_main_menu, x_main_menu, Element)

        # Refershing the screen so show all the updated stuff
        stdscr.refresh()


# Encryption Sub Menu
def _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc):
    stdscr.clear()
    # height and width for encryption sub menu
    height_enc_menu, width_enc_menu = stdscr.getmaxyx()
    for index_enc_menu, _element_enc_menu in enumerate(_sub_menu_list_encrypt):
        x_sub_menu_encrypt = width_enc_menu // 2 - len(_element_enc_menu) // 2
        y_sub_menu_encrypt = height_enc_menu // 2 - len(_sub_menu_list_encrypt) // 2 + index_enc_menu
        global x_of_sub_menu_encrypt
        global y_of_sub_menu_encrypt
        global  first_element_of_enc_menu
        x_of_sub_menu_encrypt = x_sub_menu_encrypt
        y_of_sub_menu_encrypt = y_sub_menu_encrypt
        first_element_of_enc_menu = height_enc_menu // 2 - len(_sub_menu_list_encrypt) // 2
        if index_enc_menu == _current_row_index_submenu_enc:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y_sub_menu_encrypt, x_sub_menu_encrypt, _sub_menu_list_encrypt2[index_enc_menu])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y_sub_menu_encrypt, x_sub_menu_encrypt, _element_enc_menu)
            # REFRESH SCREEN
        stdscr.refresh()


# Decryption Sub Menu
def _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec):
    stdscr.clear()
    # height and width for encryption sub menu
    height_dec_menu, width_dec_menu = stdscr.getmaxyx()
    for index_dec_menu, _element_dec_menu in enumerate(_sub_menu_list_decrypt):
        x_sub_menu_decrypt = width_dec_menu // 2 - len(_element_dec_menu) // 2
        y_sub_menu_decrypt = height_dec_menu // 2 - len(_sub_menu_list_decrypt) // 2 + index_dec_menu
        global x_of_sub_menu_decrypt
        global y_of_sub_menu_decrypt
        global first_element_of_dec_menu
        x_of_sub_menu_decrypt = x_sub_menu_decrypt
        y_of_sub_menu_decrypt = y_sub_menu_decrypt
        first_element_of_dec_menu = height_dec_menu // 2 - len(_sub_menu_list_decrypt) // 2
        if index_dec_menu == _current_row_index_submenu_dec:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y_sub_menu_decrypt, x_sub_menu_decrypt, _sub_menu_list_decrypt2[index_dec_menu])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y_sub_menu_decrypt, x_sub_menu_decrypt, _element_dec_menu)
            # REFRESH SCREEN
        stdscr.refresh()


# Function to display text in center
def Display_text_in_center(stdscr, text):
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)


# Some Animation for Encryption Process
def Animated_text_encrypt(stdscr):
    text = "Generating Encryption Key.Available at Desktop/ANFU_KEYS"
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    time.sleep(2)
    text4 = "PLEASE KEEP THE ENCRYPTION KEY SAFE!"
    stdscr.clear()
    stdscr.attron(curses.color_pair(68))
    Display_text_in_center(stdscr, text4)
    stdscr.attroff(curses.color_pair(68))
    stdscr.refresh()
    time.sleep(2)
    text2 = "Encrypting the File/Folder.."
    stdscr.clear()
    stdscr.attron(curses.color_pair(101))
    Display_text_in_center(stdscr, text2)
    stdscr.attroff(curses.color_pair(101))
    stdscr.refresh()
    time.sleep(2)



# Some Animation for Decryption Process
def Animated_text_decrypt(stdscr):
    text = "Reading Encryption Key."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    time.sleep(2)
    stdscr.clear()
    text2 = "Decrypting the File/Folder.."
    stdscr.clear()
    stdscr.attron(curses.color_pair(101))
    Display_text_in_center(stdscr, text2)
    stdscr.attroff(curses.color_pair(101))
    stdscr.refresh()
    time.sleep(2)


# Function for getting filename
def _get_filename(stdscr):
    filename = Tk()
    if CheckOs() == "Windows":
        filename.FileName = filedialog.askopenfilename(
            initialdir="C:\\", title="Select a File", filetypes=(("All Files", "*.*"),)
        )
        filename.destroy()
        return filename.FileName    
    # if not windows then linux,IGNOREEEEEEEEE MAC
    else:        
        filename.FileName = filedialog.askopenfilename(
            initialdir="/home", title="Select a File", filetypes=(("All Files", "*.*"),)
        )
        filename.destroy()
        return filename.FileName


# Function for getting Directory name
def _get_dirname(stdscr):
    # Creating obj of Tk class
    Dir = Tk()
    # Selecting a dir
    Dir.Dirname = filedialog.askdirectory()
    # Destroying the window
    Dir.destroy()
    return Dir.Dirname


def _get_keyfile(stdscr):
    keyfile = Tk()
    if CheckOs() == "Windows":
        keyfile.KeyfileName = filedialog.askopenfilename(
            initialdir="C:\\",
            title="Select a Key File",
            filetypes=(("Anfu Keyfiles", "*.anky"),),
        )
        keyfile.destroy()
        return keyfile.KeyfileName
    else:
        # if not windows then linux,IGNOREEEEEEEEE MAC
        keyfile.KeyfileName = filedialog.askopenfilename(
            initialdir="/home",
            title="Select a Key File",
            filetypes=(("Anfu Keyfiles", "*.anky"),),
        )
        keyfile.destroy()
        return keyfile.KeyfileName


# Function to check if a file is being choosed or not
def is_file_choosen(stdscr, thefilename):
    if str(thefilename) == "()" or str(thefilename) == "" :
        stdscr.clear()
        stdscr.attron(curses.color_pair(68))
        Display_text_in_center(stdscr, "Error:OniChan you baka,Choose a File First")
        stdscr.attroff(curses.color_pair(68))
        stdscr.refresh()
        time.sleep(2)
        Main(stdscr)

#Display only banner
def DisplayOnlyBanner(stdscr):
    try:
        curses.init_pair(39, curses.COLOR_RED, -1)    
        height_screen,width_screen = stdscr.getmaxyx()
        x_banner = width_screen // 2 - 40 // 2
        y_banner = height_screen // 2 - 11
        for Lines in Banner.split("\n"):
            stdscr.attron(curses.color_pair(39))
            stdscr.addstr(y_banner, x_banner, Lines)
            stdscr.attroff(curses.color_pair(39))
            y_banner += 1
    except Exception :
        stdscr.clear()
        Display_text_in_center(stdscr,"Please set windows size of atleast 112x35(x,y)") 

def encrypt_file_notification(stdscr):
    if CheckOs() == 'Windows':
        _icon_file = '_ico_file_ico.ico'
    else:
        _icon_file = '_ico_file_png.png'    
    notify_onichan.notify(
        title = "File/Folder Encryption Notification",
        message = "Your File/Folder has been Encrypted successfully...",
        app_name = "Anfu",
        app_icon = _icon_file,
        timeout=2
    )

def decrypt_file_notification(stdscr):
    if CheckOs() == 'Windows':
        _icon_file = '_ico_file_ico.ico'
    else:
        _icon_file = '_ico_file_png.png'    
    notify_onichan.notify(
        title = "File/Folder Decryption Notification",
        message = "All Operations successfully...",
        app_name = "Anfu",
        app_icon = _icon_file,
        timeout=2
    )

def if_file_dir_encrypted_successfully(stdscr,path):    
    def dir_not_encrypted_error(stdscr):
        stdscr.refresh()
        stdscr.clear()        
        stdscr.attron(curses.color_pair(69))
        Display_text_in_center(stdscr,"Look's like the Directory didn't get encrypt")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Possible Reasons might be a very big Directory or Insufficient memory..")
        stdscr.refresh()
        time.sleep(2.69)
        stdscr.clear()
        Display_text_in_center(stdscr,"Try adding file to a zip or freeing some RAM")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Log File at :Desktop/ANFU_ERROR_LOG.txt")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Report bugs at github.com/justaus3r/Anfu/issues")
        stdscr.refresh()
        time.sleep(2.69)
        stdscr.clear()
        stdscr.attroff(curses.color_pair(69)) 
        Main(stdscr)
    
    def file_not_encrypted_error(stdscr):
        stdscr.refresh()
        stdscr.clear()
        stdscr.attron(curses.color_pair(69))
        Display_text_in_center(stdscr,"Look's like the File/Archive didn't get encrypt")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Possible Reasons might be a very big file or Insufficient memory..")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Try adding file to a zip or freeing some RAM then try again.")
        stdscr.refresh()
        time.sleep(2.3)
        stdscr.clear()
        Display_text_in_center(stdscr,"Log File at :Desktop/ANFU_ERROR_LOG.txt")
        stdscr.refresh()
        time.sleep(2.2)
        stdscr.clear()
        Display_text_in_center(stdscr,"Report bugs at github.com/justaus3r/Anfu/issues")
        stdscr.refresh()
        time.sleep(2.6) 
        stdscr.clear()
        stdscr.attroff(curses.color_pair(69))
        Main(stdscr)
                    
    if os.path.isfile(path):
        if os.path.basename(path).split('.')[1] == 'zip':
            try:
                ZipFile(path)
                file_not_encrypted_error(stdscr)
            except Exception:
                pass    
        else:
            # if the keyfile is not present in key folder ,means that the file didnt get encrypt 
            if CheckOs() == 'Windows':
                _keyfile_path = f'C:\\Users\\{getuser()}\\Desktop\\ANFU_KEYS\\{os.path.basename(path)}.FILE.anky' 
            else:
                _keyfile_path = f'/home/{getuser()}/Desktop/ANFU_KEYS/{os.path.basename(path)}.FILE.anky'    
            if not os.path.isfile(_keyfile_path):
                file_not_encrypted_error(stdscr)
    else:
        if os.path.isdir(path):
            stdscr.clear()
            stdscr.refresh()
            dir_not_encrypted_error(stdscr)
            stdscr.refresh()     
        elif  os.path.isfile(os.getcwd() + os.sep + f'{os.path.basename(path)}.zip'):
            try:
                ZipFile(os.getcwd() + os.sep + f'{os.path.basename(path)}.zip')
                dir_not_encrypted_error(stdscr)
            except Exception:
                Display_text_in_center(stdscr,f"Look's like the file is encrypted and present in \n {os.getcwd()}")    
                time.sleep(2.3)
                Main(stdscr)
        else:
            pass        
# File Encryption 
def _encrypt_a_file(stdscr):
    # printing the text in center
    text = (
        "Press any key to Select a File,Esc to return to Menu"
    )
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    # gettin key pressed by usr
    KEY = stdscr.getch()
    stdscr.clear()
    # If user presses ESC then return to main menu instead of selecting a file.
    if KEY == 27:
        Main(stdscr)
    # calling the File Select Function
    Filename = _get_filename(stdscr)
    # function to Check if user didn't choose any file and if the drive has enough space
    is_file_choosen(stdscr, Filename)
    if_enough_space(stdscr,Filename)
    _is_file_too_big(stdscr,Filename)
    stdscr.clear()
    # Creating object of FileEncryption Class
    File = FileEncryption()
    # Some Animated stuff to show before actually Encrypting the file
    Animated_text_encrypt(stdscr)
    # Calling the EncryptFile method to encrypt the file
    File.EncryptFile(Filename)
    if_file_dir_encrypted_successfully(stdscr,Filename)
    text3 = "File/Folder Has Been Encrypted Successfully..."
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    encrypt_file_notification(stdscr)
    time.sleep(2)
    text5 = "Returning to Main Menu.wait please."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text5)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    time.sleep(2)    
    # Calling the Main method cuz will go to main menu after encrypting the file
    Main(stdscr)

# Folder Encryption
def _encrypt_a_folder(stdscr):
    text = "Press any key to Select a Folder,Press Esc to return to Menu"
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    KEY = stdscr.getch()
    if KEY == 27:
        Main(stdscr)
    # calling the function that return dirname
    Dir = _get_dirname(stdscr)
    # Check if user didn't choose any Directory(an empty tuple is returned so we will check for that)
    is_file_choosen(stdscr, Dir)
    _is_file_too_big(stdscr,Dir)
    # Creating object of FolderEncryption class
    Enc = FolderEncryption()
    # clearing screen before animation
    stdscr.clear()
    # Animation before Encrypting dir
    Animated_text_encrypt(stdscr)
    Enc.EncryptFolder(Dir)
    if_file_dir_encrypted_successfully(stdscr,Dir)
    text3 = "File/Folder Has Been Encrypted Successfully..."
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    encrypt_file_notification(stdscr)
    time.sleep(2)
    text5 = "Returning to Main Menu.wait please."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text5)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    time.sleep(2)    
    # Calling the main menu after encryption
    Main(stdscr)

# Decrypt File
def _decrypt_a_file(stdscr):
    text = (
        "Press any key to Select a File,Esc to return to Menu"
    )
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    _get_key = stdscr.getch()
    if _get_key == 27:
        Main(stdscr)
    stdscr.clear()
    # Calling the getfile function to get the file
    EncFile = _get_filename(stdscr)
    # check if usr didnt choose anyfile
    is_file_choosen(stdscr, EncFile)
    text1 = "Now Choose a Key file to Decrypt the File"
    stdscr.attron(curses.color_pair(68))
    Display_text_in_center(stdscr, text1)
    stdscr.attroff(curses.color_pair(68))
    stdscr.refresh()
    time.sleep(2)
    # now after getting the file we will get the encryption key(by calling the getkey function) to decrypt the file
    KeyFile = _get_keyfile(stdscr)
    # check if usr didnt choose anyfile
    is_file_choosen(stdscr, KeyFile)
    Decrypt = FileEncryption()
    # showin some animation before decrypting the file
    stdscr.clear()
    Animated_text_decrypt(stdscr)
    # Decrypting the file
    Decrypt.DecryptFile(KeyFile, EncFile)
    text3 = "Checking for Exceptions"
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    time.sleep(1.0)
    text4 = "All Operations executed Successfully."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text4)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    decrypt_file_notification(stdscr)
    time.sleep(0.69)
    # CAlling the main menu after decryption
    Main(stdscr)

#Decrypt Folder
def _decrypt_a_folder(stdscr):
    text = "Press any key to Select the Encrypted File,Esc to return to Menu"
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(69))
    _get_key = stdscr.getch()
    if _get_key == 27:
        Main(stdscr)
    # clearin screen
    stdscr.clear()
    _enc_file = _get_filename(stdscr)
    # check if usr didnt choose anyfile
    is_file_choosen(stdscr, _enc_file)
    stdscr.clear()
    text = "Now choose a Decryption Key to Decrypt the File"
    stdscr.attron(curses.color_pair(101))
    Display_text_in_center(stdscr, text)
    stdscr.attroff(curses.color_pair(101))
    # Refreshing the screen to print updated stuff
    stdscr.refresh()
    time.sleep(1.69)
    # Getting the decryption key
    _dec_Key = _get_keyfile(stdscr)
    is_file_choosen(stdscr, _dec_Key)
    # Some Animation Before Decryption
    Animated_text_decrypt(stdscr)
    # Decrypting the file
    EncDir = FolderEncryption()
    EncDir.DecryptFolder(_dec_Key, _enc_file)
    text3 = "Checking for Exceptions"
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    time.sleep(1.0)
    text4 = "All Operations executed Successfully."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text4)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    decrypt_file_notification(stdscr)
    time.sleep(0.69)
    # Goto main menu after decryption
    Main(stdscr)

# Calculate file/folder size
def _calculate_file_dir_size(stdscr,path):
    _file_size = 0
    try:
        if os.path.isfile(path):
            _file_size = os.path.getsize(path)
            return _file_size
        else:
            for rootpath,dirs,files in os.walk(path):
                for file in files:
                    filepath = os.path.join(rootpath,file)
                    if not os.path.islink(filepath):
                        _file_size += os.path.getsize(filepath)            
            return _file_size      
    except Exception as exception:
        Display_text_in_center(stdscr,f"An unknown Exception occured,Error\n{exception}\n report it at github.com/justaus3r/Anfu/issues")
        stdscr.getch()
        Main(stdscr)

# check if the file is too big to encrypt
def _is_file_too_big(stdscr,path):
    file_size = _calculate_file_dir_size(stdscr,path)
    if int(file_size) > 999999999:
        stdscr.clear()
        stdscr.attron(curses.color_pair(69))
        Display_text_in_center(stdscr,"Hey Onichan!,The file is too big for encryption.")
        stdscr.refresh()
        stdscr.clear()
        time.sleep(1.5)
        Display_text_in_center(stdscr,"Please choose a file smaller than 1 GB")
        stdscr.refresh()
        time.sleep(2)
        stdscr.attroff(curses.color_pair(69))
        Main(stdscr)                

# enc submenu
def _encryption_sub_Menu(stdscr,_current_row_index_submenu_enc):
    # if _current_row_index is 0,meaning that user pressed enter on Encrypt option thenshow the submenu for Encryption menu
    # Calling the Encryption SubMenu
    _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc)
    # Catching Keys pressed by usr
    while True:
        DisplayOnlyBanner(stdscr)
        # Resetting mouse values to avoid funny behavier from previous values
        x_mouse_enc_menu = ''
        y_mouse_enc_menu = ''           
        _key_enc_menu = stdscr.getch()
        stdscr.clear()
        DisplayOnlyBanner(stdscr)
        if (
            _key_enc_menu == curses.KEY_UP
            and _current_row_index_submenu_enc > 0
        ):
            _current_row_index_submenu_enc -= 1
        elif (
            _key_enc_menu == curses.KEY_DOWN
            and _current_row_index_submenu_enc
            < len(_sub_menu_list_encrypt) - 1
        ):
            _current_row_index_submenu_enc += 1
        elif _key_enc_menu == curses.KEY_ENTER or _key_enc_menu in (10, 13):
            # Sub_Menu FOR Encryption Menu
            if _current_row_index_submenu_enc == 0:
                _encrypt_a_file(stdscr)
            # else if user presses the Encrypt a folder option
            elif _current_row_index_submenu_enc == 1:
                _encrypt_a_folder(stdscr)
            elif _current_row_index_submenu_enc == 2:
                #going back to main menu
                Main(stdscr)
        elif _key_enc_menu == curses.KEY_MOUSE:
            _ ,x_mouse_enc_menu ,y_mouse_enc_menu ,_ ,_ = curses.getmouse()
            if y_mouse_enc_menu == first_element_of_enc_menu and x_mouse_enc_menu in range(x_of_sub_menu_encrypt - 5,x_of_sub_menu_encrypt + 12):
                _encrypt_a_file(stdscr)
            elif y_mouse_enc_menu == first_element_of_enc_menu + 1 and x_mouse_enc_menu in range(x_of_sub_menu_encrypt - 5,x_of_sub_menu_encrypt + 12):
                _encrypt_a_folder(stdscr)
            elif y_mouse_enc_menu == first_element_of_enc_menu + 2 and x_mouse_enc_menu in range(x_of_sub_menu_encrypt,x_of_sub_menu_encrypt + 6):
                # going back to menu
                Main(stdscr)


        stdscr.refresh()
        # Calling Updated Encrypt Menu
        _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc)

# dec submenu
def _decryption_sub_menu(stdscr,_current_row_index_submenu_dec):
    _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec)
    while True:
        DisplayOnlyBanner(stdscr)        
        # Resetting mouse values to avoid funny behavier from previous values
        x_mouse_dec_menu = ''
        y_mouse_dec_menu = ''        
        _key_dec_menu = stdscr.getch()
        stdscr.clear()
        DisplayOnlyBanner(stdscr)        
        if (
            _key_dec_menu == curses.KEY_UP
            and _current_row_index_submenu_dec > 0
        ):
            _current_row_index_submenu_dec -= 1
        elif (
            _key_dec_menu == curses.KEY_DOWN
            and _current_row_index_submenu_dec < len(_sub_menu_list_decrypt)
        ):
            _current_row_index_submenu_dec += 1
        elif _key_dec_menu == curses.KEY_ENTER or _key_dec_menu in (10, 13):
            # _current_row_index_submenu_dec = 0 --------> decrypt a file ,1 -------->decrypt a folder ,2------------> back to menu
            if _current_row_index_submenu_dec == 0:
                _decrypt_a_file(stdscr)
            elif _current_row_index_submenu_dec == 1:
                _decrypt_a_folder(stdscr)
            elif _current_row_index_submenu_dec == 2:
                # Go back to Main menu if usr press back option
                Main(stdscr)
        elif _key_dec_menu == curses.KEY_MOUSE:
            _, x_mouse_dec_menu, y_mouse_dec_menu, _, _ = curses.getmouse()
            if y_mouse_dec_menu == first_element_of_dec_menu and x_mouse_dec_menu in range(x_of_sub_menu_decrypt - 5,x_of_sub_menu_decrypt + 12):
                _decrypt_a_file(stdscr)
            elif y_mouse_dec_menu == first_element_of_dec_menu + 1 and x_mouse_dec_menu in range(x_of_sub_menu_decrypt - 5 ,x_of_sub_menu_decrypt + 12):
                _decrypt_a_folder(stdscr)
            elif y_mouse_dec_menu == first_element_of_dec_menu + 2 and x_mouse_dec_menu in range(x_of_sub_menu_decrypt,x_of_sub_menu_decrypt + 6):
                # return to menu
                Main(stdscr)

        stdscr.refresh()
        _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec)

# About
def About(stdscr):
    _about_window = Tk()
    _about_window.title("About ANFU")
    Label(
        _about_window,
        text="An open source program for Encryping Files and Folders",
    ).pack()
    Label(_about_window, text=f"Version:{VERSION}").pack()
    Label(_about_window, text="Distributed under GPLV3").pack()
    Label(
        _about_window,
        text="Star the repo(github.com/Justaus3r/Anfu),if you think it deserves.",
    ).pack()
    Label(_about_window, text="Cheers :)").pack()
    _about_window.mainloop()
    # goto main menu afterr showing about
    Main(stdscr)

#exit    
def _exit(stdscr):
    try:
        os.remove("AnfuTmpcfg.temp")
        os.remove("write_notification_bool")
    except FileNotFoundError:
        pass
    # When creeating an executable change python.exe to _virtual_mem_check.exe
    if CheckOs() == 'Windows':
        os.system("taskkill /f /im python.exe")
    sys.exit(0)



def _help(stdscr):
    stdscr.clear()
    help_msg = '''
┌═════════════════════════════════════════════════════════════════════════════┐
█                                    HELP                                     █
█      https:github.com/Justaus3r/Anfu for  more detailed troubleshooting     █ 
█               Usage:                                                        █
█                     Just Navigate through menu using UP/DOWN Keys or mouse. █
█                     Before Encryption be sure that your system has minimal  █
█                     ram free,as Anfu works best with free memory especially █
█                     with files greater than 100 Mb.As of this time Anfu     █
█                     can't encrypt File/Folder greater than 1 Gigabyte.      █
█                      "Big Files are not recommended for Encryption"         █                                                                             
█               Troubleshooting some problems:                                █
█              1:Enabling Mouse on Windows(Beta Feature):                     █
█                Sometimes mouse doesn't work when you start Anfu(not a bug   █
█                maybe,cmd limitation),you can simply enable it by right      █
█                clicking the mouse on menu or by using UP/DOWN key.          █
█              2:Directory/File not getting Encrypted:                        █
█               Probably because the file is too big,you system does not have █
█               enough RAM or you directory contains files that Anfu does not █
█               have permissions.                                             █
└═════════════════════════════════════════════════════════════════════════════┘
                       PRESS ANY KEY/CLICK TO CONTINUE
'''
    try:
        curses.init_pair(39, curses.COLOR_RED, -1)    
        height_screen,width_screen = stdscr.getmaxyx()
        x_banner = width_screen // 2 - 40 
        y_banner = height_screen // 2 - 11
        for Lines in help_msg.split("\n"):
            stdscr.attron(curses.color_pair(39))
            stdscr.addstr(y_banner, x_banner, Lines)
            stdscr.attroff(curses.color_pair(39))
            y_banner += 1
        stdscr.getch()
        Main(stdscr)    
    except Exception :
        stdscr.clear()
        Display_text_in_center(stdscr,"Please set windows size of atleast 112x35(x,y)[recommended 113x40]") 



def if_enough_space(stdscr,path):
    disk_usage = shutil.disk_usage(path)
    total_memory = int(disk_usage[0])
    used_memory = int(disk_usage[1])
    file_size = int(_calculate_file_dir_size(stdscr,path))
    if used_memory + file_size > total_memory:
        req_size = used_memory + file_size - total_memory / 1024 /1024 /1024
        stdscr.clear()
        Display_text_in_center(stdscr,f"Hey Onichan,it looks like you don't have enough memory in your disk,{req_size} Gigabytes more needed")
        Main(stdscr)


def DisplayBannerWithAnimation(stdscr):
    # Defining the color scheme here too as color schemes from Main function won't work here
    curses.use_default_colors()
    curses.init_pair(69, curses.COLOR_MAGENTA, -1)
    # Second Color scheme
    curses.init_pair(101, curses.COLOR_BLUE, -1)
    # Third Color scheme
    curses.init_pair(68, curses.COLOR_RED, -1)
    # Fourth Color scheme
    curses.init_pair(100, curses.COLOR_GREEN, -1)
    height, width = stdscr.getmaxyx()
    x = width // 2 - 40 // 2
    y = height // 2 - 6
    for Lines in Banner.split("\n"):
        stdscr.attron(curses.color_pair(101))
        stdscr.addstr(y, x, Lines)
        stdscr.attroff(curses.color_pair(101))
        y += 1
    # defining new value of x as previous value is only for banner
    # there r 12 characters in the lists so we will subtract 12 to keep the text in center
    x1 = width // 2 - 12 // 2
    for i in range(0, 12):
        stdscr.attron(curses.color_pair(69))
        stdscr.addstr(y, x1, textlist[i])
        stdscr.attroff(curses.color_pair(69))
        stdscr.refresh()
        time.sleep(0.2)


# Main Function
def Main(stdscr):
    # Checking if the temp file exists,and if not then create a temp file having value 0.Based on this value ,a Banner will be shown.
    if os.path.isfile("AnfuTmpcfg.temp") is False:
        with open("AnfuTmpcfg.temp", "w") as WriteTemp:
            WriteTemp.write("0")
            WriteTemp.close()
    # Current row index for all Menu's
    _current_row_index = 0
    _current_row_index_submenu_enc = 0
    _current_row_index_submenu_dec = 0

    # Setting first color scheme
    curses.use_default_colors()
    curses.init_pair(69, curses.COLOR_MAGENTA, -1)
    # Second Color scheme
    curses.use_default_colors()
    curses.init_pair(101, curses.COLOR_BLUE, -1)
    # Third Color scheme
    curses.use_default_colors()
    curses.init_pair(68, curses.COLOR_RED, -1)
    # Fourth Color scheme
    curses.use_default_colors()
    curses.init_pair(100, curses.COLOR_GREEN, -1)

    # Turning the cursor blinking to False
    curses.curs_set(0)

    # Reading Config file and updating it,if value is 0 then display banner and update it to 1 because we only want to show the banner 1 time
    try:
        with open("AnfuTmpcfg.temp", "r") as ReadConf:
            _show_banner_count = ReadConf.read()
            ReadConf.close()
    except:
        _show_banner_count = 1
    if int(_show_banner_count) < 1:
        with open("AnfuTmpcfg.temp", "w") as Writeconf:
            Writeconf.write("1")
        DisplayBannerWithAnimation(stdscr)       
    # Calling the Menu Function in Main Function
    Menu(stdscr, _current_row_index)

    # Looping an infinite loop to catch the keys pressed by the user
    while True:
        DisplayOnlyBanner(stdscr)
        # Resetting mouse values to avoid funny behavier from previous values
        x_mouse = ''
        y_mouse = ''
        Key = stdscr.getch()
        curses.mousemask(1)
        stdscr.clear()
        DisplayOnlyBanner(stdscr)
        # if usr press up key and the _current_row_index > 0 then decrease the _current_row_index so that we can move to one option upward
        if Key == curses.KEY_UP and _current_row_index > 0:
            _current_row_index -= 1

        # if usr enters the down key and _current_row_index is smaller than lenght of _menu_list_1 - 1 then increase the _current_row_index so we can move downward
        elif Key == curses.KEY_DOWN and _current_row_index < len(_menu_list_1) - 1:
            _current_row_index += 1

        # if user press enter key then check the _current_row_index and show subMenus According to it
        elif Key == curses.KEY_ENTER or Key in (10, 13):
            if _current_row_index == 0:
                _encryption_sub_Menu(stdscr,_current_row_index_submenu_enc)
            elif _current_row_index == 1:
                _decryption_sub_menu(stdscr,_current_row_index_submenu_dec)
            elif _current_row_index == 2:
                _help(stdscr)
            elif _current_row_index == 3:
                About(stdscr)
            elif _current_row_index == 4:
                _exit(stdscr)    
            stdscr.getch()
        elif Key == curses.KEY_MOUSE:
            _, x_mouse , y_mouse , _ , _ = curses.getmouse()
            if y_mouse == first_element_of_menu and x_mouse in range(x_of_main_menu - 1,x_of_main_menu + 9):
                _encryption_sub_Menu(stdscr,_current_row_index_submenu_enc)
            elif y_mouse == first_element_of_menu + 1 and x_mouse in range(x_of_main_menu - 1,x_of_main_menu + 9):    
                _decryption_sub_menu(stdscr,_current_row_index_submenu_dec)
            elif y_mouse == first_element_of_menu + 2 and x_mouse in range(x_of_main_menu - 1,x_of_main_menu + 5):    
                _help(stdscr)
            elif y_mouse == first_element_of_menu + 3 and x_mouse in range(x_of_main_menu - 1,x_of_main_menu + 5):    
                About(stdscr)
            elif y_mouse == first_element_of_menu + 4 and x_mouse in range(x_of_main_menu - 1,x_of_main_menu + 5):    
                _exit(stdscr)    
        stdscr.refresh()
        # Displaying the Updated Menu
        Menu(stdscr, _current_row_index)



# Checking and deleting the conf(if exist)files before calling the wrapper function
if os.path.isfile("AnfuTmpcfg.temp") is True:
    os.remove("AnfuTmpcfg.temp")   
# Executing the ram checking module in a thread before starting the program
def execute_ram_checker():
    os.system('_run_hidden.vbs')
#Only execute the ram checking module if the os is windows
if os.name == 'nt':
    thread_execute_ram_checker = threading.Thread(target=execute_ram_checker)    
    thread_execute_ram_checker.start()
curses.wrapper(Main)
