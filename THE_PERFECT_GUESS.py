from random import randint
print("-------------------\n")
print("THE PERFECT GUESS\n")
print("-------------------\n")
com=randint(1,1000)
while True:
  n=int(input("ENTER NUMBER WHICH YOU WANT TO GUESS (PRESS ZERO IF YOU WANT TO QUIT)\n"))
 
  if(n>com):
    print("YOUR GUESS IS HIGHER\n")
  elif(n==0):
    print(f"{com}")
  elif(n<com):
    print("YOUR GUESS IS LOWER\n")
  elif(n==com):
    print("YOUR GUESS IS CORRECT\n")
    print("WINNER\n")
  
    break
  