import time

def solve_exact(distance_matrix, start=0):
    n = len(distance_matrix)
    customers = [i for i in range(n) if i != start]

    best = {
        "route": None,
        "distance": float("inf")
    }

    def dfs(current_node, visited, current_route, current_distance):
        if len(visited) == len(customers):
            total = current_distance + distance_matrix[current_node][start]
            if total < best["distance"]:
                best["distance"] = total
                best["route"] = current_route + [start]
            return

        for next_node in customers:
            if next_node in visited:
                continue
            next_distance = current_distance + distance_matrix[current_node][next_node]
            if next_distance >= best["distance"]:
                continue
            dfs(next_node, visited | {next_node}, current_route + [next_node], next_distance)

    start_time = time.perf_counter()
    dfs(start, set(), [start], 0)
    end_time = time.perf_counter()

    exec_time_ms = (end_time - start_time) * 1000
    return best["route"], best["distance"], exec_time_ms