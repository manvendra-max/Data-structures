class Node():
    def __init__(self, node_data=None, next_node = None, prev_node = None):
        self.data = node_data
        self.next = next_node
        self.previous_node = prev_node

    
def create_dl_from_list(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], prev_node=prev)
        prev.next = temp
        prev = temp
    
    return head

def print_list(head):
    temp = head
    while (temp):
        print(temp.data, end=' ')
        temp = temp.next
    
def insert_at_the_end(head, data):
    new_node = Node(data)

    if head == None:
        return new_node
    
    tail = head
    while (tail.next):
        tail = tail.next
    
    new_node.previous_node = tail
    tail.next = new_node

    return head
    


head = create_dl_from_list([1,2,3,4])
print_list(head)

print("inserting into dl")

insert_at_the_end(head, 5)

print_list(head)
        

    
