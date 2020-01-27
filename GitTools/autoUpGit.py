#! /usr/bin/env python3.6
# coding=utf-8

import os

if __name__ == '__main__':
	#os.chdir(path)
	#StartFolder = os.path.dirname(os.path.realpath(__file__))
	# Directorio base del repositorio
	StartFolder = '/Users/mike/Desktop/repositories/'
	print(StartFolder)
	ListOfFolders = next(os.walk('.'))[1]
	for folder in ListOfFolders:
		if (folder != 'gitlab_template'):
			if os.path.exists(folder+"/UpGit.sh"):
				print(folder+"\t->\tUpGit.sh\tExecuting UpGit.sh")
				os.chdir(folder)
				os.system('./UpGit.sh')
				os.chdir(StartFolder)
			else:
				print(folder)
			print("-"*30)

			
