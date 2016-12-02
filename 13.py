CLASS graph
   FUNCTION initilization
      NODE = {}
      edgeKey = {}
      edgeNode = {}
      edgeKey X edgeNode = edges
      distance = ∅

    
   FUNCTION addNode(value)
      node = value
   FUNCTION add_edge(from_NODE, to_NODE, distance)
      from_NODE = from
      to_NODE = to
      weight = distance

def add_node(self, value):
    self.nodes.add(value)

def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distance[(from_node, to_node)] = distance




