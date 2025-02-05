import time

class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        new_node = DNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        new_node = DNode(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_position(self, position):
        if not self.head:
            return
        current = self.head
        for _ in range(position):
            if not current.next:
                return
            current = current.next
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.prev
        print()

def main():
    start_time = time.time()
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.display_forward()
    dll.display_reverse()
    dll.delete_at_position(1)
    dll.display_forward()
    end_time = time.time()
    print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
