from collections import defaultdict

graph = {\
            'Arad': {'Sibiu', 'Zerind', 'Timisoara'},\
            'Zerind': {'Arad', 'Oradea'},\
            'Oradea': {'Zerind', 'Sibiu'},\
            'Sibiu': {'Arad', 'Oradea', 'Faragas', 'Rimnicu'},\
            'Timisoara': {'Arad', 'Lugoj'},\
            'Lugoj': {'Timisoara', 'Mehadia'},\
            'Mehadia': {'Lugoj', 'Dobreta'},\
            'Dobreta': {'Mehadia', 'Craiova'},\
            'Craiova': {'Dobreta', 'Rimnicu', 'Pitesti'},\
            'Rimnicu': {'Sibiu', 'Craiova', 'Pitesti'},\
            'Faragas': {'Sibiu', 'Bucharest'},\
            'Pitesti': {'Rimnicu', 'Craiova', 'Bucharest'},\
            'Bucharest': {'Faragas', 'Pitesti', 'Giurgiu', 'Urziceni'},\
            'Giurgiu': {'Bucharest'},\
            'Urziceni': {'Bucharest', 'Vaslui', 'Hirsova'},\
            'Hirsova': {'Urziceni', 'Eforie'},\
            'Eforie': {'Hirsova'},\
            'Vaslui': {'Iasi', 'Urziceni'},\
            'Iasi': {'Vaslui', 'Neamt'},\
            'Neamt': {'Iasi'}\
        }

def print_all_util(graph,s,d,visited,path):
    visited[s]=True
    path.append(s)
    if s==d:
        print path
    else:
        for i in graph[s]:
            if visited[i]==False:
                print_all_util(graph,i,d,visited,path)
    path.pop()
    visited[s]=False



def print_all(graph,s,d):
    visited={}
    visited = defaultdict(lambda:False,visited)
    path = []
    print_all_util(graph,s,d,visited,path)

print_all(graph,'Arad','Bucharest')
#print(graph.keys())

