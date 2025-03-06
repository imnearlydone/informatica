def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
        print(curr_node)
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    print(curr_node)
    return visited