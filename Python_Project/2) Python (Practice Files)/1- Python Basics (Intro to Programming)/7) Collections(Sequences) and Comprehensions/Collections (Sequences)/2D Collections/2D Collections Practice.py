# Example 1: list[lists]
print("List[Lists] Implementation:")
print()
fruits = ["Apple", "Banana", "Cherry","Pineapple", "Mango", "Grapes", "Raspberry"]
vegetables = ["Potato", "Cabbage", "Onion", "Carrot","Cauliflower", "Pumpkin", "Beet"]
meat = ["Chicken", "Fish", "Pork", "Beef","Mutton", "Tofu", "Turkey"]

grocery = [fruits, vegetables, meat]
print(f"Groceries Complete List: {grocery}")
print()
print("2D Lists Implementation 1 Practice Completed!")
print()

for i in range(0,3):
    for j in range(0,7):
        print(f"{grocery[i][j]}",end=" ")
    print()
print()
print("2D Lists Implementation 2 Practice Completed!")
print()

for sublist in grocery:
    for item in sublist:
        print(item, end=" ")
    print()
print()
print("2D Lists Implementation 3 Practice Completed!")
print()

# Example 2: list[tuples]
print("List[Tuples] Implementation:")
lt = [(1,2,3), (4,5,6), (7,8,9), ("*",0,"#")]
for row in lt:
    for col in row:
        print(col, end=" ")
    print()
print()

# Example 3: tuple(tuples)
print("Tuple(Tuples) Implementation:")
data = ((1, 'Ali'), (2, 'Sadullah'), (3, 'Bobby'),(4, 'Rohit'), (5, 'Rameez'))
for r in data:
    for c in r:
        print(c, end=" ")
    print()
print()

# Example 4: tuple(lists)
print("Tuple(Lists) Implementation: ")
Data = ([1, 2], [3, 4], [5, 6], [7, 8], [9, 0])
for ro in Data:
    for co in ro:
        print(co, end=" ")
    print()
print()

# Example 5: tuple(sets)
print("Tuple(Sets) Implementation: ")
da = ({1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 0})
for rows in da:
    for cols in rows:
        print(cols, end=" ")
    print()
print()

# Example 5: list[sets]
print("List[Sets] Implementation: ")
Da = [{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 0}]
for Rows in Da:
    for columns in Rows:
        print(columns, end=" ")
    print()
print()