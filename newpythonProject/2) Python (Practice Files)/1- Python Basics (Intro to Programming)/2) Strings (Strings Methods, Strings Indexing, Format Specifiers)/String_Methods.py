                                                                                    #  (String 1- 10) Functions and 9- Decorators & Arguments (Multiple Positional & Keyword Arguments) / String Methods) in Python
# (1) Capitalize  Method => .capitalize()
# Description: Only the first letter of the first word is capitalized out of the whole string. It does not change the original string.
name2 = input ("Enter the Name to Make it Capitalized: ")
capital = name2.capitalize()
print(f"Your Name After Being Capitalized: {capital}")

# (2) Title Method => .title()
# Description: It converts first letter of each word in a string to upper case. It does not change the original string.
text1 = 'My favorite number is 25.'
print(text1.title())
text2= '234 k3l2 *43 fun'
print(text2.title())
# title () capitalizes the first letter after apostrophes as well.
text = "He's an engineer, isn't he?"
print(text.title())

# (3) Upper Method => .upper()
# Description: Whole String is converted into Upper Case Letters
name3 = input ("Enter the Name to Make it Upper Case: ")
uppercase = name3.upper()
print(f"Your Name After Being UpperCased: {uppercase}")

# (4) Lower Method => .lower()
# Description: Whole String is converted into Lower Case Letters
name4 = input ("Enter the Name to Make it Lower Case: ")
lowercase = name4.lower()
print(f"Your Name After Being LowerCased: {lowercase}")
# (5) CaseFold Method => .casefold()
# Description: Its an aggressive lower method

# (6) SwapCase Method => .swapcase()



# (7) IsUpper Method => .isupper()

# (8) IsLower Method => .islower()

# (9) IsTitle Method => .istitle()
# It will return (True if the string is a title cased string) and (False if the string is not a title cased string or an empty string).
s = 'Python Is Good.'
print(s.istitle())
s = 'Python is good'
print(s.istitle())
s = 'This Is @ Symbol.'
print(s.istitle())
s = '99 Is A Number'
print(s.istitle())
s = 'PYTHON'
print(s.istitle())

# (10) IsDigit Method => .isdigit()
name5 = input ("Enter the Name For Digits Checking using isdigit(): ")
digitChecking = name5.isdigit()
print(f"For Digits Checking: {digitChecking}")

# (11) IsDecimal Method => .isdecimal()

# (12) IsNumeric Method => .isnumeric()

# (13) IsAlpha Method => .isalpha()
name6 = input ("Enter the Name For Alphabets Checking using isalpha(): ")
alphabetsChecking = name6.isalpha()
print(f"For Alphabets Checking: {alphabetsChecking}")

# (14) IsAlNum Method => .isalnum()

# (15) IsSpace  Method => .isspace()
# Characters that are used for spacing are called whitespace characters. For example: tabs, spaces, newline, etc.
# isspace() method returns True if all characters in the string are whitespace characters and False if the string is empty or contains at least one non-printable character
s = '\n      \t'
print(s.isspace())
s = ' a '
print(s.isspace())
s = ''
print(s.isspace())

# (16) Find Method => .find()
# For find(), the function will return the character's first occurrence index and if not found then will return -1 as a value
name7 = input ("Enter the Name to find First Occurrences of White Space and Alphabet (i) using find(): ")
search1 = name7.find(" ")
print(f"White Space First Occurrence Found At Index: {search1}")
search2 = name7.find("i")
print(f"Alphabet's First Occurrence Found At Index: {search2}")

# (17) Reverse Find Method => .rfind()
# For rfind(), the function will return the character's first reverse occurrence index (Reading the String in Reverse Order)  and if not found then will return -1 as a value
name8 = input ("Enter the Name to Reverse Find First Occurrence Using rfind(): ")
reverse_search = name8.rfind("i")
print(f"Alphabet's First Reverse Occurrence Found At Index: {reverse_search}")

# (18) Index Method => .index()

# (19) Reverse Index Method => .rindex()

# (20) Replace Method => .replace()
replacing = input ("Enter Any Text Or Phone Number For Replacing Purposes:  ")
replaced = replacing.replace("-","")
print(f"After Replacing the Asked Character:  {replaced}")

# (21) Count Method => .count()
# Here the count method will count the total number of whitespaces
counter = input ("Enter Any Textual Data To Count it Using count(): ")
counted = counter.count(" ")
print(f"After Counting the Asked Character, The Count Is: {counted}")

# (22) Split Method => .split()
# To break a string into smaller strings (sub-strings) based on a separator (Like Colon is a Separator Below), we use split()
time = "1:19:48"
parts = time.split(":")
print(parts)

# (23) Reverse Split Method => .rsplit()

# (24) Splitlines Method => .splitlines()

# (25) Strip Method => .strip()
# It returns a copy of the string with leading and trailing whitespaces (spaces, tabs, and newlines) removed

# (26) Left Strip Method => .lstrip()

# (27) Right Strip Method => .rstrip()

# A) Remove newline characters from a string
string = "\nHello, World!\n"
new_string1 = string.strip()
print(new_string1)
# B) Remove spaces/tabs from a string
string = "  Hello, World!   "
new_string2 = string.strip()
print(new_string2)

# (28) StartsWith Method => .startswith()

# (29) EndsWith Method => .endswith()

# (30) Join Method => .join()

# (31) Format Method => .format()

# (32) Format_Map Method => .format_map()

# (33) ZFill Method => .zfill()





# print(help(str)) # It will display some string methods etc. because we have asked for help for string class