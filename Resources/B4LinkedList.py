class LinkedList:
    #constructor
    def __init__(self):
        self.head = None
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_location(self, location, data):
        current = self.head
        for i in range(location-1):
            current = current.next
            #failsafe if list isn't that long
            if current == None:
                print("List not long enough")
                return
        new_node = Node(data) #create new node with data
        new_node.next = current.next #set new node to the same
        #pointer as the found node
        current.next = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        #edge case if list is empty
        if self.head is None:
            self.head = new_node
        else:
            current = self.head #link to start of list
            while current.next != None: #moving down the list
                current = current.next
        #when the loop ends, the next pointer must be none, which is default
        current.next = new_node

    def delete_node(self, data):
        current = self.head
        prev = None

        #case 1, the node is the head of the list
        if current != None and current.data == data:
            self.head = current.next
            current = None
            return

        #searching for node
        while current != None and current.data != data:
            prev = current
            current = current.next

        #case 3 - node not found
        if current == None:
            print("Node with data ", str(data), " not found.")

        #case 2 - unlink node from list
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        return False


class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None

l = LinkedList()
l.insert_at_beginning(15)
l.insert_at_end("toe")
l.insert_at_location(1, True)
l.print_list()