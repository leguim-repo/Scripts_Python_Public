#! /usr/bin/env python3.8
# coding=utf-8


"""
pip3 install gitpython
https://gitpython.readthedocs.io/en/stable/intro.html
https://gitpython.readthedocs.io/en/stable/

	if os.path.exists(self.StartFolder+"/"+folder+"/UpGit.sh"):
			print(folder+"\t->\tUpGit.sh\tExecuting UpGit.sh")
			os.chdir(folder)
			#os.system('./UpGit.sh')
			os.chdir(self.StartFolder)
"""

import os
import git


StartFolder = '/Users/miguel/Desktop/Repositorios/jupiter-repo/'

class AutoUpGit():
	def __init__(self,StartFolder):
		self.StartFolder = StartFolder

	def walk(self,action):
		print(self.StartFolder)
		ListOfFolders = next(os.walk(self.StartFolder))[1]
		for folder in ListOfFolders:
			print(folder)
			print("-"*len(folder))
			action(self.StartFolder+"/"+folder)
			print("-"*30)
			print("")

	def isGitFolder(self,folder):
		if os.path.exists(folder+"/.git"):
			return True
		else:
			return False

	def CheckStatusAndUpGit(self,folder):
		if self.isGitFolder(folder):
			repo = git.Repo(folder)
			print(repo.remotes.origin.url)
			print(repo.git.status())
			if "nothing to commit" not in repo.git.status():
				self.ExecuteUpGit(folder)
		else:
			print("Nothing to make")
	
	def ExecuteUpGit(self,folder):
			print(folder+"\t->\tUpGit.sh\tExecuting UpGit.sh")
			os.chdir(folder)
			os.system('./UpGit.sh')
			os.chdir(self.StartFolder)

if __name__ == '__main__':
	w=AutoUpGit(StartFolder)
	w.walk(w.CheckStatusAndUpGit)
