class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

def deep_copy(head_node):
    if head_node is None:
        return None
    node = Node(head_node.val)
    node.next_node = deep_copy(head_node.next_node)
    return node
    
m1 = Node("A")
m2 = Node("B")
m3 = Node("C")
m4 = Node("D")
m5 = Node("E")
m6 = Node("F")


m1.set_next_node(m2)
m2.set_next_node(m3)

print("List 1")
list1 = Singly_linked_list(m1)
list1.list_traversed()

m4.set_next_node(m5)
m5.set_next_node(m6)

print("")
print("List 2")
list2 = Singly_linked_list(m4)
list2.list_traversed()

list2=deep_copy(list1.head_node)
list2 = Singly_linked_list(list2)
print("New List 2")
list2.list_traversed()
