import subprocess

subprocess.run("Disable-NetAdapter -Name Ethernet 2", shell=True)