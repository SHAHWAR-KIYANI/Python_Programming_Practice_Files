# String Indexing using  Indexing Operator / Slicing Operator i.e. [ start : end : step]
# start is inclusive and end is exclusive in the slicing operator

credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[ : : 1 ]) # It will print everything from start to end (Start from Left to Right i.e. Index 0 through Last Index)
print(credit_card_number[ : : -1 ]) # It will print everything from start to end (Starting from Right to Left means in Reverse  i.e. Index -1 then -2 and So On)
print(credit_card_number[ 0:4:1 ]) # It will print everything from index 0 uptill index 3 (Not Upto index 4 as end is exclusive)
print(credit_card_number[ 0:4:-1 ]) # It will print everything from index 0 uptill index 3 (Not Upto index 4 as end is exclusive) but in reverse order