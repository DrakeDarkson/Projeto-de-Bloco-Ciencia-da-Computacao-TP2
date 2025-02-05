import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


def main():
    start_time = time.time()
    
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.display()
    linked_list.delete_node(20)
    linked_list.display()
    
    end_time = time.time()
    print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
