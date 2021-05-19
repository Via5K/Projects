#CreteSoftwareSetupFileFromScript
from cx_Freeze import Executable, setup

setup( name = 'Adder', #entering name of the software
	Version = '1.0', #entering verison
	description = 'Beta Verison Of Adder', #entering the description of the software
	author = 'Neeraj',
	executables = [Executable(r'.\WorkingTelegramChannelMemeberAdder.py', #and here in executable we enter the path of the script.
					icon = r'.\emailer.ico', #icon path
					shortcutName = 'Adder', #what do you want your software name
					shortcutDir = 'DesktopFolder')]  # directory where shortcut will be created
	)
	