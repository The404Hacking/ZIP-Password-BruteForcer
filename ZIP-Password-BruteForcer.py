import zipfile
from time import time

def main(file_path: str, pass_list_puth: str):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print(" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
		return None

	i = 0
	c_t = time()
	with open(pass_list_puth, "r") as f:
		passes = f.read().split("\n")

		print(f' [+] Load {len(passes)} passwords')

		for password in passes:
			i += 1
			try:
				zip_.extractall(pwd=password.encode())
				t_t = time() - c_t
				print(f"\n [*] Password Found :)\n" + f" [*] Password: {password}\n")
				print(f" [***] Took {t_t} seconds to Srack the Password. That is, {i} attempts per second.")
				return password
			except:
				pass

		print(" [X] Sorry, Password Not Found :(")
		return None

if __name__ == '__main__':
	textzippass = '''
#########################################
# Zip Password Brute Forcer (Top Speed) #
#########################################
# The404Hacking                         #
# Digital Security ReSearch Group       #
# T.me/The404Hacking                    #
#########################################
	'''
	print(textzippass)

	file_path = input(" [+] ZIP File Address: ")
	word_list = input(" [+] Password List Address: ")

	main(file_path, word_list)