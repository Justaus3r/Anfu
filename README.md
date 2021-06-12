### Readme.md 👋
<img src="https://raw.githubusercontent.com/Justaus3r/Anfu/Master/image/encryption.png">

## Anfu
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![Contribution](https://img.shields.io/badge/Contributions-Welcome-<brightgreen>)
![language](https://badgen.net/badge/Language/Python/cyan)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://github.com/Justaus3r)
[![GitHub commits since](https://img.shields.io/github/commits-since/Justaus3r/Anfu/0.1)]() 
[![Issues](https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000)](https://github.com/Justaus3r/Penta/issues)
[![GitHub Release](https://img.shields.io/github/release/Justaus3r/Anfu?style=flat)]()
[![Code of Conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat)](https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md) 
[![Documentation Status](https://readthedocs.org/projects/anfu/badge/?version=latest)](https://anfu.readthedocs.io/en/latest/?badge=latest)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

A python program to Encrypt Files and Directories using Symmetric(fernet) Encryption.it has a simple Textual user interface(TUI).its available for both Linux and Windows.

### Download
| Os:         | Link:                                     | 
| ------------- |:-------------:                               | 
|**Windows(10 only)**    | [Windows](https://drive.google.com/uc?export=download&id=1LVW8_62BQCcQy913dx6uIJla218wIy6M)|
|**Linux**      | [Linux](https://drive.google.com/uc?export=download&id=1WSOFs3nU9ZGHlyIVa5EJ-7_r4fA4voiC)  |

### Alternative Mirror:
If above link is not working,you can also download Anfu(windows) from [Source-forge](https://sourceforge.net/projects/anfu/files/Anfu.exe/download)

### Screenshot:

 ![Screenshot](https://drive.google.com/uc?export=download&id=1ZDll6R1LYuY_E9zpaklfI3i3DgEa45yi)

## Usage:
#### Windows:
Just download the executable and start using it

##### Linux:
- Download the zip and extract it
- Change the permission of setup file to executable(i.e ```chmod +x setup.sh```)
- Execute the script i.e:```./setup.sh```
- Type ```Anfu``` in terminal and start using it.cheers!
### Key Features
- A simple and attractive TUI(Textual user interface).
- Portable ,no need for installation.install anywhere anytime
- Symmetric encryption.Files are encrypted with high level encryption
- Can Automatically Adjust itself with the screen at start time.

### TODO List:
- Encrypt Files with password

### 🔴 Note:
Please keep the encryption key safe,if anyone gets it your data might get compromised.if you don't want to keep the key file then open it and copy the key and keep that key somewhere safe. 

### Conttribution:
All Contributions are Welcomed..Fork the repo and pull requests.Suggestions at x-neron@pm.me

### Documentation:
A breif Documentation is also available at [readthedocs](https://anfu.readthedocs.io/en/latest/)
### License:
Distributed Under GPLV3
## Changelog

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
