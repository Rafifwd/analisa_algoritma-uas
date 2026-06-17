def calculate_dynamic_fuel_ratio(current_load_kg, max_load_kg, ratio_full, ratio_empty):
    persentase_beban = max(0.0, min(1.0, current_load_kg / max_load_kg))
    selisih_rasio = ratio_full - ratio_empty
    return ratio_empty + (persentase_beban * selisih_rasio)

def calculate_segment_fuel_cost(distance_km, current_ratio, fuel_price):
    return distance_km * current_ratio * fuel_price

def calculate_cloud_cost(execution_time_ms, rate_per_ms):
    return execution_time_ms * rate_per_ms

# --- Fungsi Jembatan untuk dipanggil oleh main.py ---
def calculate_tco(route, distance_matrix, execution_time_ms, fuel_price, config):
    # Ekstrak konfigurasi
    max_load = config["vehicle"]["max_load_kg"]
    ratio_full = config["vehicle"]["fuel_ratio_full_liter_per_km"]
    ratio_empty = config["vehicle"]["fuel_ratio_empty_liter_per_km"]
    rate_per_ms = config["cloud_cost"]["rate_idr_per_ms"]
    weights = config["packages"]["weight_kg"]

    # 1. Hitung total beban di awal (sebelum berangkat dari Hub)
    # Asumsi Hub (index 0) tidak memiliki berat paket, hanya menghitung pesanan pelanggan
    current_load = sum(weights[node] for node in route if node != 0)

    total_fuel_cost = 0.0

    # 2. Iterasi perjalanan per segmen di dalam rute
    for i in range(len(route) - 1):
        start_node = route[i]
        end_node = route[i+1]
        dist = distance_matrix[start_node][end_node]
        
        # Hitung rasio BBM dinamis berdasarkan beban saat ini
        current_ratio = calculate_dynamic_fuel_ratio(current_load, max_load, ratio_full, ratio_empty)
        
        # Hitung biaya bensin di segmen ini
        segment_fuel = calculate_segment_fuel_cost(dist, current_ratio, fuel_price)
        total_fuel_cost += segment_fuel
        
        # Turunkan beban paket karena sudah diantar ke end_node
        current_load -= weights[end_node]

    # 3. Hitung biaya komputasi cloud
    total_cloud_cost = calculate_cloud_cost(execution_time_ms, rate_per_ms)

    # 4. Total TCO
    tco = total_fuel_cost + total_cloud_cost

    return total_fuel_cost, total_cloud_cost, tco