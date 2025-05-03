class Node:
    def __init__(self, data1 = None, next1 = None):
        self.data = data1
        self.next = next1
    
    def create_ll_from_list(self, arr):
        head = Node(arr[0])
        mover = head
        for i in range(1, len(arr)):
            next_node = Node(arr[i])
            mover.next = next_node
            mover = next_node
        
        return head


    def print_linked_list(self, head):
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def delete_a_node(self, node):
        node.data = node.next.data
        node.next = node.next.next

obj = Node()
head = obj.create_ll_from_list([1,2,3,4])
obj.print_linked_list(head)
