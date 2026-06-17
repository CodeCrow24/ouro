@echo off
pushd "%~dp0"
"%SystemRoot%\py.exe" ouro.py %*
popd
pause