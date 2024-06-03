pip install pyyaml
pip install xmltodict
pip install pyinstaller


Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Install-Module -Name PowerShellGet -Force -AllowClobber