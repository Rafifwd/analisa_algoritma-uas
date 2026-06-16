import argparse
import json
import os

def load_data():
    # Asumsi file main.py ada di dalam src/ dan JSON ada di data/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    with open(os.path.join(base_dir, 'data', 'location.json'), 'r') as f:
        location = json.load(f)
    with open(os.path.join(base_dir, 'data', 'distance_matrx.json'), 'r') as f:
        distance_matrx = json.load(f)
    with open(os.path.join(base_dir, 'data', 'config.json'), 'r') as f:
        config = json.load(f)
        
    return location, distance_matrx, config

def main():
    # Setup CLI Argument Parser
    parser = argparse.ArgumentParser(description="Last-Mile Delivery Route Simulator")
    parser.add_argument('--scenario', type=str, choices=['subsidi', 'krisis'], required=True,
                        help="Pilih skenario harga BBM: subsidi atau krisis")
    args = parser.parse_args()

    print(f"--- Memulai Simulasi Skenario: {args.scenario.upper()} ---")

    # Load Data dari Anggota 1
    print("Memuat data konfigurasi...")
    location, distance_matrx, config = load_data()
    print(f"Data berhasil dimuat. Total lokasi: {len(location)}")

    # TODO: Panggil Algoritma Greedy (Anggota 2) di sini nanti
    print("\n[Placeholder] Menjalankan Algoritma Heuristik (Greedy)...")
    
    # TODO: Panggil Algoritma Exact / Backtracking (Anggota 3) di sini nanti
    print("[Placeholder] Menjalankan Algoritma Eksak (Backtracking)...")

    # TODO: Hitung TCO dan cetak tabel komparasi output di sini nanti
    print("\n[Placeholder] Menampilkan hasil TCO dan perbandingan rute...")

if __name__ == "__main__":
    main()