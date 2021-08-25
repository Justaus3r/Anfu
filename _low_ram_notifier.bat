@echo off
rem 
rem ░█████╗░███╗░░██╗███████╗██╗░░░██╗
rem ██╔══██╗████╗░██║██╔════╝██║░░░██║
rem ███████║██╔██╗██║█████╗░░██║░░░██║
rem ██╔══██║██║╚████║██╔══╝░░██║░░░██║
rem ██║░░██║██║░╚███║██║░░░░░╚██████╔╝
rem ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v0.2.0
rem This file is  part of Anfu.py,a tui encryption tool
rem Copyright Justaus3r 2021
rem Distributed under GPLV3
rem  This program is free software: you can redistribute it and/or modify
rem    it under the terms of the GNU General Public License as published by
rem    the Free Software Foundation, either version 3 of the License, or
rem    (at your option) any later version.
rem    This program is distributed in the hope that it will be useful,
rem     but WITHOUT ANY WARRANTY; without even the implied warranty of
rem    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
rem    GNU General Public License for more details.
rem    You should have received a copy of the GNU General Public License
rem    along with this program.  If not, see <http://www.gnu.org/licenses/>.
rem A simple batch file to show notification ,when user exceeds 85% ram usage

rem setting screeen color ,title and version
color 0c
title Anfu Low Ram Notification
set VERSION=0.3.11
mode 94,10
echo    _____          _____      
echo   /  _  \   _____/ ____\_ __ 
echo  /  /_\  \ /    \   __\  ^|  \
echo /    ^|    \   ^|  \  ^| ^|  ^|  /
echo \____^|__  /___^|  /__^| ^|____/ %VERSION%
echo    \/     \/            
echo WARNING!
echo Hey onichan!,you are using too much RAM,stop watching nudes and don't encrypt any file 
echo greater than 100 Mb in meanwhile as it might trigger undesired interferance.

pause 
exit
