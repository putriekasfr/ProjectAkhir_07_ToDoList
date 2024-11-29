pengguna = {}

def registrasi():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in pengguna:
        print("Username sudah terdaftar.")
    else:
        pengguna[username] = password
        print("Registrasi berhasil!")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if pengguna.get(username) == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah.")
        return False

def format_rupiah(angka):
    return f"Rp {angka:,.2f}".replace(',', '.').replace('.00', '') 
def tampilkan_menu():
    print("\n=== Menu keep notes ===")
    print("1. Tambah Catatan")
    print("2. Hapus Catatan")
    print("3. Tampilkan Semua Catatan")
    print("4. Tandai Catatan Selesai")
    print("5. Update Catatan")
    print("6. Cari Catatan")
    print("7. Hitung Total Catatan")
    print("8. Keluar")

def tambah_catatan(catatan_list):
    catatan = input("Masukkan catatan: ")
    kategori = input("Masukkan kategori : ")
    nilai = input("Masukkan budget harga untuk catatan: ")
    
    try:
        nilai = float(nilai) 
    except ValueError:
        print("Nilai tidak valid, menggunakan 0 sebagai nilai default.")
        nilai = 0.0  
    kategori_set = set(kategori.split(","))
    catatan_list.append((catatan, False, kategori_set, nilai))

def hapus_catatan(catatan_list):
    catatan = input("Masukkan catatan yang ingin dihapus: ")
    for item in catatan_list:
        if item[0] == catatan:  
            catatan_list.remove(item)
            print(f"Catatan '{catatan}' berhasil dihapus.")
            return
    print(f"Catatan '{catatan}' tidak ditemukan.")

def tampilkan_catatan(catatan_list):
    if not catatan_list:
        print("Tidak ada catatan.")
    else:
        print("\nDaftar Catatan:")
        index = 1
        for item in catatan_list:
            status = "sudah dibeli/sudah dibayar" if item[1] else "belum dibeli/belum dibayar"
            kategori = ", ".join(item[2])
            nilai = item[3]  
            print(f"{index}. {item[0]} - Status: {status} - Kategori: {kategori} - Nilai: {format_rupiah(nilai)}")
            index += 1

def tandai_selesai(catatan_list):
    catatan = input("Masukkan catatan yang sudah selesai: ")
    for index in range(len(catatan_list)):
        if catatan_list[index][0] == catatan:
            catatan_list[index] = (catatan_list[index][0], True, catatan_list[index][2], catatan_list[index][3])  
            print(f"Catatan '{catatan}' berhasil ditandai sebagai selesai.")
            return
    print(f"Catatan '{catatan}' tidak ditemukan.")

def update_catatan(catatan_list):
    catatan_lama = input("Masukkan catatan yang ingin diupdate: ")
    for index in range(len(catatan_list)):
        if catatan_list[index][0] == catatan_lama:
            catatan_baru = input("Masukkan catatan baru: ")
            kategori = input("Masukkan kategori baru: ")
            nilai = input("Masukkan budget harga yang baru: ")
            
            try:
                nilai = float(nilai)  
            except ValueError:
                print("Nilai tidak valid, menggunakan nilai sebelumnya.")
                nilai = catatan_list[index][3]  
            
            kategori_set = set(kategori.split(","))  
            catatan_list[index] = (catatan_baru, catatan_list[index][1], kategori_set, nilai)  
            print(f"Catatan '{catatan_lama}' berhasil diupdate menjadi '{catatan_baru}'.")
            return
    print(f"Catatan '{catatan_lama}' tidak ditemukan.")

def cari_catatan(catatan_list):
    kata_kunci = input("Masukkan kata kunci untuk mencari catatan: ")
    ditemukan = [item for item in catatan_list if kata_kunci in item[0]]
    
    if ditemukan:
        print("\nCatatan yang ditemukan:")
        for item in ditemukan:
            status = "Selesai" if item[1] else "Belum Selesai"
            kategori = ", ".join(item[2])  
            nilai = item[3]
            print(f"- {item[0]} - Status: {status} - Kategori: {kategori} - budget harga: {format_rupiah(nilai)}")
    else:
        print("Tidak ada catatan yang ditemukan.")
def format_rupiah(angka):
    if angka % 1 == 0:  
        return f"Rp {int(angka):,}".replace(',', '.')
    else: 
        return f"Rp {angka:,.2f}".replace(',', '.').replace('.00', '')  

def hitung_total(catatan_list):
    total_belum_dibeli = sum(item[3] for item in catatan_list if not item[1])  
    total_sudah_dibeli = sum(item[3] for item in catatan_list if item[1])  
    
    print(f"\nTotal nilai dari semua catatan: {format_rupiah(total_belum_dibeli + total_sudah_dibeli)}")
    print(f"Total nilai dari catatan yang sudah dibeli: {format_rupiah(total_sudah_dibeli)}")
    print(f"Total nilai dari catatan yang belum dibeli: {format_rupiah(total_belum_dibeli)}")

catatan_list = []  

while True:
    print("\n=== Menu Utama ===")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1-3): ")
    
    if pilihan == "1":
        registrasi()
    elif pilihan == "2":
        if login():
            while True:
                tampilkan_menu()
                pilihan_todo = input("Pilih opsi (1-8): ")
                
                if pilihan_todo == "1":
                    tambah_catatan(catatan_list)
                elif pilihan_todo == "2":
                    hapus_catatan(catatan_list)
                elif pilihan_todo == "3":
                    tampilkan_catatan(catatan_list)
                elif pilihan_todo == "4":
                    tandai_selesai(catatan_list)
                elif pilihan_todo == "5":
                    update_catatan(catatan_list)
                elif pilihan_todo == "6":
                    cari_catatan(catatan_list)
                elif pilihan_todo == "7":
                    hitung_total(catatan_list)  
                elif pilihan_todo == "8":
                    print("Terima kasih,Program telah selesai.")
                    break
                else:
                    print("Pilih yang bener ayo coba lagi.")
    elif pilihan == "3":
        print("Terima kasih,Program selesai.")
        break
    else:
        print("Pilihan yang bener ayo coba lagi.")
