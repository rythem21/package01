from fungsi import *
ulang = True
while(ulang):
	jawab = input("\n(A)dd || (D)elete || (L)ist || (S)earch || (E)xit = ")
	if(jawab == "A" or jawab == "a"):
		tambah()
	elif(jawab == "D" or jawab == "d"):
		hapus()
	elif(jawab == "L" or jawab == "l"):
		daftar()
	elif(jawab == "S" or jawab == "s"):
		cari()
	elif(jawab == "E" or jawab == "e"):
		keluar()