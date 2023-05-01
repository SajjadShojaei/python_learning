# -------------[Sets]----------------
# Note: Set items are unchangeable, but you can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values.

thisset = {"apple", "banana", "cherry", "apple"}
print('thisset -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

print('checked iteme in set =====>' ,'banana' in thisset , '\n')

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

thisset.add('orange')
print('thisset_added_tiems -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')

# Add Sets
# To add items from another set into the current set, use the update() method.

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print('thisset_added_sets -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print('thisset_added_list -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove('kiwi')

# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard('anything')
print('thisset_remove_item -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')

# The clear() method empties the set:
thisset.clear()
print('thisset_clear_all_set -- lenght=> ' , len(thisset)  ,' \n type=>' , type(thisset)  ,'\n data =>' , thisset , '\n')


