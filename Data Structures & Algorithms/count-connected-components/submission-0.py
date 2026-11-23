def dfs(node, adj_list, visited): # takes the node being visited, adj_list of the graphs, and a list to track whether a node as been visited
# for each neighbor of node
#       if neighbour has not been visited
#           visit neighbour
#        recursively call dfs on neighbour
    visited[node] = True # marks the curr node as visited
    for neighbour in adj_list[node]: # loops through all the neighbours of the current node from the adjacency list
        if not visited[neighbour]: #checks if a neighbour hasnt been visited
            dfs(neighbour, adj_list, visited) #if not visited, rec calls dfs to visit all reachable nodes from here


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = []
        visited = [False] * n



        for i in range(n):
            adj_list.append([]) # empty list for each node in the graph

        for (u, v) in edges: # loops through each edge in the edges list
            # populate adjaceny list
            adj_list[u].append(v) #adds a connection to the adjecntcy list for both nodes
            adj_list[v].append(u) # since the graph is undirected, u and v add eachother as neighbors

        num_components = 0 # counter will count hoe many connected components in the graph 

        for node in range(n): #loops through nodes 0 - n-1
            # call dfs on node if it os not visited
            # and add 1 to num_components. 

            if not visited[node]: # if the current node has not been visited
                dfs(node, adj_list, visited) # starts the search fir this node
                num_components += 1 # after the search, one connected component has been visited so, incrememt

        return num_components # total number of connected components



