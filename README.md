# Project: Show Me the Data Structures

## Overview
For this project, you will answer the six questions laid out in the next sections. The questions cover a variety of topics related to the data structures you've learned in this course. You will write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices.

## Problem solution analysis
### I. Problem 1: Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

```python
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
```

### Solution analysis
In order to implement this solution, I applied 2 type of data structure:

- Doubly Linked List: I have implemented the doubly linked list instead of using the [structlinks](https://pypi.org/project/structlinks/) or no built-in list/collection package, you can find it in ```src/LinkedList/doubly_linked_list.py```. In this algorithm, I use only the remove, poll (remove the head if the non-getting cache exists) and append method to move the cache item to the head of the list. You can find the visualization in DLL section [here](https://visualgo.net/en/list)

```python
class DoublyLinkedList:
    """
    The doubly linked list
    """

    def __init__(self, items=None):
        """
        Initialize the doubly linked list with the provided list or not
        @param items: the provided list items
        """
        self.head = None
        self.tail = None

        if items is None:
            items = []

        if len(items) > 0:
            for item in items:
                self.append(item)

    def append(self, value):
        """
        Add the new element at the tail of the doubly linked list
        @param value: the new element to be added at the tail of the doubly linked list
        """
        new_node = DoublyLinkedListNode(value=value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def poll(self):
        """
        Remove the head of the doubly linked list and return the removed element
        @return: the element to be removed from the doubly linked list
        """
        current = self.head

        if current is None:
            return None
        self.head = current.next

        if self.head is not None:
            self.head.prev = None

        if current is self.tail:
            self.pop()
        return current.value
    
    def pop(self, position=-1):
        """
        Remove the tail or the specific position of the doubly linked list and return the removed value
        @param position: The position of the element from doubly linked list, defaults to -1
        @return: the removed node value from the doubly linked list
        """
        # removes the tail of the doubly linked list if the position is negative.
        if position <= 0:
            current = self.tail

            if current is None:
                return None
            self.tail = current.prev

            if self.tail is not None:
                self.tail.next = None

            if current is self.head:
                self.poll()

            return current.value

        current = self.head

        # if the position is out of range of the doubly linked list,
        # remove the tail of the doubly linked list by default
        for _ in range(position):
            if current is None:
                return self.pop()
            current = current.next
        # if position is in range of the doubly linked list
        # remove the item from the specific position of the doubly linked list.
        if current is None:
            return None

        if current is self.head:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current is self.tail:
            self.tail = current.prev
        else:
            current.next.prev = current.prev

        return current.value

    def remove(self, value):
        """
        Remove the element from the doubly linked list
        @param value: the new element to be added at the specific position of the doubly linked list
        """
        removed_node = None
        current = self.head

        while current is not None:
            if current.value == value:
                removed_node = current
                break
            current = current.next

        if removed_node is None:
            return None

        if removed_node == self.head:
            self.poll()
        elif removed_node == self.tail:
            self.pop()
        else:
            next_node = removed_node.next
            prev_node = removed_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
```

- Map: it offers a constant lookup time through the doubly linked list

```python
class LRUCache:
    def __init__(self, capacity):
        self.caches = {}
        self.linked_list = DoublyLinkedList()
        if isinstance(capacity, int):
            if capacity >= 0:
                self.capacity = capacity
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get(self, key):
        # Move the key to the head of the doubly linked list and return the items from the map
        if key in self.linked_list:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(self.caches[key])

            return self.caches[key]
        return -1 # In case there is no key in map

    def set(self, key, value):
        # Move the key to the head of the doubly linked list and return the items from the map
        if key in self.caches:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(value)
        else:
            # Remove the head key from the linked list and the map
            if len(self.caches) >= self.capacity:
                del self.caches[self.linked_list.poll()]
            self.caches[key] = value
            # Add the value to the linked list
            self.linked_list.append(value)
```

### Time complexity:
###### Doubly Linked List

```python
class DoublyLinkedList:
    """
    The doubly linked list
    """

    def __init__(self, items=None):
        """
        Time complexity: O(n)
        """
        self.head = None
        self.tail = None

        if items is None:
            items = []

        if len(items) > 0:
            for item in items: # O(n)
                self.append(item)

    def append(self, value):
        """
        Time complexity: O(1)
        """
        new_node = DoublyLinkedListNode(value=value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def poll(self):
        """
        Time complexity: O(1)
        """
        current = self.head

        if current is None:
            return None
        self.head = current.next

        if self.head is not None:
            self.head.prev = None

        if current is self.tail:
            self.pop() # O(1) for the best case;O(n) for the worst case
        return current.value
    
    def pop(self, position=-1):
        """
        Time complexity: O(n)
        """
        # removes the tail of the doubly linked list if the position is negative.
        if position <= 0:
            current = self.tail

            if current is None:
                return None
            self.tail = current.prev

            if self.tail is not None:
                self.tail.next = None

            if current is self.head:
                self.poll() # O(n)

            return current.value

        current = self.head

        # if the position is out of range of the doubly linked list,
        # remove the tail of the doubly linked list by default
        for _ in range(position): # O(n) if the search node is out of range
            if current is None:
                return self.pop()
            current = current.next
        # if position is in range of the doubly linked list
        # remove the item from the specific position of the doubly linked list.
        if current is None:
            return None

        if current is self.head:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current is self.tail:
            self.tail = current.prev
        else:
            current.next.prev = current.prev

        return current.value

    def remove(self, value):
        """
        Time complexity: O(n)
        """
        removed_node = None
        current = self.head

        while current is not None: # O(n) for searching the removable node
            if current.value == value:
                removed_node = current
                break
            current = current.next

        if removed_node is None:
            return None

        if removed_node == self.head:
            self.poll()
        elif removed_node == self.tail:
            self.pop() # O(n)
        else:
            next_node = removed_node.next
            prev_node = removed_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
```

###### LRU algorithm

```python
class LRUCache:
    def __init__(self, capacity):
        self.caches = {}
        self.linked_list = DoublyLinkedList()
        if isinstance(capacity, int):
            if capacity >= 0:
                self.capacity = capacity
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get(self, key):
        """
        Time complexity: O(n^2)
        """
        if key in self.linked_list: # O(n)
            self.linked_list.remove(self.caches[key]) # O(n)
            self.linked_list.append(self.caches[key])

            return self.caches[key]
        return -1

    def set(self, key, value):
        """
        Time complexity: O(n^2)
        """
        if key in self.caches: # O(n)
            self.linked_list.remove(self.caches[key]) # O(n)
            self.linked_list.append(value)
        else:
            if len(self.caches) >= self.capacity:
                del self.caches[self.linked_list.poll()]
            self.caches[key] = value
            self.linked_list.append(value)
```

### Space complexity
###### Doubly Linked List

```python
class DoublyLinkedList:
    """
    The doubly linked list
    """

    def __init__(self, items=None):
        """
        Space complexity: O(n)
        """
        self.head = None
        self.tail = None

        if items is None:
            items = []

        if len(items) > 0:
            for item in items:
                self.append(item)

    def append(self, value):
        """
        Space complexity: O(1)
        """
        new_node = DoublyLinkedListNode(value=value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def poll(self):
        """
        Space complexity: O(1)
        """
        current = self.head

        if current is None:
            return None
        self.head = current.next

        if self.head is not None:
            self.head.prev = None

        if current is self.tail:
            self.pop()
        return current.value
    
    def pop(self, position=-1):
        """
        Space complexity: O(1)
        """
        # removes the tail of the doubly linked list if the position is negative.
        if position <= 0:
            current = self.tail

            if current is None:
                return None
            self.tail = current.prev

            if self.tail is not None:
                self.tail.next = None

            if current is self.head:
                self.poll()

            return current.value

        current = self.head

        # if the position is out of range of the doubly linked list,
        # remove the tail of the doubly linked list by default
        for _ in range(position): # O(n) if the search node is out of range
            if current is None:
                return self.pop()
            current = current.next
        # if position is in range of the doubly linked list
        # remove the item from the specific position of the doubly linked list.
        if current is None:
            return None

        if current is self.head:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current is self.tail:
            self.tail = current.prev
        else:
            current.next.prev = current.prev

        return current.value

    def remove(self, value):
        """
        Space complexity: O(1)
        """
        removed_node = None
        current = self.head

        while current is not None:
            if current.value == value:
                removed_node = current
                break
            current = current.next

        if removed_node is None:
            return None

        if removed_node == self.head:
            self.poll()
        elif removed_node == self.tail:
            self.pop()
        else:
            next_node = removed_node.next
            prev_node = removed_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
```


###### LRU algorithm


```python
class LRUCache:
    def __init__(self, capacity):
        self.caches = {}
        self.linked_list = DoublyLinkedList()
        if isinstance(capacity, int):
            if capacity >= 0:
                self.capacity = capacity
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get(self, key):
        """
        Space complexity: O(1)
        """
        if key in self.linked_list:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(self.caches[key])

            return self.caches[key]
        return -1

    def set(self, key, value):
        """
        Space complexity: O(1)
        """
        if key in self.caches:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(value)
        else:
            if len(self.caches) >= self.capacity:
                del self.caches[self.linked_list.poll()]
            self.caches[key] = value
            self.linked_list.append(value)
```

### II. Problem 2: File Recursion

Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip)

```text
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
```
Python's ```os``` module will be useful—in particular, you may want to use the following resources:

[os.path.isdir(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)

[os.path.isfile(path)](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)

[os.listdir(directory)](https://docs.python.org/3.7/library/os.html#os.listdir)

[os.path.join(...)](https://docs.python.org/3.7/library/os.path.html#os.path.join)

### Solution analysis
I have implemented 2 ways (using the built-in (find_files_with_built_in(suffix, path)) and manual(find_files(self, suffix, path))), both of them have the same idea
For the manual solution, I have used find_files function which will take suffix (file extension) and path (directory path where we need to search). In this function, I am recursively searching for a file with a given extension in a parent directory and all its sub-directories. I am storing all these files with a given suffix in a list and returning it as the set.

### Time complexity:
#### Using built-in solution
The total time of calling os.walk(path) in find_files_with_built_in method takes n times for iteration and n times for iteration the file item from os.walk(path) method and n times for checking the file extension with endwith method => the overall time complexity is O(n^3)
The total time of calling os.listdir takes n times for enlist all file directory and the loop takes n time for iterate through this list => total overall time complexity is O(n + n) ~= O(n)

### Space complexity:
The space complexity for find_file method takes O(n) for allocating the string to each item of the list

### III. Problem 3: Huffman coding
#### Overview
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

### Solution analysis
##### Huffman Coding solution

Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
1.First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.

| (Unique) Character | Frequency |
|--------------------|-----------|
| A	                 | 7         |
| B	                 | 3         |
| C	                 | 7         |
| D	                 | 2         |     
| E	                 | 6         |     

2. Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.

We would need our list to work as a [priority queue](https://en.wikipedia.org/wiki/Priority_queue), where a node that has lower frequency should have a higher priority to be popped-out. The following snapshot will help you visualize the example considered above:
![priority_queue.png](documents%2Fimages%2Fpriority_queue.png)

In this project, I will use the min heap instead of priority queue, both of them operate the same, although the order is different from heapq transformation list, but the order is correct when using the traditional traversal
3. Pop-out two nodes with the minimum frequency from the priority queue created in the above step.

4. Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.

5. Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.

![huffman-tree-1.png](documents%2Fimages%2Fhuffman-tree-1.png)

![huffman-tree-2.png](documents%2Fimages%2Fhuffman-tree-2.png)

6. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:

![huffman-tree-3.png](documents%2Fimages%2Fhuffman-tree-3.png)

7. Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.


| (Unique) Character | Frequency | Huffman Code |
|:-------------------|-----------|--------------|
| D                  | 2         | 000          | 
| B                  | 3         | 001          | 
| E                  | 6         | 01           | 
| A                  | 7         | 10           | 
| C                  | 7         | 11           |

#### Time complexity
##### Heap
The time complexity for adding new item into the binary tree and swap the position between this new node and the parent node with add method to binary heap tree is O(log(n)) for the overall time complexity:

```python
    def add(self, value):
        """
        Time complexity: O(log(n))
        """
        if not self.root:
            self.root = Node(value=value)
            return

        traversed = [self.root]
        while len(traversed) > 0: # O(log(n)) for the worst case during the traversal sequence
            node = traversed.pop(0)

            if not node.left:
                node.left = Node(value=value)
                break
            elif not node.right:
                node.right = Node(value=value)
                break
            else:
                traversed.append(node.left)
                traversed.append(node.right)

        self._heaptify_up(value) # O(log(n))
    
    
    def _heaptify_up(self, value):
        """
        Time complexity: O(log(n))
        """
        found_node = self._find_heap_node(self.root, value) # O(n)

        while found_node:# O(log(n) for the worst case during the traversal sequence
            parent_node = self._find_parent_node(self.root, value) # O(n)

            if parent_node and self.comparator(parent_node, found_node):
                parent_node.value, found_node.value = found_node.value, parent_node.value
                found_node = parent_node
            else:
                break

    def _find_heap_node(self, node, value):
        """
        Time complexity: T(n) = 2T(n/2) => O(n)
        """
        if not node:
            return None
        if node.value == value:
            return node
        left_node = self._find_heap_node(node.left, value) # T(n/2)
        right_node = self._find_heap_node(node.right, value) # T(n/2)

        return left_node if left_node else right_node

    def _find_parent_node(self, node, value):
        """
        Time complexity: T(n) = 2T(n/2) => O(n)
        """
        if not node:
            return None

        if (node.left and node.left.value == value) or (node.right and node.right.value == value):
            return node

        left_node = self._find_parent_node(node.left, value) # T(n/2)
        right_node = self._find_parent_node(node.right, value) # T(n/2)

        return left_node if left_node else right_node
```

The time complexity for root extraction by removing the old root node from heap and move the node from the last index of the tree takes O(log(n)) for the overall time complexity:

```python
    def extract(self):
        """
        Time complexity: O(log(n))
        """
        if not self.root:
            return None
        current_value = self.root.value
        last_node = self._find_last_node() # O(n)

        if self.root == last_node:
            self.root = None
        else:
            self.root.value = last_node.value
            self._remove_last_node() # O(n)
            self._heaptify_down(self.root.value) # O(log(n))
        return current_value

    def _find_last_node(self):
        """
        Time complexity: O(n)
        """
        global node
        traversed = [self.root]

        while len(traversed) > 0: # O(n)
            node = traversed.pop(0)
            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)
        return node
    
    def _find_child_node(self, node):
        """
        Time complexity: O(1)
        """
        if not node:
            return None
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        return node.left if self.comparator(node.left, node.right) else node.right

    def _remove_last_node(self):
        """
        Time complexity: O(n)
        """
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:# O(n) for the worst case during the traversal sequence
            node = queue.pop(0)

            if node.left:
                if node.left == self._find_last_node(): # O(n)
                    node.left = None
                    break
                else:
                    queue.append(node.left)
            if node.right:
                if node.right == self._find_last_node(): # O(n)
                    node.right = None
                    break
                else:
                    queue.append(node.right)

    def _heaptify_down(self, value):
        """
        Time complexity: O(log(n))
        """
        found_node = self._find_heap_node(self.root, value) #O(n)

        while found_node:# O(log(n) for the worst case during the traversal sequence
            found_child_node = self._find_child_node(found_node) #O(n)
            if found_child_node and found_child_node.value > found_node.value:
                found_child_node.value, found_node.value = found_node.value, found_child_node.value
                found_node = found_child_node
            else:
                break
```

#### Space complexity

The space complexity for adding new item into the binary tree and swap the position between this new node and the parent node with add method to binary heap tree is O(n) for the overall space complexity:

```python
    def add(self, value):
        """
        Space complexity: O(n)
        """
        if not self.root:
            self.root = Node(value=value)
            return

        traversed = [self.root] # O(n)
        while len(traversed) > 0: # O(n)
            node = traversed.pop(0)

            if not node.left:
                node.left = Node(value=value)
                break
            elif not node.right:
                node.right = Node(value=value)
                break
            else:
                traversed.append(node.left)
                traversed.append(node.right)

        self._heaptify_up(value) # O(n)
    
    
    def _heaptify_up(self, value):
        """
        Space complexity: O(n)
        """
        found_node = self._find_heap_node(self.root, value) #O(n)

        while found_node:
            parent_node = self._find_parent_node(self.root, value) # O(n)

            if parent_node and self.comparator(parent_node, found_node):
                parent_node.value, found_node.value = found_node.value, parent_node.value
                found_node = parent_node
            else:
                break

    def _find_heap_node(self, node, value):
        """
        Space complexity: O(n)
        """
        if not node:
            return None
        if node.value == value:
            return node
        left_node = self._find_heap_node(node.left, value) # O(n)
        right_node = self._find_heap_node(node.right, value) # O(n)

        return left_node if left_node else right_node

    def _find_parent_node(self, node, value):
        """
        Space complexity: O(n)
        """
        if not node:
            return None

        if (node.left and node.left.value == value) or (node.right and node.right.value == value):
            return node

        left_node = self._find_parent_node(node.left, value) # O(n)
        right_node = self._find_parent_node(node.right, value) #O(n)

        return left_node if left_node else right_node
```

The space complexity for root extraction by removing the old root node from heap and move the node from the last index of the tree takes O(n) for the overall space complexity:

```python
    def extract(self):
        """
        Space complexity: O(n)
        """
        if not self.root:
            return None
        current_value = self.root.value
        last_node = self._find_last_node() # O(n)

        if self.root == last_node:
            self.root = None
        else:
            self.root.value = last_node.value
            self._remove_last_node() # O(n)
            self._heaptify_down(self.root.value) # O(n)
        return current_value

    def _find_last_node(self):
        """
        Space complexity: O(n)
        """
        global node
        traversed = [self.root] # O(n)

        while len(traversed) > 0: # O(n)
            node = traversed.pop(0)
            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)
        return node
    
    def _find_child_node(self, node):
        """
        Space complexity: O(1)
        """
        if not node:
            return None
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        return node.left if self.comparator(node.left, node.right) else node.right


    def _remove_last_node(self):
        """
        Space complexity: O(n)
        """
        if not self.root:
            return

        queue = [self.root] # O(n)

        while len(queue) > 0: # O(n)
            node = queue.pop(0)

            if node.left:
                if node.left == self._find_last_node():
                    node.left = None
                    break
                else:
                    queue.append(node.left)
            if node.right:
                if node.right == self._find_last_node():
                    node.right = None
                    break
                else:
                    queue.append(node.right)

    def _heaptify_down(self, value):
        """
        Space complexity: O(n)
        """
        found_node = self._find_heap_node(self.root, value) # O(n)

        while found_node:
            found_child_node = self._find_child_node(found_node)
            if found_child_node and found_child_node.value > found_node.value:
                found_child_node.value, found_node.value = found_node.value, found_child_node.value
                found_node = found_child_node
            else:
                break
```


##### Huffman Coding solution
#### Time complexity

```python
    def merge_nodes(self, sequence):
        """
        Time complexity: O(nlog(n))
        """
        frequency = {}

        if sequence is not None:

            for char in sequence:
                frequency[char] = frequency.get(char, 0) + 1

            min_heap = Heap()  # [HuffmanNode(char, freq) for char, freq in frequency.items()]

            for char, freq in frequency.items(): # O(n)
                min_heap.add(HuffmanNode(char=char, frequency=freq)) # O(log(n))

            while len(min_heap) > 1: # O(n)
                left = min_heap.extract() # O(log(n))
                right = min_heap.extract() # O(log(n))

                merged_frequency = left.frequency + right.frequency
                merged_node = HuffmanNode(None, merged_frequency)
                merged_node.left = left
                merged_node.right = right
                min_heap.add(merged_node)

            return min_heap.extract() # O(log(n))

    def build_huffman_codes(self, root, code='', codes=None):
        """
        Time complexity: O(n)
        """
        if codes is None:
            codes = {}
        if root:
            if not root.left and not root.right:
                codes[root.char] = code
            self.build_huffman_codes(root.left, code + '0', codes) # O(n)
            self.build_huffman_codes(root.right, code + '1', codes) # O(n)
        return codes

    def huffman_encoding(self, sequence):
        """
        Time complexity O(nlog(n))
        """
        if not sequence:
            return '', None

        merged_node = self.merge_nodes(sequence) # O(nlog(n))
        codes = self.build_huffman_codes(merged_node) # O(n)

        encoded_sequence = ''.join(codes[char] for char in sequence) # O(n)

        return encoded_sequence, merged_node

    def huffman_decoding(self, sequence, merged_node):
        """
        Time complexity O(n)
        """
        if not sequence or not merged_node:
            return ''

        decoded_sequence = ''
        current_node = merged_node

        for bit in sequence: # O(n)
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if not current_node.left and not current_node.right:
                decoded_sequence += current_node.char
                current_node = merged_node

        return decoded_sequence
```

#### Space complexity

```python
    def merge_nodes(self, sequence):
        """
        Space complexity: O(n)
        """
        frequency = {}

        if sequence is not None:

            for char in sequence:
                frequency[char] = frequency.get(char, 0) + 1

            min_heap = Heap()  # [HuffmanNode(char, freq) for char, freq in frequency.items()]

            for char, freq in frequency.items():
                min_heap.add(HuffmanNode(char=char, frequency=freq))

            while len(min_heap) > 1:
                left = min_heap.extract()
                right = min_heap.extract()

                merged_frequency = left.frequency + right.frequency
                merged_node = HuffmanNode(None, merged_frequency)
                merged_node.left = left
                merged_node.right = right
                min_heap.add(merged_node)

            return min_heap.extract()

    def build_huffman_codes(self, root, code='', codes=None):
        """
        Space complexity: O(n)
        """
        if codes is None:
            codes = {}
        if root:
            if not root.left and not root.right:
                codes[root.char] = code
            self.build_huffman_codes(root.left, code + '0', codes)
            self.build_huffman_codes(root.right, code + '1', codes)
        return codes

    def huffman_encoding(self, sequence):
        """
        Space complexity: O(n)
        """
        if not sequence:
            return '', None

        merged_node = self.merge_nodes(sequence)
        codes = self.build_huffman_codes(merged_node)

        encoded_sequence = ''.join(codes[char] for char in sequence)

        return encoded_sequence, merged_node

    def huffman_decoding(self, sequence, merged_node):
        """
        Space complexity: O(1)
        """
        if not sequence or not merged_node:
            return ''

        decoded_sequence = ''
        current_node = merged_node

        for bit in sequence:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if not current_node.left and not current_node.right:
                decoded_sequence += current_node.char
                current_node = merged_node

        return decoded_sequence
```
### IV. Problem 4: Active Directory
### Overview
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
Write a function that provides an efficient look up of whether the user is in a group.

```python
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return None

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
```

### Solution analysis
I re-used the following provided code (class Group) without any manual data structure, and I noted the solution in :

```python
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if group is not None:
            self.groups.append(group)

    def add_user(self, user):
        if user is not None and len(user.strip()) > 0:
            self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()

    if user in users: # First, checks the user to search exists in the parent group
        return True
    else:
        groups = group.get_groups() 
        for group_item in groups: # If the user to search does not exist in the parent group, finds it in the derived group by using the recursive.
            if is_user_in_group(user, group_item):
                return True
        return False
```

#### Time complexity

```python
def is_user_in_group(user, group):
    """
    Time complexity: O(n)
    """
    users = group.get_users()

    if user in users:
        return True
    else:
        groups = group.get_groups() 
        for group_item in groups: # O(n)
            if is_user_in_group(user, group_item): # O(n)
                return True
        return False
```

#### Space complexity

```python
def is_user_in_group(user, group):
    """
    Space complexity: O(n)
    """
    users = group.get_users()

    if user in users:
        return True
    else:
        groups = group.get_groups() 
        for group_item in groups:
            if is_user_in_group(user, group_item): # O(n)
                return True
        return False
```

### V. Problem 5: Blockchain
### Overview

[A Blockchain](https://en.wikipedia.org/wiki/Blockchain) is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.
Use your knowledge of linked lists and hashing to create a blockchain implementation.

![untitled-diagram.png](documents%2Fimages%2Funtitled-diagram.png)

### Solution analysis

In this problem, I used the linked list (the entire implementation is in ```src/LinkedList/linked_list.py```) without the external packages (structlinks, list,...) and the provided code:

```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Initialize the singly-linked list
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items:
            self.append(item)

    def push(self, value):
        """
        Add the specified element at the beginning of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def append(self, value):
        """
        Add the specified element at the end of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
```

```python
import hashlib
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
        
    def calc_hash(self):
        
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
```
Here is my solution for problem 5
```python
class BlockChain:
    def __init__(self):
        self.blocks = LinkedList()

    def add_block(self, data):
        current_time = datetime.datetime.utcnow() # Gets the current timestamp

        if len(self.blocks) == 0:
            self.blocks.append(Block(current_time, data, 0))  # Add the first block into the linked list if the list is empty, this block has no previous hashing string
        else:
            new_block = Block(current_time, data, self.blocks.tail.value.hash)
            self.blocks.append(new_block)# keep adding the other blocks behind the 1st block, these block will have the previous hashing string from their front

    def print_blocks(self):
        current_block = self.blocks.head
        while current_block:
            print("Index:", self.blocks.index(current_block.value))
            print("Timestamp:", current_block.value.timestamp)
            print("Data:", current_block.value.data)
            print("Previous Hash:", current_block.value.previous_hash)
            print("Hash:", current_block.value.hash)
            print()
            current_block = current_block.next

    def __contains__(self, item):
        current_block = self.blocks.head
        while current_block:
            if item == current_block.value.data:
                return True
        return False
```

#### Time complexity

```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Initialize the singly-linked list
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items:
            self.append(item)

    def push(self, value):
        """
        Time complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def append(self, value):
        """
        Time complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
```

```python
class BlockChain:
    def __init__(self):
        self.blocks = LinkedList()

    def add_block(self, data):
        """
        Time complexity: O(n)
        """
        current_time = datetime.datetime.utcnow()

        if len(self.blocks) == 0: # O(n)
            self.blocks.append(Block(current_time, data, 0))
        else:
            new_block = Block(current_time, data, self.blocks.tail.value.hash)
            self.blocks.append(new_block)

    def print_blocks(self):
        """
        Time complexity: O(n)
        """
        current_block = self.blocks.head
        while current_block: # O(n)
            print("Index:", self.blocks.index(current_block.value))
            print("Timestamp:", current_block.value.timestamp)
            print("Data:", current_block.value.data)
            print("Previous Hash:", current_block.value.previous_hash)
            print("Hash:", current_block.value.hash)
            print()
            current_block = current_block.next

    def __contains__(self, item):
        """
        Time complexity: O(n)
        """
        current_block = self.blocks.head
        while current_block: # O(n)
            if item == current_block.value.data:
                return True
        return False
```

#### Space complexity

```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Initialize the singly-linked list
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items:
            self.append(item)

    def push(self, value):
        """
        Space complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def append(self, value):
        """
        Space complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
```

```python
class BlockChain:
    def __init__(self):
        self.blocks = LinkedList()

    def add_block(self, data):
        """
        Space complexity: O(1)
        """
        current_time = datetime.datetime.utcnow() 

        if len(self.blocks) == 0:
            self.blocks.append(Block(current_time, data, 0))
        else:
            new_block = Block(current_time, data, self.blocks.tail.value.hash)
            self.blocks.append(new_block)

    def print_blocks(self):
        """
        Space complexity: O(1)
        """
        current_block = self.blocks.head
        while current_block:
            print("Index:", self.blocks.index(current_block.value))
            print("Timestamp:", current_block.value.timestamp)
            print("Data:", current_block.value.data)
            print("Previous Hash:", current_block.value.previous_hash)
            print("Hash:", current_block.value.hash)
            print()
            current_block = current_block.next

    def __contains__(self, item):
        """
        Space complexity: O(1)
        """
        current_block = self.blocks.head
        while current_block:
            if item == current_block.value.data:
                return True
        return False
```

### VI. Problem 6: Union and Intersection

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
```
### Solution analysis
In this problem, I don't use the provided linked list, but I will re-use my linked list, it can find the union and intersection between current linked list and the second linked list:

```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Initialize the singly-linked list
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items:
            self.append(item)

    def push(self, value):
        """
        Add the specified element at the beginning of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        """
        Add the specified element at the end of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def copy(self):
        """
        Copy each item of the original linked list to the new one
        @return: the new linked list
        """
        cloned_linked_list = LinkedList()
        current = self.head

        while current is not None:
            cloned_linked_list.append(current.value)
            current = current.next

        return cloned_linked_list
    def union(self, linked_list):
        """
        Finds the union between 2 provided linked lists.
        @param linked_list: the 2nd linked list
        @return: the linked list including the union between 2 provided linked lists.
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        union_linked_list = self.copy()
        current = linked_list.head

        while current is not None:
            if current.value not in union_linked_list:
                union_linked_list.append(current.value)
            current = current.next

        return union_linked_list

    def intersection(self, linked_list):
        """
        Finds the intersection between two provided linked lists
        @param linked_list: the 2nd linked list
        @return: the linked list including the intersection between 2 provided linked lists
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        intersection_linked_list = LinkedList()
        current = self.head

        while current:
            if current.value in linked_list:
                intersection_linked_list.append(current.value)
            current = current.next

        return intersection_linked_list
```

#### Time complexity

```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Time complexity: O(n)
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items: # O(n)
            self.append(item)

    def push(self, value):
        """
        Time complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        """
        Time complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def copy(self):
        """
        Time complexity: O(n)
        """
        cloned_linked_list = LinkedList()
        current = self.head

        while current is not None: # O(n)
            cloned_linked_list.append(current.value)
            current = current.next

        return cloned_linked_list
    def union(self, linked_list):
        """
        Time complexity: O(n^2)
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        union_linked_list = self.copy()
        current = linked_list.head

        while current is not None: # O(n)
            if current.value not in union_linked_list: # O(n)
                union_linked_list.append(current.value)
            current = current.next

        return union_linked_list

    def intersection(self, linked_list):
        """
        Time complexity: O(n^2)
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        intersection_linked_list = LinkedList()
        current = self.head

        while current: # O(n)
            if current.value in linked_list: # O(n)
                intersection_linked_list.append(current.value)
            current = current.next

        return intersection_linked_list

    def __contains__(self, value):
        """
        Time complexity: O(n)
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        """
        Time complexity: O(n)
        """
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
```

#### Space complexity
```python
class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Space complexity: O(n)
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items: # O(n)
            self.append(item)

    def push(self, value):
        """
        Space complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        """
        Space complexity: O(1)
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def copy(self):
        """
        Space complexity: O(n)
        """
        cloned_linked_list = LinkedList()
        current = self.head

        while current is not None: # O(n)
            cloned_linked_list.append(current.value)
            current = current.next

        return cloned_linked_list
    def union(self, linked_list):
        """
        Space complexity: O(n)
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        union_linked_list = self.copy()
        current = linked_list.head

        while current is not None: # O(n)
            if current.value not in union_linked_list:
                union_linked_list.append(current.value)
            current = current.next

        return union_linked_list

    def intersection(self, linked_list):
        """
        Space complexity: O(n)
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        intersection_linked_list = LinkedList()
        current = self.head

        while current: # O(n)
            if current.value in linked_list:
                intersection_linked_list.append(current.value)
            current = current.next

        return intersection_linked_list

    def __contains__(self, value):
        """
        Space complexity: O(1)
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        """
        Space complexity: O(1)
        """
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
```

## How can I run the code
### Installation:
Make sure that you will need these setups:
1. Programming language SDK environment: [Python](https://www.python.org/downloads/)
2. IDE: [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
3. Packages: parameterized, unittest (make sure either pip or conda is required)
### Run the sample code
You can run directly in the src to view some sample outputs by right-clicking the python file (main.py or the name of the problem(for example of the Problem 1: LRU Cache, then the correspond file is LRUCache.py))
I have added the test cases by using the python unittest, you can run one of the python file (problem_1.py, problem_1.py, problem_2.py, problem_3.py, problem_4.py, problem_5, problem_6.py) based on the problem name in test folder, the name of each folder in test folder is the problem name
