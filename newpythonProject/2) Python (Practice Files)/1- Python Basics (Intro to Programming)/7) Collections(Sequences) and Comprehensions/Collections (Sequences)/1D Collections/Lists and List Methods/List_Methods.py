# 1) sort() Method
list1 = [5,1,89,56,100,34,45,98]
# Sorting in Ascending Order Permanently
list1.sort()
print(f"List1 After Sorting Permanently in Ascending Order: {list1}")
# Sorting in Descending Order Permanently
list1.sort(reverse = True)
print(f"List1 After Sorting Permanently in Descending Order: {list1}")

# 2) sorted() Method
list2 = [5,1,89,56,100,34,45,98]
# Temporary Sorting in Ascending Order
print(f"List2 After Temporary Sorting in Ascending Order: {sorted(list2)}")
# Temporary Sorting in Descending Order
print(f"List2 After Temporary Sorting in Descending Order: {sorted(list2, reverse = True)}")

# 3) clear() Method
list3 = [5,1,89,56,100,34,45,98]
list3.clear()
print(f"List3 After Clearing: {list3}")

# 4) copy() Method
list4 = [5,1,89,56,100,34,45,98]
copied_list = list4.copy()
print(f"Copied List of List4 (Shallow Copy - No Modification of the Original List4): {copied_list}")

# 5) count() Method
list5 = [5,1,89,56,100,34,45,98]
print(f"Number of 5's in List5 After Counting: {list5.count(5)}")

# 6) extend() Method
list6 = [5,1,89,56,100,34,45,98]
new_list = [100,200,300]
list6.extend(new_list)
print(f"List6 After Extending: {list6}")

# 7) index() Method
list7 = [5,1,89,56,100,34,45,98]
print(f"Index of 89 in List7: {list7.index(89)}")

# 8) insert() Method
list8 = [5,1,89,56,100,34,45,98]
list8.insert(4,300)
print(f"List8 After Insertion at Index 4: {list8}")

# 9) pop() Method
list9 = [5,1,89,56,100,34,45,98]
print(f"List9 After Popping: {list9.pop(3)}")

# 10) remove() Method
list10 = [5,1,89,56,100,34,45,98]
list10.remove(5)
print(f"List10 After Removal of 5: {list10}")

# 11) reverse() Method
list11 = [5,1,89,56,100,34,45,98]
list11.reverse()
print(f"List11 After Reversing: {list11}")
list11.sort()
print(f"List11 After Reversing and Sorting: {list11}")

# 12) append() Method
list12 = [5,1,89,56,100,34,45,98]
list12.append(78)
print(f"List12 After Appending 78: {list12}")

# 13) min() Method
list13 = [5,1,89,56,100,34,45,98]
print(f"List13's Min Value: {min(list13)}")

# 14) max() Method
list14 = [5,1,89,56,100,34,45,98]
print(f"List14's Max Value: {max(list14)}")

# 15) len() Method
list15 = [5,1,89,56,100,34,45,98]
print(f"Length of List15: { len(list15)}")