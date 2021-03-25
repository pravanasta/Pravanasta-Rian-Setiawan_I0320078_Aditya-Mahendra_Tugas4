print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("================== Program Seleksi Kursus =================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

# input bilangan bulat
x = int(input("Berapa usia kamu : "))
y = input("Apakah Anda sudah lulus ujian kualifikasi (y/t) ? ")

# proses output
if x  >= 21 and y == "y" :
    print("Anda dapat mendaftar di kursus.")
else :
    print("Anda tidak dapat mendaftar di kursus.")

print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("===================       SELESAI        ==================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")