import numpy as np
import pandas as pd

class Transactions(dict):
    def __init__(self):
        self = dict()
        
    def add_item(self, nama_item, jumlah_item, harga_item):
        '''
        Menambahkan item kedalam transaksi
        '''
        
        # Declare valriable
        self.nama_item = nama_item
        self.jumlah_item = jumlah_item
        self.harga_item = harga_item
        
        # Assign variables into dictionary
        self[nama_item] = [jumlah_item, harga_item]
        
        return f'Item yang dibeli adalah: {self}'
                    

    def update_item_name(self, nama_item, nama_item_baru):
        '''
        Memperbaharui nama item yang telah diinput
        '''
        
        # Declare valriable
        self.nama_item = nama_item
        self.nama_item_baru = nama_item_baru
        
        # Copy new dictionary from old one
        self[nama_item_baru] = self[nama_item]
        
        # Delete the old one
        del self[nama_item]
        
        return f'Item yang dibeli adalah: {self}'


        
    def update_item_qty(self, nama_item, jumlah_item_baru):
        '''
        Memperbaharui jumlah item yang telah diinput
        '''
        
        # Deklarasi variabel
        self.nama_item = nama_item
        self.jumlah_item_baru = jumlah_item_baru
        
        # Ganti value jumlah dari nama item terpilih
        self[nama_item][0] = jumlah_item_baru
        
        return f'Item yang dibeli adalah: {self}'
        
        
    def update_item_price(self, nama_item, harga_item_baru):
        '''
        Memperbaharui harga item yang telah diinput
        '''
        # Deklarasi variabel
        self.nama_item = nama_item
        self.harga_item_baru = harga_item_baru
        
        # Ganti value harga dari nama item terpilih
        self[nama_item][1] = harga_item_baru
        
        return f'Item yang dibeli adalah: {self}'
        
        
    def delete_item(self, nama_item):
        '''
        Menghapus sebuah item yang telah diinput
        '''
        
        # Deklarasi variabel
        self.nama_item = nama_item
        
        # Menghapus key:value dalam dictionary
        del self[nama_item]
        
        return f'Item yang dibeli adalah: {self}'
        
        
    def reset_transaction(self):
        '''
        Menghapus seluruh item yang telah diinput
        '''
        
        # Hapus seluruh dictionary
        self.clear()
        
        return 'Semua item berhasil didelete!'
    
    def check_order(self):
        '''
        Menampilkan tabel yang berisi seluruh item yang telah dibeli.
        Kolom pada tabel berupa Nama Item, Jumlah Item, Harga Barang, Total Harga.
        '''
        
        # Deklarasi checker yang akan berubah ketika ada kesalahan
        checker = True
        
        # Cek eksistensi kesalahan input dari user
        for item in self:
            if len(self[item]) == 2 and item != np.nan:
                pass
            else:
                checker = False
        
        # Tampilkan message berdasarkan hasil cek
        if checker:
            print('Pemesanan sudah benar')
        else:
            print('Terdapat kesalahan')
        
        # Konstruksi tabel hasil untuk ditampilkan
        table = pd.DataFrame(self).T.reset_index()
        table = table.rename(columns={'index': 'Nama Item', 0: 'Jumlah Item', 1: 'Harga Barang'})
        table.index = np.arange(1, len(table) + 1)
        table['Total Harga'] = table['Jumlah Item'] * table['Harga Barang']
        
        return table
    
    def total_price(self):
        '''
        Menampilkan total keseluruhan biaya yang harus dibayarkan setelah diskon.
        Diskon 5% apabila total biaya diatas Rp 200.000
        Diskon 8% apabila total biaya diatas Rp 300.000
        Diskon 10% apabila total biaya diatas Rp 500.000
        '''
        
        # Konstruksi tabel dari dictionary
        table = pd.DataFrame(self).T.reset_index()
        table = table.rename(columns={'index': 'Nama Item', 0: 'Jumlah Item', 1: 'Harga Barang'})
        table.index = np.arange(1, len(table) + 1)
        
        # Hitung Total Harga dari jumlah item x harga item
        table['Total Harga'] = table['Jumlah Item'] * table['Harga Barang']
        
        # Jumlahkan kolom Total Harga
        bayar = table['Total Harga'].sum()
        
        # Penerapan diskon terhadap total harga
        if bayar < 200000:
            pass
        elif bayar < 300000:
            bayar = int(bayar*0.95)
        elif bayar < 500000:
            bayar = int(bayar*0.92)
        else:
            bayar = int(bayar*0.90)
        
        return bayar

