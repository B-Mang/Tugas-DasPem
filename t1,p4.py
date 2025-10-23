gp = 300000
nk = input("Masukkan nama karyawan :")
g = int(input("Masukkan golongan anda (1/2/3) :"))
p = str(input("Masukkan Pendidikan Anda (SMA/D1/D3/S1) :"))
jk = int(input("Masukkan jam kerja anda :"))
lm = jk > 8
jl = jk - 8

if g == 1:
    tb = 0.5
elif g == 2:
    tb = 0.1
elif g == 3: 
    tb = 0.15
else:
    print("Tunjangan untuk golongan anda tidak ada")
    tb = 0

if p == "SMA":
    tp = 0.25
elif p == "D1":
    tp = 0.05
elif p == "D3": 
    tp = 0.2
elif p == "S1":
    tp = 0.3
else:
    print("Tunjangan untuk Pendidikan anda tidak ada")
    tb = 0

if lm == True:
    blm = jl * 3500

ttj = tb * gp
ttp = tp * gp
t = ttp + ttj
total = gp + t + blm

print("Karyawan yang bernama :", nk)
print("Tunjangan jabatan :", ttj)
print("Tunjangan pendidikan :", ttp)
print("Honor lembur :", blm)
print("Total gaji (Gaji pokok + tunjangan + lembur) :", total)

