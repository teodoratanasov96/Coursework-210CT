from collections import defaultdict # used for the dictionary

class Graph:
  """this class is used to generate the weighted grapth with nodes, edges and distances"""
  def __init__(self):
    self.nodes = set() # set so the nodes are unique
    self.edges = defaultdict(list) # weight
    self.distance = {} #distance

  def add_node(self, value):
    """function to add nodes to the grapth"""
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    """used to add edges to the graph"""
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distance[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  """This function performs dijstra's algorthin the graph"""
  visited = {initial: 0} #
  path = {}

  nodes = set(graph.nodes)

  while nodes: # goes through all the nodes
    min_node = None
    for node in nodes:
      if node in visited: # check if the node has been visited
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None: # skip if no nodes
      break

    nodes.remove(min_node) # remove nodes that have all ready been processed
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]: # itterate thorugh the edges
        weight = current_weight + graph.distance[(min_node, edge)]
        print(weight, "min_node", min_node, "edge:", edge) # Used in debuging
        if edge not in visited or weight < visited[edge]: # if more efficent add route to paths
          visited[edge] = weight
          path[edge] = min_node

  return visited, path

##Below is creating the graph and its weight etc
g = Graph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')

g.add_edge('a', 'b', 10)
g.add_edge('b', 'a', 10)
g.add_edge('b', 'c', 10)
g.add_edge('c', 'b', 10)
g.add_edge('a', 'c', 15)
g.add_edge('c', 'a', 15)
g.add_edge('c', 'd', 20)
g.add_edge('d', 'c', 20)

print(dijsktra(g, 'a'))
