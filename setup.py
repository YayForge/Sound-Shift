import os
import subprocess
import time

def signature():
    string = "≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀ By YAY ❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾"
    signature = """
    ██████╗ ██╗   ██╗    ██╗   ██╗ █████╗ ██╗   ██╗
    ██╔══██╗╚██╗ ██╔╝    ╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝
    ██████╔╝ ╚████╔╝      ╚████╔╝ ███████║ ╚████╔╝ 
    ██╔══██╗  ╚██╔╝        ╚██╔╝  ██╔══██║  ╚██╔╝  
    ██████╔╝   ██║          ██║   ██║  ██║   ██║   
    ╚═════╝    ╚═╝          ╚═╝   ╚═╝  ╚═╝   ╚═╝  

    """
    print(string)
    print(signature)
    print(string)
    print()

def module():
    print("Approval is required to install the necessary PowerShell module ('AudioDeviceCmdlets').")
    mod = 'n'
    while True:
        try:
            mod = input("Would you like to install the module? (y/N): ")
            if mod.lower() == 'y':
                print("Installing PowerShell module...")
                subprocess.call(
                    ["powershell", "Install-Module -Name AudioDeviceCmdlets -Force -Scope CurrentUser"]
                )
                print("PowerShell module installation completed.")
            else:
                print("Module not installed, exiting.")
                time.sleep(3)
                exit()
        except:
            print("Invalid value!")

def list():
    print("Listing audio devices...")
    subprocess.call(
        ["powershell", "Get-AudioDevice -List"]
    )

def input():
    index1 = input("Enter the index number of the first device you want to switch to: ")
    index2 = input("Enter the index number of the second device you want to switch to: ")
    return index1, index2

def file(index1, index2):
    script_content = f"""
import os

appdata_path = os.getenv('LOCALAPPDATA')
my_app_data_path = os.path.join(appdata_path, 'SoundShift')
settings_path = os.path.join(my_app_data_path, 'sound_settings.txt')

if not os.path.exists(my_app_data_path):
    os.mkdir(my_app_data_path)
    with open(settings_path, "w") as file:
        file.write("1")

with open(settings_path, 'r') as file:
    data = file.read()

if data == "1":
    os.system("powershell Set-AudioDevice -Index {index1}")
    with open(settings_path, 'w') as file:
        file.write("0")
elif data == "0":
    os.system("powershell Set-AudioDevice -Index {index2}")
    with open(settings_path, 'w') as file:
        file.write("1")
"""
    
    with open("soundshift.py", "w") as script_file:
        script_file.write(script_content)
    print("A new Python file named 'soundshift.py' has been created. You can now use this file to switch between audio devices.")

signature()
print("Welcome to the Soundshift uploader")
print("Attention: When you add a new sound element, the indexes may change. In this case, it is possible to recreate the soundshift.py script.")
module()
list()
index1, index2 = input()
file(index1, index2)
