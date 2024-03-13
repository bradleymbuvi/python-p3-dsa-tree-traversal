class Tree:
  
	def __init__(self, root = None):
		self.root = root

	def get_element_by_id(self, id):
		      result = None
		      nodes_to_search = [self.root]
		      while len(nodes_to_search) != 0:
			            node = nodes_to_search.pop(0)
			            if node['id'] == id:
				                  result = node
			            else:
				                  nodes_to_search = nodes_to_search + node['children']
		return result

  def get_element_by_id(self, id):
    pass