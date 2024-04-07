# nested loops = the "inner loop" will finish all iterations before finish
# one iteration of the outer loop.

#game Symbols by rows/ columns

rows = int(input("enter how many rows : "))
columns = int(input("enter how many columns : "))
symbol =  input("enter how many columns : ") # @ $  % &

for i in range(rows): #2 #1 #2
   for k in range(columns): #2
      print(symbol, end="") # #
   print()  # new-line