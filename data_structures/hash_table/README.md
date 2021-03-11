# HASH TABLES

- associative storage in array
- O(1) lookup, key-> value mapping
- unordered
- key -----hash--func----> index --------> hash table - array of linked list; linked lists have values
  - key - value - what we sould like to store/retrieve/delete etc.
  - hash-func - converts key (any data type) to numerical index (eg. str key, index = sum of ascii values % size; (size of hash table)
- 2 or more keys map to same index -- HASH COLLISION; use linked list of values at each array position to store multiple values
- worst case collision - all our keys map to same index, single linked list, O(n) lookup



