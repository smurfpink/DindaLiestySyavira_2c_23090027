nim_awal = "23090027"

jumlah_nim_baru = 5

def generate_nim_baru(nim_awal, index):
 
  angka_baru = (100, 999)
  nim_baru = nim_awal[:7] + str(angka_baru)

  nim_baru += f"-{index + 1}"

  return nim_baru

nim_baru_list = []
for i in range(jumlah_nim_baru):
  nim_baru = generate_nim_baru(nim_awal, i)
  nim_baru_list.append(nim_baru)

print("Daftar NIM baru:")
for nim_baru in nim_baru_list:
  print(nim_baru)
