dict = {"nama" : ["arabi","rizki","risky","adit"],
		"nim": [182103002,182103003,182103004,182103005],
		"jurusan" :["Sistem informasi","teknik informatika","teknologi informasi","manajemen informatika"],
		"umur" : [19,20,21,22]}

import pandas as pd
br = pd.DataFrame(dict)
print(br)

br.to_csv(index=False,path_or_buf="D:/datamahasiswa.csv")

lin2=br [br.jurusan=="Sistem informasi"]
print(lin2.head())
