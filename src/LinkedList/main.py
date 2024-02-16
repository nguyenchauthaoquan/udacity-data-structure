from src.LinkedList.doubly_linked_list import DoublyLinkedList

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.append(value=1)
doubly_linked_list.append(value=1.5)
doubly_linked_list.append(value=2)
doubly_linked_list.append(value=3)
doubly_linked_list.insert(position=0, value=0)
doubly_linked_list.insert(position=1, value=2.5)
doubly_linked_list.insert(position=2, value=4.5)
doubly_linked_list.insert(position=6, value=3.5)
doubly_linked_list.insert(position=20, value=30)
doubly_linked_list.insert(position=21, value=40)

doubly_linked_list.display()

print(len(doubly_linked_list))

print(doubly_linked_list.poll())

doubly_linked_list.display()
print(len(doubly_linked_list))

print(doubly_linked_list.pop())

doubly_linked_list.display()
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