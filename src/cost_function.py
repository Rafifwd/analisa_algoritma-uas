def calculate_dynamic_fuel_ratio(current_load_kg, max_load_kg, ratio_full, ratio_empty):
    """
    Menghitung rasio konsumsi BBM (liter/km) menggunakan interpolasi linear 
    berdasarkan persentase beban paket yang dibawa motor.
    """
    persentase_beban = current_load_kg / max_load_kg
    selisih_rasio = ratio_full - ratio_empty
    
    current_ratio = ratio_empty + (persentase_beban * selisih_rasio)
    return current_ratio

def calculate_segment_fuel_cost(distance_km, current_ratio, fuel_price):
    """
    Menghitung biaya BBM untuk satu segmen perjalanan antar titik.
    """
    return distance_km * current_ratio * fuel_price

def calculate_cloud_cost(execution_time_ms, rate_per_ms):
    """
    Menghitung biaya sewa server cloud berdasarkan waktu eksekusi algoritma.
    """
    return execution_time_ms * rate_per_ms

def calculate_tco(total_fuel_cost, total_cloud_cost):
    """
    Menghitung Total Cost of Ownership (TCO).
    """
    return total_fuel_cost + total_cloud_cost