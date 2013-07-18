#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Brute_force_Archive_ZIP-RAR_files.py
# Cracker un Targetfile Zip / RAR
# Copyright (C) 2013  "[THE DOUBL]"  - https://twitter.com/The_doubl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from time import sleep
import sys
import zipfile
import rarfile
import os.path
import optparse
from threading import Thread
from threading import *
from sys import exit

#For windows
#rarTargetfile.UNRAR_TOOL = "C:\Program Targetfiles (x86)\WinRAR\unrar.exe "
#rarTargetfile.UNRAR_TOOL = "C:\Program Targetfiles (x86)\7-Zip\7zFM.exe"
#rarTargetfile.UNRAR_TOOL ="C:\Program Targetfiles (x86)\WinRAR\WinRAR.exe"
rarfile.UNRAR_TOOL = "unrar"


parser = optparse.OptionParser("Usage: python crack_zip.py -f <file> -d <dicfile>")
parser.add_option('-f', dest='Targetfile', type='string',help='specifier le Targetfile zip')
parser.add_option('-d', dest='dicfile', type='string',help='Specify dictionary file')
(options, args) = parser.parse_args()

if (options.Targetfile == None) | (options.dicfile == None):
  print parser.usage
	exit(0)
else:
	Targetfile = options.Targetfile
	dicfile = options.dicfile



def crackfile(Targetfile, password):
	try:
		Targetfile.extractall(pwd=password)
		#screenLock.acquire()
		print'\n[+]  PASSWORD FOUND!! {-_-} ! \n'
		for i in range(21):
		    sys.stdout.write('\r')
		    sys.stdout.write("PROCESSING... [%-20s] %d%%" % ('='*i, 5*i))
		    sys.stdout.flush()
		    sleep(0.25)
		#print"\n ---------------------------------------------------------------------------"
		print '\n[+] PASSWORD:' + password #+ '\n'
		print 'MISSION #BREAKARCHIVE ACCOMPLISHED!'
	
	except:
		def recherche():
			#sys.stdout.write('\r')
			a="."
			sys.stdout.write(a)
		recherche()
		a=" "
		sleep(0.25)
	

def main():
	finished=False

	#What is the tipe of file ?	
	Targetfile=options.Targetfile
	print'\n'
	print '################################################################################\n'
	print '#############                       WELCOME                        ###########\n'
	print '################################################################################'
 	
 	if (zipfile.is_zipfile(Targetfile)):
 		Targetfile=zipfile.ZipFile(Targetfile)

 		print '\n'
 		print 'TYPE OF THE ARCHIVE: ZIP \n'
		print'STRUCTURE OF  ZIPFILE'
		print'--------------------------------------------------------------------------------'
		Targetfile.printdir()
		elts=Targetfile.infolist()
		
		i=1	
		for item in elts:
			
			filename=os.path.basename(item.filename)
			if filename=='':
				filename="Directory"
			print'--------------------------------------------------------------------------------'
			print "file %d:" %i ,filename.upper(), '\n', 
			print "  [+]VERSION NEEDED TO crackfile ARCHIVE :",  item.extract_version, '\n',
			print "  [+]SYSTEM WITCH CREATED THE ARCHIVE:", SystemSource(item.create_system), '\n',
			print "  [+]VERSION WHICH CREATED THE ARCHIVE:", item.create_version,'\n',
			print "  [+]TYPE OF COMPRESSION FOR THE FILE:", typecompress(item.compress_type), '\n',
			print "  [+]SIZE OF THE COMPRESSED FILE:", item.compress_size,  'octets \n',
			print "  [+]SIZE OF THE UNCOMPRESSED FILE:", item.file_size, 'octets \n\n',			
			i=i+1

 	elif(rarfile.is_rarfile(Targetfile)):
 		Targetfile=rarfile.Rarfile(Targetfile)

 		print '\n'
 		print 'TYPE OF ARCHIVE: RAR \n'
		print'ARCHITECHTURE DU Targetfile RAR'
		print'--------------------------------------------------------------------------------'

		elmts=Targetfile.infolist()

		i=1    #INDEX OF FILE
		for item in elmts:
			
			print "FILE %d:" %i ,os.path.basename(item.filename), '\n', 
			print "  [+]VERSION NEEDED TO crackfile ARCHIVE :",  item.extract_version, '\n',
			print "  [+]SYSTEM WITCH CREATED THE ARCHIVE:", SystemSource(item.host_os), '\n',
			print "  [+]COMPRESSION MODE:", item.mode,'\n',
			print "  [+]TYPE OF COMPRESSION FOR THE FILE:", typecompress(item.compress_type), '\n\n',
			i=i+1


 	else:
 		print"CHOOSE A RAR / ZIP ARCHIVE"
 		exit()

 
	#BRUTEFORCING....
	dico = open(dicfile) 
	
	print'--------------------------------------------------------------------------------'
	print'PROCESSING...'
	#i=0
	for line in dico.readlines(): #READING DICTFILE
		password = line.strip('\n')
		
		t = Thread(target=crackfile, args=(Targetfile, password)) 
		t.start()




#SYSTEM WHICH CREATED THE ARCHIVE 
def SystemSource(x):
	if (rarfile.is_rarfile(Targetfile)):
		return {1: 'MSDOS',2: 'OS2', 3: 'UNIX', 4: 'MACOS', 5: 'BEOS',}[x]
	else:
		return { 0: 'Win32', 3: 'UNIX',}[x]

#TYPE OF COMPRESSION
def typecompress(y):
	return{0:'ZIP_STORED (aucun)',8:'ZIP_DEFLATED (zlib)'}[y]

if __name__ == '__main__':
	main()
