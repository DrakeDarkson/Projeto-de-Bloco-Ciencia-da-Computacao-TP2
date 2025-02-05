import time

class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = DNode(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.value)
            temp = temp.next
        print(elements)
    
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        
        current = self.head.next
        while current:
            key = current.value
            prev = current.prev
            while prev and prev.value > key:
                prev.next.value = prev.value
                prev = prev.prev
            if prev:
                prev.next.value = key
            else:
                self.head.value = key
            current = current.next
    
    def merge_sorted(self, other):
        merged = DoublyLinkedList()
        temp1, temp2 = self.head, other.head
        while temp1 and temp2:
            if temp1.value < temp2.value:
                merged.append(temp1.value)
                temp1 = temp1.next
            else:
                merged.append(temp2.value)
                temp2 = temp2.next
        while temp1:
            merged.append(temp1.value)
            temp1 = temp1.next
        while temp2:
            merged.append(temp2.value)
            temp2 = temp2.next
        return merged

def main():
    dll1 = DoublyLinkedList()
    dll2 = DoublyLinkedList()
    values1 = [4, 2, 9, 1, 7]
    values2 = [3, 5, 6, 8, 10]
    
    for v in values1:
        dll1.append(v)
    for v in values2:
        dll2.append(v)
    
    print("Lista antes da ordenação:")
    dll1.display()
    
    start_time = time.time()
    dll1.insertion_sort()
    end_time = time.time()
    
    print("Lista após ordenação:")
    dll1.display()
    print(f"Tempo de execução da ordenação: {end_time - start_time:.6f} segundos")
    
    print("Mesclando duas listas ordenadas:")
    merged_list = dll1.merge_sorted(dll2)
    merged_list.display()
    
    print("Tempo total de execução:", time.time() - start_time)
    
if __name__ == "__main__":
    main()
