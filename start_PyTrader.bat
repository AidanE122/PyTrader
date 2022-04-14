@ECHO off

COLOR A

set "script_path=%~dp0"
set "script_path=%script_path%main.py"

python %script_path% %*