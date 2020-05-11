jumlah = 75000
hasil=jumlah/100000
sisa=jumlah%100000
print ("jumlah uang pecahan anda")
print()
print (hasil, "seratusribuan")
print(sisa, "rupiah")
print()
if (sisa>=50000):
    hasil=sisa/50000
    sisa=sisa%50000
    print (hasil, "lima puluh ribuan")
    print(sisa, "rupiah")
    print()
if (sisa>=20000):
    hasil=sisa/20000
    sisa=sisa%20000
    print (hasil, "dua puluh ribuan")
    print(sisa, "rupiah")
    print()
if (sisa>=10000):
    hasil=sisa/10000
    sisa=sisa%10000
    print (hasil, "sepuluh ribuan")
    print(sisa, "rupiah")
    print()
if (sisa>=5000):
    hasil=sisa/5000
    sisa=sisa%5000
    print (hasil, "lima ribuan")
    print(sisa, "rupiah")
    print()
if (sisa>=1000):
    hasil=sisa/1000
    sisa=sisa%1000
    print (hasil, "seribuan")
    print(sisa, "rupiah")
    print()
if (sisa>=500):
    hasil=sisa/500
    sisa=sisa%500
    print (hasil, "lima ratusan")
    print(sisa, "rupiah")
    print()
if (sisa>=100):
    hasil=sisa/100
    sisa=sisa%100
    print (hasil, "seratusan")
    print(sisa, "rupiah")
    print()
