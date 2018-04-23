import os
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
cls()
banner = '\n ###################################\n'
banner += ' # ZIP Password BruteForcer        #\n'
banner += ' ###################################\n'
banner += ' # Coded By Sir.4m1R               #\n'
banner += ' # The404Hacking                   #\n'
banner += ' # Digital Security ReSearch Group #\n'
banner += ' # T.me/The404Hacking              #\n'
banner += ' ###################################\n'
banner += ' GitHub:\n'
banner += ' https://github.com/The404Hacking/ZIP-Password-BruteForcer\n\n'
banner += ' [1] Zip Password Cracker\n'
banner += ' [0] Exit\n'
print banner

a=input(" [?] Enter Number : ")
if a==0:
 import os
 cls()
 print " [!] Good Bye :)"
 quit()
elif a==1:
 #!/usr/bin/python

 import zipfile
 import os
 from time import time
 
 cls()
 textzippass = '''
 #########################################
 # Zip Password Brute Forcer (Top Speed) #
 #########################################
 # The404Hacking                         #
 # Digital Security ReSearch Group       #
 # T.me/The404Hacking                    #
 #########################################
 '''
 print textzippass
 file_path = raw_input (" [+] ZIP File Address: ")
 print ""
 word_list = raw_input (" [+] Password List Address: ")
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print " [!] Please check the file's Path. It doesn't seem to be a ZIP file."
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				print "\n [*] Password Found :)\n" + " [*] Password: "+password+"\n" 
				print " [***] Took %f seconds to Srack the Password. That is, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print " [X] Sorry, Password Not Found :("
		quit()
 main(file_path, word_list)