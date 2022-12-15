@echo off
REM Get Current Script Root Path

title Create Log
SET CurrentSource = %~dp0
SET CopySoruce = %systemdrive%
SET MayaDoc =  %UserProfile%\Documents\maya
call:MENU
pause
EXIT /B 0

:MENU
@echo off
cls
color 0A
@echo on
@echo.
@echo. 	1 = Install AS Tools
@echo. 	2 = Uninstall AS Tools
@echo.
@echo off
SET /P M=Type 1 or 2 then press ENTER:
if %M%==1 call:INSTALL
if %M%==2 call:UNINSTALL

EXIT /B 0

REM Create Log
:INSTALL
if not exist %UserProfile%\Documents\maya call:SETUP_MISSING_SCRIPTS
if exist %UserProfile%\Documents\maya call:CREATE_MOD_FILE
EXIT /B 0

:UNINSTALL
if exist %UserProfile%\Documents\maya\modules\as_tools.mod call:REMOVE_MOD_FILE
EXIT /B 0

:CREATE_MOD_FILE
mkdir %UserProfile%\Documents\maya\modules
(
echo + Rigging_Tool 1.0 %CurrentSource %as_tools\tools
echo scripts: %CurrentSource %as_tools\tools
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Tools
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Modeling
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Rigging
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Animation
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Utillties
echo PYTHONPATH += %CurrentSource %as_tools\tools\mayaScripts\scripts\Help
echo PYTHONPATH += %CurrentSource %as_tools\tools\python/lib/site-packages
echo MAYA_PLUG_IN_PATH += %CurrentSource %as_tools\tools\maya\plugin
echo MAYA_SHELF_PATH += %CurrentSource %as_tools\tools\maya\shelves
) > %UserProfile%\Documents\maya\modules\as_tools.mod
EXIT /B 0

:REMOVE_MOD_FILE
del %UserProfile%\Documents\maya\modules\as_tools.mod
EXIT /B 0

:SETUP_MISSING_SCRIPTS
@echo off
color 0C
cls
@echo on
@echo.
@echo       Maya do not set up.
@echo.
@echo off
pause
call:MENU
EXIT /B 0
