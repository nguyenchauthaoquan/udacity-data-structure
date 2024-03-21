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
- Map: it offers a constant lookup time through the doubly linked list

### Time complexity:
###### Doubly Linked List

The total time complexity for adding new item at the end of the doubly linked list is O(1) since we want to maintain the order of the list without moving to the next one
The total time complexity for removing the head items with poll method takes O(1), it simply set the head and tail
The total time complexity for removing any items with remove method takes O(n), the best case is that the list have only one item that we want to remove and directly return to None and the list is unchanged if there is no value to remove. The worst case includes 2 cases:
1. The item we want to remove is not on the list, it takes n times to iterate all node in the list and find the match value
2. The item we want to remove is at the end of the list, it also takes n times to iterate all node in the list and find the match value

###### LRU algorithm time complexity

The total time for get method takes O(1) for the best case when there is no cache item or only 1 item in the map and O(n^2) for the worst case by processing the below steps:
- Checking the item we want to get by LRU cache with the in operator for the map takes n times
- Remove and append the item to the doubly linked list we want to get by LRU cache takes n times more
=> the total time is O(n * n) = O(n^2)
The total time for set method takes O(1) for the best case when there are only 1 match from the map and O(n^3) for the worst case by processing the below steps:
- Checking the item we want to get by LRU cache with the in operator for the map takes n times
- Remove and append the item to the doubly linked list we want to get the key-value pair by LRU cache takes n times more
- The total time for removing the map with del operator takes n times for the worst case and 1 for best case, because this operator works based on the ```__del__``` method

### Space complexity
###### Doubly Linked List

The total space complexity for adding new item at the end of the doubly linked list with append method is O(1) with only assigning to head and the tail, it only involves creating a new node and adjusting a few pointers.
The total space complexity for removing the item of the doubly linked list is O(1) with the remove method. It adjusts the head and the tail without allocating the new node
The total space complexity for removing the item of the doubly linked list is O(1) with the poll method. It adjusts the head and the tail without allocating the new node

###### LRU algorithm time complexity

The total space complexity is O(1), The get method doesn't require any additional space allocation beyond the variables used within the method itself, so its space complexity remains constant.

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
![priority_queue.png](documents%2Fimages%2Fpriority_queue.png). In this project, I will use the min heap instead, although the order is different from heapq transformation list, but the order is correct when using the traditional traversal

