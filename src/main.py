import argparse
import json
import os

# Import fungsi dari file algoritma dan cost function
from algorithm_greedy import solve_greedy
from algorithm_exact import solve_exact
from cost_function import calculate_tco

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, 'data', 'location.json'), 'r') as f:
        location = json.load(f)
    with open(os.path.join(base_dir, 'data', 'distance_matrix.json'), 'r') as f:
        distance_matrix = json.load(f)["matrix"]
    with open(os.path.join(base_dir, 'data', 'config.json'), 'r') as f:
        config = json.load(f)
    return location, distance_matrix, config

def main():
    parser = argparse.ArgumentParser(description="Last-Mile Delivery Route Simulator")
    parser.add_argument('--scenarios', type=str, choices=['subsidi', 'krisis'], required=True,
                        help="Pilih skenario harga BBM: subsidi atau krisis")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  LAST-MILE DELIVERY SIMULATOR - SKENARIO: {args.scenarios.upper()}  ")
    print(f"{'='*60}")

    location, distance_matrix, config = load_data()
    fuel_price = config["scenarios"][args.scenarios]["fuel_price_per_liter_idr"]
    
    print(f"Total lokasi dikunjungi : {len(location)} titik (1 Hub + {len(location)-1} Pelanggan)")
    print(f"Harga BBM saat ini      : Rp {fuel_price:,}/liter\n")

    # --- Eksekusi Algoritma ---
    # 1. Greedy
    g_route, g_dist, g_time = solve_greedy(distance_matrix)
    g_fuel, g_comp, g_tco = calculate_tco(g_route, distance_matrix, g_time, fuel_price, config)

    # 2. Exact (Backtracking)
    e_route, e_dist, e_time = solve_exact(distance_matrix, start=0)
    e_fuel, e_comp, e_tco = calculate_tco(e_route, distance_matrix, e_time, fuel_price, config)

    # --- Tampilkan Hasil Rute ---
    print("[ DETAIL RUTE ]")
    print(f"Greedy       : {' -> '.join(map(str, g_route))}")
    print(f"Backtracking : {' -> '.join(map(str, e_route))}\n")

    # --- Tampilkan Tabel Komparasi ---
    print("[ KOMPARASI PERFORMA & BIAYA (TCO) ]")
    print(f"{'-'*60}")
    print(f"{'Metrik':<20} | {'Greedy (Heuristik)':<16} | {'Eksak (Backtracking)':<18}")
    print(f"{'-'*60}")
    print(f"{'Total Jarak':<20} | {g_dist:>13.2f} km | {e_dist:>15.2f} km")
    print(f"{'Waktu Eksekusi':<20} | {g_time:>13.4f} ms | {e_time:>15.4f} ms")
    print(f"{'-'*60}")
    print(f"{'Biaya BBM':<20} | Rp {g_fuel:>10,.2f} | Rp {e_fuel:>12,.2f}")
    print(f"{'Biaya Komputasi':<20} | Rp {g_comp:>10,.2f} | Rp {e_comp:>12,.2f}")
    print(f"{'-'*60}")
    print(f"{'TOTAL TCO':<20} | Rp {g_tco:>10,.2f} | Rp {e_tco:>12,.2f}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()