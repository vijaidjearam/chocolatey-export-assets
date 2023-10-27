Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
New-Item -ItemType Directory -Path C:\Users\WDAGUtilityAccount\Desktop\chocolatey-export-assets
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/vijaidjearam/chocolatey-export-assets/main/chocolatey-export-assets.py" -OutFile "C:\Users\WDAGUtilityAccount\Desktop\chocolatey-export-assets\chocolatey-export-assets.py"
choco install -y python
python.exe -m pip install --upgrade pip
pip install requests
