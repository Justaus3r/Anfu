"""
░█████╗░███╗░░██╗███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔════╝██║░░░██║
███████║██╔██╗██║█████╗░░██║░░░██║
██╔══██║██║╚████║██╔══╝░░██║░░░██║
██║░░██║██║░╚███║██║░░░░░╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v1.0
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


This is My First Project with curses so prolly gonna be messy,also there are gonna be some code repetitions
"""
import curses
import time
import sys
import os
import time
from src.EncFo import FolderEncryption
from src.EncFi import FileEncryption
from tkinter import *
from tkinter import filedialog
from rich import print

# Defining All the menu lists
_menu_list_1 = ["Encrypt", "Decrypt", "About", "Exit"]
_menu_list_2 = ["𝓔𝓷𝓬𝓻𝔂𝓹𝓽", "𝓓𝓮𝓬𝓻𝔂𝓹𝓽", "𝓐𝓫𝓸𝓾𝓽", "𝓔𝔁𝓲𝓽"]
_sub_menu_list_encrypt = ["Encrypt a File", "Encrypt a Folder", "Back"]
_sub_menu_list_encrypt2 = ["𝓔𝓷𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓲𝓵𝓮", "𝓔𝓷𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓸𝓵𝓭𝓮𝓻", "𝓑𝓪𝓬𝓴"]
_sub_menu_list_decrypt = ["Decrypt a File", "Decrypt a Folder", "Back"]
_sub_menu_list_decrypt2 = ["𝓓𝓮𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓲𝓵𝓮", "𝓓𝓮𝓬𝓻𝔂𝓹𝓽 𝓪 𝓕𝓸𝓵𝓭𝓮𝓻", "𝓑𝓪𝓬𝓴"]


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

# Defining the Banner
Banner = """
░█████╗░███╗░░██╗███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔════╝██║░░░██║
███████║██╔██╗██║█████╗░░██║░░░██║
██╔══██║██║╚████║██╔══╝░░██║░░░██║
██║░░██║██║░╚███║██║░░░░░╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v1.0
An open source File Encryption Program
"""

# Func for Checkin Os
def CheckOs():
    if os.name == "nt":
        return "Windows"
    return "Linux"


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
        x = _width // 2 - len(Element) // 2
        y = _height // 2 - len(_menu_list_1) // 2 + index
        # printing the Elements
        # Checking if the  index is equal to _current_row_index and using elements from _menu_list_2 to print the selected element
        if index == _current_row_index:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y, x, _menu_list_2[index])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y, x, Element)

        # Refershing the screen so show all the updated stuff
        stdscr.refresh()


# Encryption Sub Menu
def _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc):
    stdscr.clear()
    # height and width for encryption sub menu
    height_enc_menu, width_enc_menu = stdscr.getmaxyx()
    for index_enc_menu, _element_enc_menu in enumerate(_sub_menu_list_encrypt):
        x = width_enc_menu // 2 - len(_element_enc_menu) // 2
        y = height_enc_menu // 2 - len(_sub_menu_list_encrypt) // 2 + index_enc_menu
        if index_enc_menu == _current_row_index_submenu_enc:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y, x, _sub_menu_list_encrypt2[index_enc_menu])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y, x, _element_enc_menu)
            # REFRESH SCREEN
        stdscr.refresh()


# Decryption Sub Menu
def _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec):
    stdscr.clear()
    # height and width for encryption sub menu
    height_dec_menu, width_dec_menu = stdscr.getmaxyx()
    for index_dec_menu, _element_dec_menu in enumerate(_sub_menu_list_decrypt):
        x = width_dec_menu // 2 - len(_element_dec_menu) // 2
        y = height_dec_menu // 2 - len(_sub_menu_list_decrypt) // 2 + index_dec_menu
        if index_dec_menu == _current_row_index_submenu_dec:
            stdscr.attron(curses.color_pair(69))
            stdscr.addstr(y, x, _sub_menu_list_decrypt2[index_dec_menu])
            stdscr.attroff(curses.color_pair(69))
        else:
            stdscr.addstr(y, x, _element_dec_menu)
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
    text2 = "Encrypting the File/Folder.."
    stdscr.clear()
    stdscr.attron(curses.color_pair(101))
    Display_text_in_center(stdscr, text2)
    stdscr.attroff(curses.color_pair(101))
    stdscr.refresh()
    time.sleep(2)
    text3 = "File/Folder Has Been Encrypted Successfully..."
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    time.sleep(2)
    text4 = "PLEASE KEEP THE ENCRYPTION KEY SAFE!"
    stdscr.clear()
    stdscr.attron(curses.color_pair(68))
    Display_text_in_center(stdscr, text4)
    stdscr.attroff(curses.color_pair(68))
    stdscr.refresh()
    time.sleep(2)
    text5 = "Returning to Main Menu.wait please."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text5)
    stdscr.attroff(curses.color_pair(69))
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
    text3 = "Checking for Exceptions"
    stdscr.clear()
    stdscr.attron(curses.color_pair(100))
    Display_text_in_center(stdscr, text3)
    stdscr.attroff(curses.color_pair(100))
    stdscr.refresh()
    time.sleep(1.3)
    text4 = "All Operations executed Successfully."
    stdscr.clear()
    stdscr.attron(curses.color_pair(69))
    Display_text_in_center(stdscr, text4)
    stdscr.attroff(curses.color_pair(69))
    stdscr.refresh()
    time.sleep(0.69)


# Function for getting filename
def _get_filename(stdscr):
    filename = Tk()
    if CheckOs() == "Windows":
        filename.FileName = filedialog.askopenfilename(
            initialdir="C:\\", title="Select a File", filetypes=(("All Files", "*.*"),)
        )
        filename.destroy()
        return filename.FileName    
    else:
        # if not windows then linux,IGNOREEEEEEEEE MAC
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
            title="Selecta Key File",
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
    if str(thefilename) == "()":
        stdscr.clear()
        stdscr.attron(curses.color_pair(68))
        Display_text_in_center(stdscr, "Error:OniChan you baka,Choose a File First")
        stdscr.attroff(curses.color_pair(68))
        stdscr.refresh()
        time.sleep(2)


def About(stdscr):
    pass


def DisplayBanner(stdscr):
    # Defining the color scheme here too as color schemes from Main function won't work here
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
        DisplayBanner(stdscr)
    # Calling the Menu Function in Main Function
    Menu(stdscr, _current_row_index)

    # Looping an infinite loop to catch the keys pressed by the user
    while True:
        Key = stdscr.getch()
        stdscr.clear()

        # if usr press up key and the _current_row_index > 0 then decrease the _current_row_index so that we can move to one option upward
        if Key == curses.KEY_UP and _current_row_index > 0:
            _current_row_index -= 1

        # if usr enters the down key and _current_row_index is smaller than lenght of _menu_list_1 - 1 then increase the _current_row_index so we can move downward
        elif Key == curses.KEY_DOWN and _current_row_index < len(_menu_list_1) - 1:
            _current_row_index += 1

        # if user press enter key then check the _current_row_index and show subMenus According to it
        elif Key == curses.KEY_ENTER or Key in (10, 13):
            if _current_row_index == 0:
                # if _current_row_index is 0,meaning that user pressed enter on Encrypt option thenshow the submenu for Encryption menu
                # Calling the Encryption SubMenu
                _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc)
                # Catching Keys pressed by usr
                while True:
                    _key_enc_menu = stdscr.getch()
                    stdscr.clear()
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
                            # function to Check if user didn't choose any file
                            is_file_choosen(stdscr, Filename)
                            stdscr.clear()
                            # Creating object of FileEncryption Class
                            File = FileEncryption()
                            # Some Animated stuff to show before actually Encrypting the file
                            Animated_text_encrypt(stdscr)
                            # Calling the EncryptFile method to encrypt the file
                            File.EncryptFile(Filename)
                            # Calling the Main method cuz will go to main menu after encrypting the file
                            Main(stdscr)

                        # else if user presses the Encrypt a folder option
                        elif _current_row_index_submenu_enc == 1:
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
                            # Creating object of FolderEncryption class
                            Enc = FolderEncryption()
                            # clearing screen before animation
                            stdscr.clear()
                            # Animation before Encrypting dir
                            Animated_text_encrypt(stdscr)
                            Enc.EncryptFoler(Dir)
                            # Calling the main menu after encryption
                            Main(stdscr)
                        elif _current_row_index_submenu_enc == 2:
                            Main(stdscr)
                            # Refreshing
                    stdscr.refresh()
                    # Calling Updated Encrypt Menu
                    _sub_menu_encrypt(stdscr, _current_row_index_submenu_enc)
            elif _current_row_index == 1:
                _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec)
                while True:
                    _key_dec_menu = stdscr.getch()
                    stdscr.clear()
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
                            # CAlling the main menu after decryption
                            Main(stdscr)
                        elif _current_row_index_submenu_dec == 1:
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
                            # Goto main menu after decryption
                            Main(stdscr)
                        elif _current_row_index_submenu_dec == 2:
                            # Go back to Main menu if usr press back option
                            Main(stdscr)
                    stdscr.refresh()
                    _sub_menu_decrypt(stdscr, _current_row_index_submenu_dec)
            elif _current_row_index == 2:
                _about_window = Tk()
                _about_window.title("About ANFU")
                Label(
                    _about_window,
                    text="An open source program for Encryping Files and Folders",
                ).pack()
                Label(_about_window, text="Version:0.1").pack()
                Label(_about_window, text="Distributed under GPLV3").pack()
                Label(
                    _about_window,
                    text="Star the repo(github.com/Justaus3r/Anfu),if you think it deserves.",
                ).pack()
                Label(_about_window, text="Cheers:)..").pack()
                _about_window.mainloop()
                # goto main menu afterr showing about
                Main(stdscr)
            elif _current_row_index == 3:
                os.remove("AnfuTmpcfg.temp")
                sys.exit(0)
            stdscr.getch()
        stdscr.refresh()
        # Displaying the Updated Menu
        Menu(stdscr, _current_row_index)


# Checking and deleting the conf(if exist)files before calling the wrapper function
if os.path.isfile("AnfuTmpcfg.temp") is True:
    os.remove("AnfuTmpcfg.temp")
curses.wrapper(Main)
