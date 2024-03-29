
# Contains topological ordering.

def dfs_loop(graph):
    v = list(graph.keys())
    n = len(v)
    path= []
    # We have to use mutable object like list to store the current number.
    curr = [n]
    ordering = dict(zip(v, [n]*n))
    visited = dict(zip(v, [False]*n))
    for vi in v:
        if not visited[vi]:
            dfs(graph, vi, visited, path, curr, ordering)
    return path


def dfs(graph, start, visited, path, curr, ordering):
    visited[start] = True
    for w in graph[start]:
        print(start, w, visited[w])
        if not visited[w]:
            visited[w] = True
            path.append([start, w])
            print('After checking:', start, w)
            dfs(graph, w, visited, path, curr, ordering)
    ordering[start] = curr[0]
    # Use slicing operation
    curr[0] = curr[0] - 1
    print('######## Topological Ordering:', ordering)




if __name__ == '__main__':
    testcase1 = {'A': ('B', 'E'),
                 'B': ('A', 'C', 'D', 'F'),
                 'C': ('B', 'G', 'D'),
                 'D': ('B', 'C', 'G'),
                 'E': 'A',
                 'F': ('G', 'B'),
                 'G': ('C', 'D', 'F')}

    testcase2 = {'A': ('B', 'C'),
                 'B': 'D',
                 'C': 'D',
                 'D': ()}

    result = dfs_loop(testcase1)
    print('\nThe Path:', result)
