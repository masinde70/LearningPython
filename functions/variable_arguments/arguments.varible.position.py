def minmum(*n):
    #print(n) #n is a tuple
    if n: #Explained after the code
      mn = n[0]
      for value in n[1:]:
          if value < mn:
             mn = value
      print(mn)

minmum(1, 3, -7, 9) #n = (1, 3, -7, 9) - prints: -7
minmum()  #n = () - prints: nothing