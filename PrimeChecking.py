import time
while(True):
 print("How many numbers do you want until the machine stops?")
 a = input("")
 print("How many times do people need to wait to the script to occur again?")
 b = input("")
 # import time is to make the script slower
 for n in range(1,int(a)):
   time.sleep(int(b)) #() = the amount of seconds you want to occur the script
   if n > 1:
      for i in range(2,n):
          if (n % i) == 0: #checks the number
              print(n,"= Not Prime. explain:") #non-prime explain
              print(i,"times",n//i,"is",n)
              break
      else:
          print(n,"Prime.") #prime explain
   else:
      print(n,"Not Prime.") #non-prime explain
   n
