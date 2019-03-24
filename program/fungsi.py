from data import *
def tambah():
	nama = input("Nama kontak = ")
	nomor = input("Nomor telepon = ")	
	contact[nama] = nomor
def hapus():
	hapus = input("Nama yang ingin dihapus : ")
	if hapus in contact.keys(): 
		del contact[hapus]
	else:
		print("Tidak ada kontak yang bernama =", hapus)
def daftar():
	print("Nama", "Nomor")
	for k, v in contact.items():
		print(k,v)
def cari():
	cari = input("Nama yang mau dicari : ")
	no = contact.get(cari)
	if cari in contact.keys():
		print(cari, "nomornya adalah", no)
	else:
		print("Tidak ada kontak nomornya")
def keluar():
	ulang = False