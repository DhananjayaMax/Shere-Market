import os
import sys
from time import sleep

f=""" 
   _____ __  ____________  ______         
  / ___// / / / ____/ __ \/ ____/         
  \__ \/ /_/ / __/ / /_/ / __/            
 ___/ / __  / /___/ _, _/ /___            
/____/_/_/_/_____/_/_|_/_____/____________
   /  |/  /   |  / __ \/ //_// ____/_  __/
  / /|_/ / /| | / /_/ / ,<  / __/   / /   
 / /  / / ___ |/ _, _/ /| |/ /___  / /    
/_/  /_/_/  |_/_/ |_/_/ |_/_____/ /_/     
                                          
"""

def b():
  os.system('clear')
  for x in f :
    print(x, end="")
    sys.stdout.flush()
    sleep(0.002)
def main():
   inw=float(input("Enter Your Invesment Money : "))
   print ("")
   sh=float(input("price Of shere  : "))
   print ("")
   ib=float(input("Enter The Profitable Amount : "))
   print ("")
   k=inw/sh
   print ("Number Of Shere Is : ",k)
   p=k*ib
   print ("Profitble Money Is : ",p)
   z=float(input("Enter The Sale Price Of Shere : "))
   print ("")
   d=z-sh
   j=d*k
   print ("Capital Profit Is : ",j)
   print ("")
   l=j/inw
   o=l*100
   print ("Precentage Of Capital Profit  \n \t\t out of inwesment : ",o)
   print ("")
   q=p/inw
   u=q*100
   print ("Precentage of profitable Money \n\t\t out of inwesment : ",u)
   print ("")
b()
main()
