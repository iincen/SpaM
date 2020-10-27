import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		+++++++++++++++++++++++++++++
		-      S P A M  S M S       -
		+---------------------------+
		-       Author : c3n        -
		=============================
		        "TULUNGAGUNG"
TOOLS INI WORK HANYA UNTUK NOMOR INDONESIA +62 !!
1. OTP Olx.co.id
""")
		pilih=int(input('root@kali> '))
		if pilih == 1:
			import src.olx
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))