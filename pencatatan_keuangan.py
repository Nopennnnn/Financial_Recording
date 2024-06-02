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

  
