lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, False, True, False, False]
tup = (1, 2, 3, 4, 5, 6, 7, "masinde", 45)
for i, element in enumerate(tup):
   if element == "masinde" or element == 7:
      break
   print(i, element)

print("Done!")