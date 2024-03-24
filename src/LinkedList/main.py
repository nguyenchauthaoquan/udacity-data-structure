from src.LinkedList.doubly_linked_list import DoublyLinkedList
from src.LinkedList.linked_list import LinkedList

if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.append(value=1)
    doubly_linked_list.append(value=1.5)
    doubly_linked_list.append(value=2)
    doubly_linked_list.append(value=3)
    doubly_linked_list.display()
    doubly_linked_list.add(position=0, value=0)
    doubly_linked_list.display()
    doubly_linked_list.add(position=-1, value=-1)
    doubly_linked_list.display()
    doubly_linked_list.add(position=1, value=2.5)
    doubly_linked_list.display()
    doubly_linked_list.add(position=2, value=4.5)
    doubly_linked_list.display()
    doubly_linked_list.add(position=3, value=3.5)
    doubly_linked_list.display()
    doubly_linked_list.add(position=20, value=30)
    doubly_linked_list.display()
    doubly_linked_list.add(position=21, value=40)
    doubly_linked_list.display()

    print(len(doubly_linked_list))

    print(doubly_linked_list.poll())

    doubly_linked_list.display()
    print(len(doubly_linked_list))

    print(doubly_linked_list.pop())

    print(len(doubly_linked_list))

    print(doubly_linked_list.index(2.5))
    print(doubly_linked_list.index(1))
    print(doubly_linked_list.index(1.5))
    print(doubly_linked_list.index(2))
    print(doubly_linked_list.index(3))
    print(2.5 in doubly_linked_list)
    doubly_linked_list.remove(2.5)
    doubly_linked_list.display()
    print(len(doubly_linked_list))

    print(2.5 in doubly_linked_list)

    print("Initialized the linked list")
    linked_list = DoublyLinkedList([1, 2, 3, 4])
    linked_list.display()

    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)

    linked_list.add(position=0, value=0)
    linked_list.display()

    linked_list.remove(0)
    print(linked_list.pop())
    linked_list.display()
    print(linked_list.pop(0))
    linked_list.display()
    print(linked_list.poll())
    linked_list.display()
    print(linked_list.pop(position=1))
    linked_list.display()
    print(linked_list.pop(position=10))
    linked_list.display()

    print("Singly Linked List")

    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(7)
    linked_list.display()

    linked_list2 = LinkedList()

    linked_list2.display()

    linked_list3 = linked_list.intersection(linked_list2)
    linked_list3.display()

    linked_list4 = linked_list.union(linked_list2)
    linked_list4.display()
