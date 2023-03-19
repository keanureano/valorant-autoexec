# This Python script allows you to easily copy your VALORANT autoexec file to and from your local machine.

## Prerequisites
- Python 3.x
- configparser
- shutil

## How to use
1. Open the script in your Python editor of choice.
2. Ensure that the necessary packages are installed.
3. Set the `valorant_name` variable to the name of the user whose autoexec file you want to copy.
4. Set the `local_name` variable to the name you want to use for the local copy of the autoexec file.
5. Set the `command` variable to either "save" or "load", depending on whether you want to copy the autoexec file to your local machine or back to VALORANT, respectively.
6. Run the script.

When you run the script with the "save" command, the autoexec file for the specified user will be copied to your local machine and stored in a folder named after the `local_name` variable. When you run the script with the "load" command, the autoexec file in the specified local folder will be copied back to VALORANT.
