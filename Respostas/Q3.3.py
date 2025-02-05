import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")

def main():
    start_time = time.time()
    ll = LinkedList()
    for i in range(10):
        ll.insert_at_end(i)
    
    print("Lista Original:")
    ll.display()
    
    print("Posição do valor 5:", ll.search(5))
    
    ll.reverse()
    print("Lista Invertida:")
    ll.display()
    
    print("Tempo total de execução:", time.time() - start_time, "segundos")

if __name__ == "__main__":
    main()
