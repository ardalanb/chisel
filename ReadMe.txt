Thought process:
- the complexity of the algorithm is O(1)
- if we want to reach that complexity we either need hash map or list.
- the data structure has to be ordered because the order is important in this case. (list or linked list)
- if we use list removing something from the beginning would be O(n) we can do better than this.
- hash map does have O(1) look up. So if we combine hash map and linked list would ideal.
(Why linked list? it's easier to add or remove items. but I have added a hashmap that the key is the actual key and
the value is the address of every node. So look up is actually O(1) - (using dictionary for hash map))

Assumptions:
- Time complexity - O(1) ~ fast look up and fast put, fast delete.
- If we are adding an item that already exists in the cache it will just overwrite the previous value and bring that node to the most recent nodes.
- we have head and tail node that sandwich our cache.
- if the user tries to delete a key that doesn't exist it will be no-op and cache will return -1 to show that the key doesn't exist.
- if the user is trying to get a key that is not in the dictionary I simply return -1
