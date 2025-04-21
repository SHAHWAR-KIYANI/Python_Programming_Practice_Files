# Format Specifiers = {value:flags} and It means to format a value on the basis of what flags are inserted. Format Specifiers here discussed are in context of f-strings. After the value, Colon is used for format specifiers
price1 = 97.234
print(f"Price1 is ${price1:.2f}")  # .(number)f after colon means round to that many decimal places (fixed point) and here .2f means upto two decimal places
price2 = 789.23
print(f"Price2 is ${price2:10}") # (number) after colon means to allocate that many spaces and here 10 spaces
price3 = 21.12
print(f"Price3 is ${price3:010}") # Here 010 means allocate and zero pad that many spaces (Total 10 spaces will be there left to right and empty spaces will be zero padded on the extreme left side
price4 = -987.675
print(f"Price4 is ${price4:<}") # Left Justify
price5 = 3000000000.78998
print(f"Price5 is ${price5:,}") # Comma Separator For Larger Values like for values in Thousands and Millions etc.
price6 = -4876.987
print(f"Price6 is ${price6:^}") # Center Align
price7 = 3.7890
print(f"Price7 is ${price7:+}") # Usage of Plus Sign for Indicating a Positive Value
price8 = 21435.00
print(f"Price8 is ${price8: }") # Here, after the Colon, there is an empty single space which means to insert a space before positive numbers
price9 = 234.9456
print(f"Price9 is ${price9:=}") # Place Sign To Leftmost Position
price10 = -4.76543
print(f"Price10 is ${price10:>}") # Right Justify

#Format Specifiers can also be used together
print(f"Price5 is ${price5:+,.3f}")