import pandas as pd
from datetime import datetime

def catatan_transaksi(jenis_transaksi):
    deskripsi = input("Masukkan deskripsi transaksi: ")
    jumlah = float(input("Masukkan jumlah transaksi: "))

    now = datetime.now()
    tanggal = now.strftime("%d-%m-%Y %H:%M:%S")

    data = {
        'Tanggal': [tanggal],
        'Jenis': [jenis_transaksi],
        'Deskripsi': [deskripsi],
        'Jumlah': [jumlah]
    }

    df = pd.DataFrame(data)

    try:
        # Baca file Excel jika sudah ada, atau buat DataFrame baru
        existing_data = pd.read_excel(r"C:\Users\noven\Desktop\Pemorograman\TUBEs\keuangan.xlsx")
        updated_data = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        updated_data = df

    # Simpan file excel
    updated_data.to_excel(r"C:\Users\noven\Desktop\Pemorograman\TUBEs\keuangan.xlsx", index=False)
    print("Transaksi berhasil dicatat.")
def main():
    while True:
        print("\nPilih menu:")
        print("1. Catatan Pengeluaran")
        print("2. Catatan Pemasukan")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            catatan_transaksi("pengeluaran")
        elif pilihan == "2":
            catatan_transaksi("pemasukan")
        elif pilihan == "3":
            print("Terima Kasih!")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi.")

if __name__ == "__main__":
    main()