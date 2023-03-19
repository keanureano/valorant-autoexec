import os
import configparser
import re
import shutil

config = configparser.ConfigParser()
config_path = f"{os.environ['LOCALAPPDATA']}\\VALORANT\\Saved\\Config"


def get_last_known_user():
    config.read(f'{config_path}\\Windows\\RiotLocalMachine.ini')
    last_known_user = config.get('UserInfo', 'LastKnownUser')
    # Output: randomletters
    return last_known_user


def get_valorant_autoexec(user):
    regex_pattern = fr'{user}-.+'
    for autoexec_path in os.listdir(config_path):
        if re.match(regex_pattern, autoexec_path):
            autoexec_path = os.path.join(config_path, autoexec_path)
            # Output: C:\users\USER\AppData\Local\VALORANT\Saved\Config\randomletters-region
            return autoexec_path


def get_local_autoexec(user):
    # Get the current working directory and create a subdirectory named "configs\local_name"
    cwd = os.getcwd()
    local_autoexec_path = os.path.join(cwd, "autoexec", user)
    return local_autoexec_path


def autoexec(valorant_name, local_name, command):
    valorant_path = get_valorant_autoexec(valorant_name)
    local_path = get_local_autoexec(local_name)
    print(f'local_path={local_path}')
    print(f'valorant_path={valorant_path}')
    if (command == "save"):
        print("saved")
        # Remove the existing folder if it exists
        if os.path.exists(local_path):
            shutil.rmtree(local_path)

        # Copy the input folder to the output folder
        shutil.copytree(valorant_path, local_path)

    if (command == "load"):
        print("loaded")
        # Remove the existing folder if it exists
        if os.path.exists(valorant_path):
            shutil.rmtree(valorant_path)

        # Copy the input folder to the output folder
        shutil.copytree(local_path, valorant_path)


last_known_user = get_last_known_user()

autoexec(last_known_user, "megafuse", "load")
