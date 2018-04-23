import subprocess
url = 'http://suporte.ti.vet.ufmg.br/instalacao/vnc/instalar_vnc.ps1'
subprocess.call(["powershell.exe", "-NoProfile", "-InputFormat", "None", "-ExecutionPolicy", "Bypass", "-Command", "iex ((New-Object System.Net.WebClient).DownloadString(\'%s\'))" % url])
