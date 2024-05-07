#biner
nomor_telepon = "085967122171"
enam_angka_terakhir = nomor_telepon[-6:]  


bilangan_biner = ""
for digit in enam_angka_terakhir:
    biner_digit = bin(int(digit))[2:]  
    bilangan_biner += biner_digit.zfill(4)  

print("Nomor telepon (6 angka terakhir):", enam_angka_terakhir)
print("Bilangan biner:", bilangan_biner)


#heksa
nomor_desimal = 122171


nomor_string = str(nomor_desimal)

enam_angka_terakhir = nomor_string[-6:]

nomor_heksadesimal = hex(int(enam_angka_terakhir))

print("Konversi heksadesimal:", nomor_heksadesimal)

#oktal
nomor_hp = "122171"

nomor_desimal = int(nomor_hp)

nomor_oktal = oct(nomor_desimal)

print("Nomor handphone dalam bilangan oktal:", nomor_oktal[2:])
