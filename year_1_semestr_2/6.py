def Ford_Bellman(curr_node, adj_list):
    dist = ["inf" for i in range(len(adj_list))]
    dist[curr_node] = 0
    for i in range(len(adj_list) - 1):
        #Уже не соображаю, что делать. Если будет можно, потом попробую доделать.