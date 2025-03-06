def BFS(start_node, adj_list, visited=None):
    queue = [(start_node, 0)]
    if visited is None:
        visited = set()
    while len(queue) > 0:
        curr_node, dist = queue.pop(0)
        visited.add(curr_node)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
    return visited
def comp_count(adj_list):
    nodes = [i for i in range(len(adj_list))]
    visited = set()
    k = 0
    while len(visited) != len(nodes):
        if visited != BFS(k, adj_list):
            k += 1
            visited += BFS(k, adj_list)
    return k


