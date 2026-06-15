# Simulasi Rute Pengiriman Last-Mile: Analisis Komparatif Algoritma Greedy vs. DFS Backtracking

Proyek ini adalah sistem simulasi untuk membandingkan rute pengiriman *last-mile* menggunakan dua pendekatan algoritma: **Greedy Nearest Neighbor** (heuristik) dan **Depth-First Search (DFS) Backtracking dengan Pruning** (eksak). Simulasi ini bertujuan membantu pengambil keputusan bisnis dalam menentukan rute yang meminimalkan *Total Cost of Ownership* (TCO) berdasarkan variasi skenario harga bahan bakar minyak (BBM).

Sistem membaca data input dari tiga file JSON eksternal:
- `locations.json`: Menyimpan data koordinat atau informasi lokasi pengiriman.
- `distance_matrix.json`: Menyimpan matriks jarak antar-lokasi.
- `config.json`: Menyimpan konfigurasi parameter sistem seperti efisiensi kendaraan dan biaya komputasi.

Output program disajikan langsung di terminal CLI berupa tabel komparasi TCO yang komprehensif untuk memudahkan analisis.

---

## 1. CARA MENJALANKAN PROGRAM

Ikuti langkah-langkah di bawah ini untuk mengkloning repositori, menyiapkan file konfigurasi, dan menjalankan simulasi di komputer lokal Anda:

### Langkah 1: Kloning Repositori
Kloning proyek ini dari repositori Git menggunakan perintah berikut:
```bash
git clone https://github.com/Rafifwd/analisa_algoritma-uas.git
cd analisa_algoritma-uas
```

### Langkah 2: Persiapkan File Data (JSON)
Pastikan berkas-berkas data berikut telah terkonfigurasi dengan benar di dalam direktori `data/`:
*   `data/location.json` (menyimpan koordinat lokasi titik pengiriman)
*   `data/distance_matrx.json` (menyimpan matriks jarak antar titik lokasi)
*   `data/config.json` (menyimpan konfigurasi kendaraan dan biaya dasar komputasi)

### Langkah 3: Eksekusi Program
Proyek ini sepenuhnya ditulis menggunakan modul bawaan (*standard library*) Python. Anda **tidak membutuhkan dependensi eksternal** (tidak perlu melakukan `pip install`). Cukup jalankan perintah CLI berikut sesuai dengan skenario ekonomi yang ingin disimulasikan:

*   **Menjalankan Skenario BBM Subsidi (Rp 5.000 / liter):**
    ```bash
    python src/main.py --scenario subsidi
    ```

*   **Menjalankan Skenario BBM Krisis (Rp 20.000 / liter):**
    ```bash
    python src/main.py --scenario krisis
    ```

---

## 2. PEMILIHAN ALGORITMA

Dalam memecahkan masalah pencarian rute terpendek (*Traveling Salesperson Problem* / TSP pada *last-mile delivery*), sistem ini menyediakan dua pilihan pendekatan dengan trade-off yang berbeda:

### A. Greedy Nearest Neighbor (Heuristik)
*   **Cara Kerja**: Algoritma selalu memilih lokasi terdekat berikutnya dari lokasi saat ini yang belum pernah dikunjungi.
*   **Kelebihan**: Sangat cepat karena hanya melakukan evaluasi lokal di setiap langkah. Mampu menangani ribuan lokasi ($n > 1000$) dalam hitungan milidetik.
*   **Kekurangan**: Tidak menjamin rute yang dihasilkan adalah rute terpendek global. Algoritma rentan menghasilkan keputusan yang buruk di akhir rute (efek *myopic* atau pandangan sempit).

### B. DFS Backtracking dengan Pruning (Eksak)
*   **Cara Kerja**: Menjelajahi seluruh kemungkinan permutasi rute pengiriman secara rekursif (DFS). Dilengkapi dengan teknik *pruning* (pemangkasan cabang): jika jarak rute parsial yang sedang diperiksa sudah melebihi jarak rute terbaik yang telah ditemukan sebelumnya, pencarian di cabang tersebut dihentikan seketika.
*   **Kelebihan**: Menjamin rute yang ditemukan adalah rute yang benar-benar optimal secara global (jarak terpendek mutlak).
*   **Kekurangan**: Membutuhkan waktu eksekusi yang sangat lama seiring bertambahnya jumlah lokasi karena pertumbuhan kompleksitas yang bersifat faktorial.

### Panduan Kesesuaian Penggunaan
*   **Gunakan Greedy Nearest Neighbor** jika jumlah titik pengiriman ($n$) cukup besar ($n > 12$) atau saat rute harus ditentukan dengan cepat di perangkat berdaya komputasi rendah.
*   **Gunakan DFS Backtracking dengan Pruning** jika jumlah titik pengiriman relatif sedikit ($n \le 12$) dan penghematan biaya bahan bakar bernilai tinggi bagi operasional perusahaan, sehingga komparasi rute eksak yang presisi dapat menjustifikasi waktu pemrosesan CPU.

---

## 3. ANALISIS KOMPLEKSITAS BIG-O

Secara teoritis, perbandingan ruang (memori) dan waktu (komputasi) dari kedua algoritma dapat dijabarkan sebagai berikut:

### Tabel Perbandingan Kompleksitas
| Algoritma | Kompleksitas Waktu (Time) | Kompleksitas Ruang (Space) | Sifat Solusi |
| :--- | :--- | :--- | :--- |
| **Greedy Nearest Neighbor** | $O(n^2)$ | $O(n)$ | Heuristik (Sub-optimal) |
| **DFS Backtracking + Pruning** | $O(n!)$ *(Worst Case)* | $O(n)$ | Eksak (Optimal Mutlak) |

### Analisis Detail

1.  **Greedy Nearest Neighbor**:
    *   **Waktu ($O(n^2)$)**: Dari titik awal, algoritma memindai seluruh $n-1$ lokasi lainnya untuk mencari titik terdekat. Pada titik berikutnya, ia memindai $n-2$ titik yang tersisa, dan seterusnya. Total iterasi yang terjadi adalah $\sum_{i=1}^{n} (n - i) = \frac{n(n-1)}{2}$, yang secara dominan disederhanakan menjadi $O(n^2)$ akibat nested loop pencarian titik terdekat.
    *   **Ruang ($O(n)$)**: Hanya memerlukan ruang memori linier untuk menyimpan array penanda titik yang telah dikunjungi (*visited array*) berukuran $n$ serta array urutan rute akhir yang juga berukuran $n$.

2.  **DFS Backtracking dengan Pruning**:
    *   **Waktu ($O(n!)$)**: Dalam skenario terburuk (*worst case*), algoritma harus memeriksa semua kombinasi rute yang mungkin, yaitu sebanyak $n!$ permutasi. Meskipun teknik *pruning* (pemangkasan) berhasil memotong banyak cabang pencarian secara signifikan pada kasus rata-rata (*average case*), batas atas teoritisnya tetap berada pada tingkat faktorial $O(n!)$.
    *   **Ruang ($O(n)$)**: Penggunaan memori dibatasi oleh kedalaman tumpukan pemanggilan rekursif (*recursion call stack*) yang mencapai maksimum $n$ tingkat (sama dengan jumlah lokasi yang dikunjungi), sehingga ruang memori yang dibutuhkan tetap berada pada tingkat linier $O(n)$.

---

## 4. SUMMARY KEPUTUSAN BISNIS

Pemilihan algoritma rute pengiriman harus mempertimbangkan keseimbangan biaya operasional armada (biaya BBM) dan biaya infrastruktur teknologi (biaya komputasi). Berikut adalah analisis rekomendasi keputusan bisnis untuk masing-masing skenario:

*   **Skenario BBM Subsidi (BBM Murah - Rp 5.000 / liter)**:
    Pada skenario ini, harga bahan bakar relatif rendah. Selisih penghematan jarak yang dihasilkan oleh algoritma eksak tidak berdampak signifikan terhadap penghematan biaya bahan bakar dalam nilai rupiah. Di sisi lain, biaya sewa server komputasi atau waktu tunggu pengerjaan komputasi eksak yang besar justru berpotensi melebihi nilai penghematan BBM tersebut. Oleh karena itu, **algoritma Greedy Nearest Neighbor direkomendasikan** karena memberikan efisiensi waktu operasional instan dengan biaya komputasi yang dapat diabaikan.
    
*   **Skenario BBM Krisis (BBM Mahal - Rp 20.000 / liter)**:
    Ketika harga bahan bakar melonjak tinggi, setiap kilometer rute yang berhasil dipangkas memiliki nilai ekonomis yang sangat tinggi bagi perusahaan. Selisih penghematan jarak dari rute optimal eksak akan menghasilkan penghematan biaya BBM yang signifikan secara akumulatif. Oleh karena itu, selama jumlah titik tujuan berada dalam rentang wajar ($n \le 12$), **algoritma DFS Backtracking dengan Pruning sangat direkomendasikan** untuk memangkas pengeluaran BBM operasional secara signifikan.

### Analisis Titik Break-Even ($P^*$)

Titik *break-even* ($P^*$) merupakan harga bahan bakar per liter di mana biaya komparasi total (TCO) kedua algoritma bernilai sama. Jika harga BBM di pasar berada di atas nilai $P^*$, maka algoritma Eksak menjadi pilihan yang lebih hemat biaya dibanding Greedy.

Persamaan Total Cost of Ownership (TCO):
$$\text{TCO}_A = (D_A \times F \times P) + C_{\text{komputasi}, A}$$

Di mana:
*   $D_A$ = Total jarak rute algoritma $A$ (km)
*   $F$ = Konsumsi bahan bakar rata-rata kendaraan (liter/km)
*   $P$ = Harga bahan bakar per liter (Rp/liter)
*   $C_{\text{komputasi}, A}$ = Biaya operasional komputasi algoritma $A$ (Rp)

Titik keseimbangan tercapai ketika $\text{TCO}_{\text{Eksak}} = \text{TCO}_{\text{Greedy}}$:
$$(D_E \times F \times P^*) + C_{\text{komputasi}, E} = (D_G \times F \times P^*) + C_{\text{komputasi}, G}$$

Melalui penyederhanaan aljabar, kita mendapatkan formula harga BBM *break-even* ($P^*$):
$$P^* = \frac{C_{\text{komputasi}, E} - C_{\text{komputasi}, G}}{(D_G - D_E) \times F} = \frac{\Delta C_{\text{komputasi}}}{\Delta D \times F}$$

#### Contoh Simulasi Numerik:
*   **Efisiensi Armada ($F$)**: $0,1\text{ liter/km}$ (atau $10\text{ km/liter}$).
*   **Penghematan Jarak ($\Delta D$)**: $D_G - D_E = 150\text{ km} - 130\text{ km} = 20\text{ km}$.
*   **Selisih Biaya Komputasi ($\Delta C_{\text{komputasi}}$)**: Diasumsikan biaya penggunaan unit CPU server cloud adalah Rp 150/detik.
    *   Waktu Greedy ($t_G$) = $0,001\text{ detik} \implies C_{\text{komputasi}, G} \approx \text{Rp } 0$
    *   Waktu Eksak ($t_E$) = $10\text{ detik} \implies C_{\text{komputasi}, E} = 10 \times \text{Rp } 150 = \text{Rp } 1.500$
    *   $\Delta C_{\text{komputasi}} = \text{Rp } 1.500$

Menghitung $P^*$:
$$P^* = \frac{\text{Rp } 1.500}{20\text{ km} \times 0,1\text{ liter/km}} = \frac{1.500}{2\text{ liter}} = \text{Rp } 750\text{ / liter}$$

**Interpretasi Hasil**:
*   Jika harga BBM **di atas Rp 750/liter** (seperti skenario subsidi Rp 5.000 maupun krisis Rp 20.000), penghematan jarak dari rute optimal **Eksak** sudah mampu menutupi biaya komputasi server. Sehingga algoritma Eksak lebih menguntungkan untuk skala kecil ($n \le 12$).
*   Namun, jika jumlah lokasi ($n$) terus bertambah, biaya komputasi algoritma eksak ($\Delta C_{\text{komputasi}}$) akan melesat naik secara eksponensial/faktorial. Hal ini akan menaikkan nilai $P^*$ secara drastis hingga melampaui harga pasar BBM krisis, menggeser kembali rekomendasi terbaik ke algoritma **Greedy**.