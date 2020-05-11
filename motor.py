import pandas as pd

print("----------- Program Sorting data penjualan motor ------------")

print()

tipe = []
kode_mesin = []
asal_pabrik = []
tahun_penjualan = []

def masukan():
	tipe.append(input("Masukkan tipe motor \t\t\t: "))
	kode_mesin.append(int(input("Masukkan kode mesin \t\t: ")))
	asal_pabrik.append(input("Masukkan asal pabrik \t\t: "))
	tahun_penjualan.append(int(input("Masukkan tahun penjualan \t\t: ")))
	print()

x = int(input("Masukkan jumlah data yang mau di input :"))
for i in range(x):
	masukan()
motor = {"tipe":tipe,"kode_mesin":asal_pabrik,"asal_pabrik":asal_pabrik,"tahun_penjualan":tahun_penjualan}
data = pd.DataFrame(motor)	
print()
save = data.to_excel('motor.xlsx')


def tampil():
	baca = pd.read_excel('motor.xlsx') 
	print(baca)
	print()

def urut():
	baca = pd.read_excel('motor.xlsx') 
	urut = data.sort_values(by=['tipe'])
	print(urut)
	print()

def simpan():
	baca = pd.read_excel('motor.xlsx') 
	urut = data.sort_values(by=['tipe'])
	save = urut.to_excel('book_urut.xlsx')
	print("Data Sudah Tersimpan!!!")
	print()

def out():
	print("--------------------------------------------------")
	print("--------------- Terimakasih ----------------------")
	print("--------------------------------------------------")


def option():
	print("--------------------------------------------------")
	print("----------------- Daftar Pilihan  ----------------")
	print("--------------------------------------------------")	
	print("1.Tampilkan Data")
	print("2.Urutkan Data")
	print("3.Simpan Data")
	print("4.Keluar")
	print("--------------------------------------------------")	
	print()
	a = int(input("Masukkan pilihan anda :"))
	for i in range(a):
		if a==1:
			tampil()
		elif a==2:
			urut()
		elif a==3:
			simpan()
		elif a==4:
			out()
			break
		return option()
option()