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
    os.system("powershell Set-AudioDevice -Index 2")
    with open(settings_path, 'w') as file:
        file.write("0")

elif data == "0":
    os.system("powershell Set-AudioDevice -Index 1")
    with open(settings_path, 'w') as file:
        file.write("1")