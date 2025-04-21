language = input("Which is Your Favourite Programming Language (Dart / Javascript / Python / Solidity: ")
language = language.upper()
# Implementation 1 (if-elIf-else)
if language == "DART":
    print("My Favourite Programming Language is Dart!")
elif language == "JAVASCRIPT":
    print("My Favourite Programming Language is Javascript!")
elif language == "PYTHON":
    print("My Favourite Programming Language is Python!")
elif language == "SOLIDITY":
    print("My Favourite Programming Language is Solidity!")
else:
    print("My Favourite Programming Language is None!")

# Implementation 2 (Conditional Expression)
# language = "OK None!"  if language == "" else print("Lazy Programmer")
# print(language)

# Implementation 3 (match case Statement)
match language:
    case "SOLIDITY":
        print("Programming Language is Solidity!")
    case "PYTHON":
        print("Programming Language is Python!")
    case "DART":
        print("Programming Language is Dart!")
    case "JAVASCRIPT":
        print("Programming Language is Javascript!")
    case _:
        print("Selected None!")