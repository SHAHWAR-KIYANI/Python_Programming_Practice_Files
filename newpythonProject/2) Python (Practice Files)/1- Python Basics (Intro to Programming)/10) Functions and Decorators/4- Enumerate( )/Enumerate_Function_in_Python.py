# # Explanation: Here for index value, we are managing the counter variable because through loop we can only get the value not index.
# list_of_RGBColors = ["Red","Green","Blue"]
# index = 0
# for colorValue in list_of_RGBColors:
#     print(f"Color at Index: {index} is {colorValue}")
#     index += 1
#
# # This issue can be solved using Enumerate() Function.
# # It will return a tuple containing both index and value which will be unpacked for further use.
# list_of_RGBColors = ["Red", "Green", "Blue"]
# for index, colorValue in enumerate(list_of_RGBColors):
#     print(f"Color at Index: {index} is {colorValue}")


list_of_RGBColors = ["Red","Green","Blue"]
for index, color in enumerate(list_of_RGBColors):
    print(index, color)