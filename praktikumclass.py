datamhs = []
pilih = 0

class Mahasiswa():
    def __init__(self, nama, nim, kelas, nilai):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.nilai = nilai

    def input(self):
        print(f"Nama Anda\t:  {self.nama}")
        print(f"NIM Anda\t: {self.nim}")
        print(f"Kelas Anda: {self.kelas} ")
        print(f"Nilai UAS\t: {self.nilai}")
        print("===")


def menu():
    print("Daftar Nilai Mahasiswa")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    try:
        pilih = int(input("Masukan Pilihan Menu Anda : "))
    except:
        print('MASUKAN ANGKA!')
    else:
        print()
        if pilih == 1:
            tambah()
        elif pilih == 2:
            tampilkan()
        elif pilih == 3:
            hapus()
        elif pilih == 4:
            ubah()
        elif pilih == 5:
            keluar()
        else:
            print("Input Menu Salah !")
            print()
            input("Enter untuk ke Menu Utama. . .")
            print()
            menu()


def tambah():
    try:
        print("Menambahkan Data")
        nama = str(input("Masukan Nama\t: "))
        nim = int(input("Masukan NIM\t: "))
        kelas = str(input("Masukan Kelas\t: "))
        nilai = int(input("Masukan Nilai UAS\t: "))
    except:
        print('MASUKAN ANGKA!')
        print("=============================================")
        menu()

    else:    
        datamhs.append({
        "nama": nama,
        "nim": nim,
        "kelas": kelas,
        "nilai": nilai
    })
        print("Data berhasil ditambahkan !")
        print()
        input("Enter untuk ke Menu Utama. . .")
        print()
        menu()


def tampilkan():
    if len(datamhs) == 0:
        print("Tidak Ada Data !")
        print("Tambah data dahulu sebelum membuka menu ini !")
    else:
        print("Daftar Nilai Mahasiswa")
        print("Total Mahasiswa : ", len(datamhs))
        print("=" * 20)

        for item in datamhs:
            item1 = item["nama"]
            item2 = item["nim"]
            item3 = item["kelas"]
            item4 = item["nilai"]
            items = Mahasiswa(item1, item2, item3, item4)
            items.input()

    print()
    input("Enter untuk ke Menu Utama. . .")
    print()
    menu()


def hapus():
    if len(datamhs) == 0:
        print("Tidak Ada Data !")
        print("Tambah data terlebih dahulu !")
    else:
        print("Hapus Data Siswa")
        for i in range(len(datamhs)):
            _hapus = input("Masukan Nama Mahasiswa : ")
            if _hapus == datamhs[i]["nama"]:
                del datamhs[i]
                print("Data berhasil dihapus")
                break
            else:
                print("data tidak di temukan")
                break
    print()
    input("Enter untuk ke Menu Utama. . .")
    print()
    menu()


def ubah():
    if len(datamhs) == 0:
        print("Tidak Ada Data !")
        print("Tambah data dahulu sebelum membuka menu ini !")
    else:
        print("Ubah Data Siswa")
        for i in range(len(datamhs)):
            _ubah = input("Masukan Nama Mahasiswa : ")
            if _ubah == datamhs[i]["nama"]:
                print("Data telah ditemukan")
                _tambah = input("Masukan Nama Baru : ")
                print()
                datamhs[i]["nama"] =_tambah
                print("Data telah diubah")
                break
            else:
                print("data tidak di temukan")
    print()
    input("Enter untuk ke Menu Utama. . .")
    print()
    menu()


def keluar():
    keluar = input("Yakin ingin keluar? (Y/T) : ")
    if keluar == "y" or keluar == "Y":
        exit()
    else:
        menu()
        print()

menu()



