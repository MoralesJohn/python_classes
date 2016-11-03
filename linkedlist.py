# node class
class Node(object):
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

# linked list class
class Doubly_linked(object):
	def __init__(self):
		self.head = None
		self.tail = None

	# adding a node to an empty array
	def add_empty(self, node):
		self.head = node
		self.tail = node
		return self

	# popAt is really just a delete
	def popNodeAt(self, node):
		node.next.prev = node.prev
		node.prev.next = node.next
		data = node.data
		node.next = None
		node.prev = None
		node = None
		return data

	def insertBefore(self, ref, data):
		node = Node(data)
		ref.prev.next = node
		node.prev = ref.prev
		ref.prev = node
		node.next = ref
		return self

	def insertAfter(self, ref, data):
		node = Node(data)
		ref.next.prev = node
		node.next = ref.next
		ref.next = node
		node.prev = ref
		return self

	def pushNode(self, data):
		node = Node(data)
		if self.head == None:
			ll.add_empty(node)
		else:
			node.prev = self.tail
			node.prev.next = node
			self.tail = node
		return self

	def popNode(self):
		node = self.tail
		self.tail = node.prev
		self.tail.next = None
		node.prev = None
		data = node.data
		node = None
		return data

	def displayList(self):
		if self.head != None:
			node = self.head
			print node.data, 
			while node.next != None:
				node = node.next
				print node.data,
			print ""

# declare a linked list
ll = Doubly_linked()

# populate and print it
ll.pushNode("random_string")
ll.pushNode("3030")
ll.pushNode("a")
ll.pushNode(19)
ll.pushNode("Zoo")
ll.displayList()

# try an insertAfter
ll.insertAfter(ll.head, "inserta")
ll.displayList()

# try a pop, and an insertBefore
print ll.popNode()
ll.insertBefore(ll.tail, "insertb")

# finally, a delete, or popAt
print ll.popNodeAt(ll.head.next.next)

ll.displayList()