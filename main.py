"""
main.py - Mass Files Creator

This script is the main file required to run the tool, this script serves the functionality of creating mass amount of waste files throughout the entire directory tree as per user specified location.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : September 28, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
2. Nikhil Raj Pandey (github:https://github.com/nikhilrajpandey,email:nikhilrajpandey1@gmail.com)
"""

# Importing the required functions and modules
from os import path, listdir,chdir
from random import randint
from sys import platform

# Checking whether color code variables are supported or not
if 'linux' in platform:
	# If the platform type is linux, then we define the color code variables

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	defcol = '\033[00m'
else:
	# If the platform type is not linux, then we define the color code variables as blank strings

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	defcol = ''

def random_text(text_length,start,end):
	""" This Function will just give you random ascii letters in range of 'start' and 'end' of a given length. For Example random_text(5,0,256) will give you 5 random ascii letters of range 0 and 256 in a string.
	"""

	text = ''
	for i in range(text_length):
		text +=  chr(randint(start, end)) # Ascii Visible characters are from 32 to 127
	return text

def massfilescreator(directory):
	""" This function serves the functionality of creating mass number of files (either filled with unreadable contents or empty). The files may consume up space in the specified directory. The function takes 1 parameter : directory. The 'directory' parameter is used to specify the target directory where the files are about to be created. The files are not only created in the user requested directory, but created in the entire directory tree i.e., the files are created in each and every sub-folder of the user specified directory and even created inside the sub-folders of the first layer sub-folder. Thus, files are created under each and every sub-folders and spreaded across the roots of the directory tree. This function is a recursive function, re-calls itself when struck by each sub-directory. """

	# Changing the current working directory to the user specified directory
	chdir(directory)
	listdir_copy = listdir()

	# Choosing a random count of which files are to be created
	count = randint(10, 100)

	for _ in range(count):
		# Iterating through the loop for the randomly chosen amount of time

		# Creating waste contents of the file
		contents = random_text(randint(1000,3000),0,256)

		# Chosing filename
		filename_length = randint(3,10)
		filename = random_text(filename_length,97,122)
		filename_extension = '.' + random_text(randint(2,4),97,122)
		filename += filename_extension

		# Saving the contents to a file with randomly choosen name
		open(filename, 'w+').write(contents)

		# Displaying the message on the console screen
		print(f'[{green}!{defcol}] Created file : {yellow}{filename}{defcol}')

	# Checking for sub-folders in the directory
	for item in listdir_copy:
		# Iterating through each item in the directory

		if path.isdir(item):
			# If the currently iterated item is a directory, then we re-call the function with the newly specified sub-folder path
			massfilescreator(item)
	chdir('..') # Stepping out from the current directory

def main():
	# Asking the user for the directory location
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Calling the massfilescreator() function in order to launch the attack
	massfilescreator(directory)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message on the console screen

		print(red_rev + f'[ Error : {e} ]' + defcol)
		exit()
