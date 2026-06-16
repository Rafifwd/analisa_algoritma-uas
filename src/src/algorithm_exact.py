import time


def exact_route(distance_matrix):
    """
    Mencari rute optimal menggunakan DFS Backtracking + Pruning.

    Parameters:
        distance_matrix (list[list[float]]):
            Matriks jarak antar titik.

    Returns:
        dict:
        {
            "route": [...],
            "distance": float,
            "execution_time_ms": float
        }
    """

    n = len(distance_matrix)

    best_distance = float("inf")
    best_route = []

    start_time = time.perf_counter()

    def dfs(current_node, visited, current_distance, current_route):
        nonlocal best_distance, best_route

        # Pruning
        if current_distance >= best_distance:
            return

        # Semua node sudah dikunjungi
        if len(visited) == n:
            total_distance = (
                current_distance +
                distance_matrix[current_node][0]
            )

            if total_distance < best_distance:
                best_distance = total_distance
                best_route = current_route + [0]

            return

        # Coba semua node yang belum dikunjungi
        for next_node in range(1, n):
            if next_node not in visited:
                dfs(
                    next_node,
                    visited | {next_node},
                    current_distance +
                    distance_matrix[current_node][next_node],
                    current_route + [next_node]
                )

    # Mulai dari Hub (node 0)
    dfs(
        current_node=0,
        visited={0},
        current_distance=0,
        current_route=[0]
    )

    end_time = time.perf_counter()

    execution_time_ms = (end_time - start_time) * 1000

    return {
        "route": best_route,
        "distance": round(best_distance, 2),
        "execution_time_ms": round(execution_time_ms, 3)
    }


# Testing sederhana
if __name__ == "__main__":

    distance_matrix = [
        [0, 5, 7, 4],
        [5, 0, 2, 8],
        [7, 2, 0, 3],
        [4, 8, 3, 0]
    ]

    result = exact_route(distance_matrix)

    print("=== Exact Route (Backtracking + Pruning) ===")
    print("Route :", result["route"])
    print("Distance :", result["distance"])
    print("Execution Time (ms) :", result["execution_time_ms"])