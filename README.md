# Super-Cashier

## Background
Super Cashier adalah back end dari sebuah self service cashier app pada sebuah Supermarket. Super Cashier membantu pelanggan supermarket untuk mengatur barang belanja yang ia beli di supermarket. Hal yang diharapkan dari Super Cashier adalah fungsionalitas sebagai berikut:
1. Dapat menginput data belanja pelanggan
2. Dapat mengatur data belanja dengan fungsionalitas CRUD (Create, Read, Update, Delete)
3. Dapat menghitung total belanja pelangan dengan otomatis mengaplikasikan diskon apabila pelanggan memenuhi syarat

Adapun flow chart fungsi dari app ini adalah sebagai berikut:

![python project](https://user-images.githubusercontent.com/59790033/205500156-3d31950a-2d8c-4d96-8ea9-95b978c6df40.png)

## Script
Script scashier.py adalah script modular menjalankan app Super Cashier termasuk segala fungsi didalamnya. Dalam script scashier.py terdapat 7 fungsi:
1. add_item
2. update_item_name
3. update_item_qty
4. update_item_price
5. delete_item
6. reset_transaction
7. check_order


### add_item
**Kegunaan:** untuk memasukan sebuah item kedalam list belanja.

**Input:** menerima input berupa 1 string dan 2 angka. String merupakan nama item, angka pertama adalah jumlah item dan angka kedua adalah harga item.

![image](https://user-images.githubusercontent.com/59790033/205500978-92d5ec21-2827-4f8f-85c7-a234775aa722.png)

**Mekanisme:** fungsi akan membuat dictionary dengan format {nama_item: [jumlah_item, harga_item]}, lalu mengembalikan dictionary tersebut dengan keterangan tambahan.

![image](https://user-images.githubusercontent.com/59790033/205501063-aa770d76-14cc-407b-9968-b0daa57587ef.png)




### update_item_name
**Kegunaan:** mengubah nama sebuah item yang telah diinput ke daftar belanja.

**Input:** nama item lama yang akan diganti dan nama item baru sebagai pengganti.

![image](https://user-images.githubusercontent.com/59790033/205501198-1ad4c729-e4ea-4abc-b589-03e446f019d4.png)

**Mekanisme:** fungsi akan mengcopy dictionary dengan nama item lama kepada nama item baru, lalu menghapus dictionary dengan nama item lama. Akhirnya, fungsi menampilkan seluruh item dalam transaksi.

![image](https://user-images.githubusercontent.com/59790033/205501308-8d9eb39a-a6ed-4c9f-9530-a348e3c1ef96.png)



### update_item_qty
**Kegunaan:** mengubah kuantitas atau jumlah sebuah item yang telah diinput ke daftar belanja.

**Input:** nama item target yang mau diupdate dan jumlah item baru sebagai pengganti.

![image](https://user-images.githubusercontent.com/59790033/205501445-2968c017-c6fe-4cf2-817d-9c0911497279.png)

**Mekanisme:** Fungsi akan mengupdate jumlah item pada item dengan nama yang terinput.

![image](https://user-images.githubusercontent.com/59790033/205501540-51806533-3ef0-475f-8c3d-f7e93892d7f4.png)

### update_item_price
**Kegunaan:** mengubah harga sebuah item yang telah diinput ke daftar belanja.

**Input:** nama item target yang mau diupdate dan harga item baru sebagai pengganti.

![image](https://user-images.githubusercontent.com/59790033/205501631-2066d8e8-23cb-45db-b75d-3e3bdbc5cc18.png)

**Mekanisme:** Fungi akan mengupdate harga item pada item dengan nama yang terinput.

![image](https://user-images.githubusercontent.com/59790033/205501645-07a009ce-27b4-41be-9149-f699cec6c3d5.png)


### delete_item
**Kegunaan:** menghapus sebuah item yang telah diinput ke daftar belanja.

**Input:** nama item target yang mau dihapus.

![image](https://user-images.githubusercontent.com/59790033/205501690-66ebbe79-fd29-4c9d-8980-5e4e9785d9e2.png)

**Mekanisme:** Fungsi akan menghapus item dengan nama yang terinput.

![image](https://user-images.githubusercontent.com/59790033/205501726-7f230afe-2506-4c54-9287-49c29b082ce0.png)


### reset_transaction
**Kegunaan:** menghapus seluruh item yang telah diinput ke daftar belanja

**Input:** tidak ada.

![image](https://user-images.githubusercontent.com/59790033/205501822-832a0e7b-9d81-486e-8b5a-3efee8e4889b.png)

**Mekanisme:** Fungsi akan menghapus dictionary yang telah terbuat.

![image](https://user-images.githubusercontent.com/59790033/205501892-a7f5ac2a-1e62-4e4c-a344-1f39519ff67a.png)


### check_order
**Kegunaan:** mengecek apaka input item yang dilakukan pelanggan sudah benar dan menampilkan tabel belanja

**Input:** tidak ada.

![image](https://user-images.githubusercontent.com/59790033/205501954-a0991347-450c-4da0-991a-f1e32f21458c.png)

**Mekanisme:** Fungsi akan melakukan check input apakah sudah benar. Input harus lengkap (nama, jumlah, harga) dan tidak boleh berisi null/nan. Lalu data tersebut ditampilkan dengan pandas dataframe.

![image](https://user-images.githubusercontent.com/59790033/205502027-fe9c8d10-bef8-45d5-9534-17ac67f0b77b.png)


### total_price
**Kegunaan:** Menampilkan total keseluruhan biaya yang harus dibayarkan setelah diskon.
        Diskon 5% apabila total biaya diatas Rp 200.000
        Diskon 8% apabila total biaya diatas Rp 300.000
        Diskon 10% apabila total biaya diatas Rp 500.000

**input:** tidak ada.

**Mekanisme 1:** fungsi akan membuat dataframe dan menghitung total harga dengan mengalikan harga x jumlah item.

![image](https://user-images.githubusercontent.com/59790033/205502155-6394e7a0-2895-46c7-8c7f-04dfa4b48477.png)

**Mekanisme 2:** dari total harga yang didapat, fungsi menghitung diskon sesuai ketentuan. Lalu menampilkan hasil akhirnya.

![image](https://user-images.githubusercontent.com/59790033/205502223-b0b29762-08ab-4c97-808a-e3790d9863d7.png)


## Hasil Test
### Test 1

![image](https://user-images.githubusercontent.com/59790033/205502277-c84f209a-db37-4efd-ba76-513b325bef1f.png)


### Test 2

![image](https://user-images.githubusercontent.com/59790033/205502292-1c436bb4-6622-432c-880e-5f00e8a71429.png)

### Test 3

![image](https://user-images.githubusercontent.com/59790033/205502312-65997816-289a-448a-8040-97e494e5aa85.png)


### Test 4

![image](https://user-images.githubusercontent.com/59790033/205502328-e0f666fe-4032-4910-95c1-3f2e2e69f54a.png)


## Conclusions
- Seluruh requirement dari perusahaan telah dapat dijalankan dengan baik
- Kedepannya dapat menambahkan user interface agar lebih nyaman digunakan dalam display
- Kedepannya dapat ditambah fitur cek diskon & encourage message to spend more agar customer ter trigger belanja lebih banyak
- Penggunaan API dan stream real time database akan sangat baik apabila bisa digunakan

