Readme.md 👋
~~~~~~~~~~~

Anfu
----

|GPLv3 License| |Contribution| |language| |Active| |GitHub commits
since| |Issues| |GitHub Release| |Code of Conduct| |Documentation
Status| |Open Source|

A python program to Encrypt Files and Directories using
Symmetric(fernet) Encryption.it has a simple Textual user
interface(TUI).its available for both Linux and Windows.

Key Features:
-------------

-  A simple and attractive TUI(Textual user interface).
-  Cross-platform,works on both windows and linux and probably on Mac
   too(haven't checked on mac tho).
-  Enhanced Error-handling,save error's in errorlog on Desktop
-  Portable ,you can either install anfu or either use a portable
   version.use anywhere anytime.
-  Symmetric encryption.Files are encrypted with high level encryption.
-  Menory checking module for constantly checking system memory and show
   warnings when system exceeds 85% of memory usage.
-  Change font-type from simple font to fancy font(you need to configure
   your terminal for showing unicode characters).
-  Show tray notification upon encryption and decryption.
-  Mouse support,you can use keyboard as well as mouse for selecting
   options.
-  Interactive,can automatically adjust itself to window size.

Download
~~~~~~~~

+---------------------+---------------------------------------------------------------------------------------------------+
| Operating system:   | Link:                                                                                             |
+=====================+===================================================================================================+
| **Windows**         | `Windows-v0.3.10 <https://mega.nz/file/Nw9VRQjC#o5bd92eDAvQfMN7B0hQFB151xUdx8o7uL8IId6uLnfo>`__   |
+---------------------+---------------------------------------------------------------------------------------------------+
| **Linux**           | `Linux-v0.1.2 <https://mega.nz/file/0l9GgBQJ#dZfgbZ2NiW8cHilTYMHA1DOt19o852-iLc83Nmejnh4>`__      |
+---------------------+---------------------------------------------------------------------------------------------------+

Screenshot:
~~~~~~~~~~~

.. figure:: https://drive.google.com/uc?export=download&id=1OHheyOFD38jAC-3QjggYsvdWNe9dt86W
   :alt: Screenshot

   Screenshot
Usage:
------

Windows:
^^^^^^^^

Just either download the installer,install and use it or download the
portable version for using it without installation.

Linux:
^^^^^^

-  Download the zip and extract it
-  Change the permission of setup file to executable(i.e
   ``chmod +x setup.sh``)
-  Execute the script i.e:\ ``./setup.sh``
-  Type ``Anfu`` in terminal and start using it.cheers!

TODO List:
~~~~~~~~~~

-  Encrypt Files with password

🔴 Note:
~~~~~~~

Please keep the encryption key safe,if anyone gets it your data might
get compromised.if you don't want to keep the key file then open it and
copy the key and keep that key somewhere safe.

Conttribution:
~~~~~~~~~~~~~~

All Contributions are Welcomed..Fork the repo and pull
requests.Suggestions at x-neron@pm.me or open an
`issue <https://github.com/Justaus3r/Anfu/issues>`__

Documentation:
~~~~~~~~~~~~~~

A breif Documentation is also available at
`readthedocs <https://anfu.readthedocs.io/en/latest/>`__ ### License:
Distributed Under GPLV3 # Changelog

All notable changes to this project will be documented in this file.
Dates are displayed in UTC.

`0.3.10 <https://github.com/Justaus3r/Anfu/compare/0.1.3...0.3.10>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    9 June 2021

-  [ImgBot] Optimize images
   ```#1`` <https://github.com/Justaus3r/Anfu/pull/1>`__
-  Major Update:Bump to version 0.3.10
   ```04261b8`` <https://github.com/Justaus3r/Anfu/commit/04261b8d37d5820baa71eba0af127fa3e1d75da8>`__
-  Add save Errorlogs on Desktop and Typo's
   ```d61e7e8`` <https://github.com/Justaus3r/Anfu/commit/d61e7e8e90a3d255287ecc7d7e690bd62023d171>`__
-  Delete old source
   ```1ce10e1`` <https://github.com/Justaus3r/Anfu/commit/1ce10e1f3e0bb638eabca64d52a3584341168434>`__
-  Add Mouse support (Experimental).
-  Add Change Program title.
-  Add a Help Menu.
-  Add more efficient Error handling
-  Add a constant memory checking module,and show warnings when system
   exceeds 85% of memory usage.(Windows only as of now)
-  Fix crash if size of program is below 112x32(x,y).
-  Add Check disk for space before encrypting a file
-  Add Change font-type.
-  Add show notification tray upon encrypting and decrypting a file.
-  Add check if a file/directory is encrypted/decrypted sucessfully.
-  Add check if a file/directory is too large for encryption to prevent
   malfunction.
-  As of version
   `0.3.10 <https://github.com/Justaus3r/Anfu/releases/tag/0.3.10>`__,Anfu
   is integrated with ConEmu64 Terminal Emulator to overcome
   windows-interpreter(cmd) limitations.
-  Fix minor bugs and Typo's.
-  Add backwards compatibility for windows 7.
-  Add ``.ankrypt`` extension for files encrypted by Anfu. ####
   `0.1.3 <https://github.com/Justaus3r/Anfu/compare/0.1.2...0.1.3>`__

    30 May 2021

-  Reformatted code
   ```4a66add`` <https://github.com/Justaus3r/Anfu/commit/4a66addeef0b9cddb3eb39274df267b708631912>`__
-  Fix open file twice before selecting a file
   ```7b29797`` <https://github.com/Justaus3r/Anfu/commit/7b297973511354b0bdac17a3ba912f22380ec30c>`__
-  Update Docs .

`0.1.2 <https://github.com/Justaus3r/Anfu/compare/0.1...0.1.2>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    14 April 2021

-  Updated readthedoc
   ```00c36d2`` <https://github.com/Justaus3r/Anfu/commit/00c36d2ad4798ca52c4a518a9d161914dc42e7dd>`__
-  Updated Docs
-  Fixed minor bugs
-  Fixed Broken links

`0.1.0 <https://github.com/Justaus3r/Anfu/releases/tag/0.1>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    12 April 2021

-  Initial Release
   ```6e8a8dd`` <https://github.com/Justaus3r/Anfu/commit/6e8a8dd17b37e060e39ef289d95c7253f0cb6640>`__
-  Fixed some Typos
   ```91f7be5`` <https://github.com/Justaus3r/Anfu/commit/91f7be5b8d9fc3741b3f1daa29faadff71c51847>`__

Note:
~~~~~

Icons for Anfu are taken from
`Flaticon <https://www.flaticon.com/>`__.Credits go to the author

.. |GPLv3 License| image:: https://img.shields.io/badge/License-GPL%20v3-yellow.svg
   :target: https://opensource.org/licenses/
.. |Contribution| image:: https://img.shields.io/badge/Contributions-Welcome-<brightgreen>
.. |language| image:: https://badgen.net/badge/Language/Python/cyan
.. |Active| image:: http://img.shields.io/badge/Status-Active-green.svg
   :target: https://github.com/Justaus3r
.. |GitHub commits since| image:: https://img.shields.io/github/commits-since/Justaus3r/Anfu/0.1
   :target: 
.. |Issues| image:: https://img.shields.io/github/issues-raw/Justaus3r/Penta?maxAge=25000
   :target: https://github.com/Justaus3r/Penta/issues
.. |GitHub Release| image:: https://img.shields.io/github/release/Justaus3r/Anfu?style=flat
   :target: 
.. |Code of Conduct| image:: https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat
   :target: https://github.com/Justaus3r/Penta/blob/main/docs/CODE_OF_CONDUCT.md
.. |Documentation Status| image:: https://readthedocs.org/projects/anfu/badge/?version=latest
   :target: https://anfu.readthedocs.io/en/latest/?badge=latest
.. |Open Source| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
   :target: https://opensource.org/
