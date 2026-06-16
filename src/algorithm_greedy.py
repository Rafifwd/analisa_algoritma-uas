import time

def run_greedy_tsp(distance_matrix):
    """
    Algoritma Greedy Nearest Neighbor dari scratch.
    Dimulai dari Hub (index 0), mencari titik terdekat yang belum dikunjungi secara iteratif.
    """
    start_time = time.perf_counter()  # Mulai mencatat waktu komputasi
    
    num_nodes = len(distance_matrix)
    visited = [False] * num_nodes
    route = [0]  # Rute selalu dimulai dari Hub (index 0)
    visited[0] = True
    total_distance = 0.0
    
    current_node = 0
    
    # Iterasi untuk mengunjungi semua lokasi pelanggan (num_nodes - 1)
    for _ in range(num_nodes - 1):
        nearest_neighbor = -1
        shortest_distance = float('inf')
        
        # Periksa jarak ke semua titik lain dari titik saat ini
        for next_node in range(num_nodes):
            if not visited[next_node]:
                dist = distance_matrix[current_node][next_node]
                # Jika jarak lebih pendek, perbarui kandidat terdekat
                if dist < shortest_distance:
                    shortest_distance = dist
                    nearest_neighbor = next_node
        
        # Pindah ke pelanggan terdekat yang ditemukan
        route.append(nearest_neighbor)
        total_distance += shortest_distance
        visited[nearest_neighbor] = True
        current_node = nearest_neighbor
        
    # Kurir harus kembali ke Hub setelah paket terakhir diantar
    return_distance = distance_matrix[current_node][0]
    route.append(0)
    total_distance += return_distance
    
    end_time = time.perf_counter()  # Selesai mencatat waktu
    execution_time_ms = (end_time - start_time) * 1000  # Konversi ke milidetik
    
    return route, total_distance, execution_time_ms