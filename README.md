### Readme.md 👋
<img src="https://raw.githubusercontent.com/Justaus3r/Anfu/Master/image/encryption.png">

## Anfu
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
![language](https://badgen.net/badge/Language/Python/cyan)
![semver](https://badgen.net/badge/Semantic-Version/0.3.10/purple)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://github.com/Justaus3r)
[![GitHub commits since](https://img.shields.io/github/commits-since/Justaus3r/Anfu/0.1)]() 
[![Issues](https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000)](https://github.com/Justaus3r/Penta/issues)
[![GitHub Release](https://img.shields.io/github/release/Justaus3r/Anfu?style=flat)]()
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md)
[![DeepSource-active-issues](https://deepsource.io/gh/Justaus3r/Anfu.svg/?label=active+issues&show_trend=true&token=jisXXMKwTBXRZ-KwRsHzyckr)](https://deepsource.io/gh/Justaus3r/Anfu/?ref=repository-badge)
[![DeepSource-fixed-issues](https://deepsource.io/gh/Justaus3r/Anfu.svg/?label=resolved+issues&show_trend=true&token=jisXXMKwTBXRZ-KwRsHzyckr)](https://deepsource.io/gh/Justaus3r/Anfu/?ref=repository-badge)
[![Documentation Status](https://readthedocs.org/projects/anfu/badge/?version=latest)](https://anfu.readthedocs.io/en/latest/?badge=latest)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

A python program to Encrypt Files and Directories using Symmetric(fernet) Encryption.it has a simple Textual user interface(TUI).its available for both Linux and Windows.

## Key Features:
- A simple and attractive TUI(Textual user interface).
- Cross-platform,works on both windows and linux and probably on Mac too(haven't checked on mac tho).
- Enhanced Error-handling,save error's in errorlog on Desktop
- Can also encrypt programs along with other files.
- Portable ,you can either install anfu or either use a portable version.use anytime anywhere.
- Symmetric encryption.Files are encrypted with high level encryption.
- Memory checking module for constantly checking system memory and show warnings when system exceeds 85% of memory usage.
- Change font-type from simple font to fancy font(you need to configure your terminal for showing unicode characters).
- Show tray notification upon encryption and decryption.
- Mouse support,you can use keyboard as well as mouse for selecting options.
- Interactive,can automatically adjust itself to window size.

### Download
**Please disable your antivirus software before running the setup or the executable as it might (falsely)detect anfu as a malicious object due to nature of the program,i will work on fixing this False positive.**
| Operating system:         | Link:                                     | 
| -------------             |:-------------:                            | 
|**Windows**                | [Windows-Installerv0.3.10](https://mega.nz/file/Nw9VRQjC#o5bd92eDAvQfMN7B0hQFB151xUdx8o7uL8IId6uLnfo)/[Windows-Portablev0.3.10](https://mega.nz/file/c18yHACL#Abn-La2BH_AKXrnHeVsVJrfUl-CKgKBLN4kInG4VZLU)|
|**Linux**                  | [Linux-v0.1.2](https://mega.nz/file/0l9GgBQJ#dZfgbZ2NiW8cHilTYMHA1DOt19o852-iLc83Nmejnh4)                |

### Screenshot:

 ![Screenshot](https://drive.google.com/uc?export=download&id=1OHheyOFD38jAC-3QjggYsvdWNe9dt86W)

## Usage:
#### Windows:
Just either download the installer,install and use it or download the portable version,extract it and exectute ```start_anfu.exe```for using it without installation.

#### Linux:
- Download the zip and extract it
- Change the permission of setup file to executable(i.e ```chmod +x setup.sh```)
- Execute the script i.e:```./setup.sh```
- Type ```Anfu``` in terminal and start using it.cheers!


## Build requirements:
if you want to run Anfu as a script ,you will need to install some requirements which are as follows:

[rich](https://pypi.org/project/rich/)

[cryptography](https://pypi.org/project/cryptography/)

[plyer](https://pypi.org/project/plyer/)

you can install them using ```python3 -m pip install -r requirements.txt```.windows users also need to install [windows-curses](https://pypi.org/project/windows-curses/).

### TODO List:
- Encrypt Files with password

### 🔴 Note:
Please keep the encryption key safe,if anyone gets it your data might get compromised.if you don't want to keep the key file then open it and copy the key and keep that key somewhere safe. 

### Conttribution:
All Contributions are Welcomed..Fork the repo and pull requests.Suggestions at x-neron@pm.me or open an [issue](https://github.com/Justaus3r/Anfu/issues)

### Documentation:
A breif Documentation is also available at [readthedocs](https://anfu.readthedocs.io/en/latest/)
### License:
Distributed Under GPLV3
# Changelog

All notable changes to this project will be documented in this file. Dates are displayed in UTC.

#### [0.3.10](https://github.com/Justaus3r/Anfu/compare/0.1.3...0.3.10)

> 9 June 2021

- [ImgBot] Optimize images [`#1`](https://github.com/Justaus3r/Anfu/pull/1)
- Major Update:Bump to version 0.3.10 [`04261b8`](https://github.com/Justaus3r/Anfu/commit/04261b8d37d5820baa71eba0af127fa3e1d75da8)
- Add save Errorlogs on Desktop and Typo's [`d61e7e8`](https://github.com/Justaus3r/Anfu/commit/d61e7e8e90a3d255287ecc7d7e690bd62023d171)
- Delete old source [`1ce10e1`](https://github.com/Justaus3r/Anfu/commit/1ce10e1f3e0bb638eabca64d52a3584341168434)
- Add Mouse support (Experimental).
- Add Change Program title. 
- Add a Help Menu.
- Add more efficient Error handling
- Add a constant memory checking module,and show warnings when system exceeds 85% of memory usage.(Windows only as of now)
- Fix crash if size of program is below 112x32(x,y).
- Add Check disk for space before encrypting a file
- Add Change font-type.
- Add show notification tray upon encrypting and decrypting a file.
- Add check if a file/directory is encrypted/decrypted sucessfully.
- Add check if a file/directory is too large for encryption to prevent malfunction.
- As of version [0.3.10](https://github.com/Justaus3r/Anfu/releases/tag/0.3.10),Anfu is integrated with ConEmu64 Terminal Emulator to overcome windows-interpreter(cmd) limitations.
- Fix minor bugs and Typo's.
- Add backwards compatibility for windows 7.
- Add ```.ankrypt``` extension for files encrypted by Anfu.
#### [0.1.3](https://github.com/Justaus3r/Anfu/compare/0.1.2...0.1.3)

> 30 May 2021

- Reformatted code [`4a66add`](https://github.com/Justaus3r/Anfu/commit/4a66addeef0b9cddb3eb39274df267b708631912)
- Fix open file twice before selecting a file [`7b29797`](https://github.com/Justaus3r/Anfu/commit/7b297973511354b0bdac17a3ba912f22380ec30c)
- Update Docs .

#### [0.1.2](https://github.com/Justaus3r/Anfu/compare/0.1...0.1.2)

> 14 April 2021

- Updated readthedoc [`00c36d2`](https://github.com/Justaus3r/Anfu/commit/00c36d2ad4798ca52c4a518a9d161914dc42e7dd)
- Updated Docs
- Fixed minor bugs
- Fixed Broken links

#### [0.1.0](https://github.com/Justaus3r/Anfu/releases/tag/0.1)

> 12 April 2021

- Initial Release [`6e8a8dd`](https://github.com/Justaus3r/Anfu/commit/6e8a8dd17b37e060e39ef289d95c7253f0cb6640)
- Fixed some Typos [`91f7be5`](https://github.com/Justaus3r/Anfu/commit/91f7be5b8d9fc3741b3f1daa29faadff71c51847)

### Note:
Icons for Anfu are taken from [Flaticon](https://www.flaticon.com/).Credits go to the author
