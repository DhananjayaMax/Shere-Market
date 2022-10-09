import os
import sys
from time import sleep

f="""\33[91m 
░██████╗██╗░░██╗███████╗██████╗░███████╗
██╔════╝██║░░██║██╔════╝██╔══██╗██╔════╝
╚█████╗░███████║█████╗░░██████╔╝█████╗░░
░╚═══██╗██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
██████╔╝██║░░██║███████╗██║░░██║███████╗
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝


███╗░░░███╗░█████╗░██████╗░██╗░░██╗███████╗████████╗
████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
██╔████╔██║███████║██████╔╝█████═╝░█████╗░░░░░██║░░░
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██╔══╝░░░░░██║░░░
██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗███████╗░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░"""


def b():
  os.system('clear')
  for x in f :
    print(x, end="")
    sys.stdout.flush()
    sleep(0.002)
def main():
   print ("")
   print ("")
   print ("")
   inw=float(input("\33[91m[\33[93m+\33[91m]\33[95m Enter Your Invesment Money : \33[93mRs -> \33[92m "))
   print ("")
   sh=float(input("\33[91m[\33[93m+\33[91m]\33[95mprice Of shere  : \33[93mRs -> \33[92m "))
   print ("")
   ib=float(input("\33[91m[\33[93m+\33[91m]\33[95m Enter The Profitable Amount : \33[93mRs -> \33[92m "))
   print ("")
   k=inw/sh
   print ("\33[91m[\33[93m+\33[91m]\33[95m Number Of Shere Is : \33[93mRs -> \33[92m ",k)
   p=k*ib
   print ("")
   print ("\33[91m[\33[93m+\33[91m]\33[95m Profitble Money Is : \33[93mRs -> \33[92m ",p)
   print ("")
   z=float(input("\33[91m[\33[93m+\33[91m]\33[95m Enter The Sale Price Of Shere : \33[93mRs -> \33[92m "))
   print ("")
   d=z-sh
   j=d*k
   print ("\33[91m[\33[93m+\33[91m]\33[95m Capital Profit Is : \33[93mRs -> \33[92m ",j)
   print ("")
   l=j/inw
   o=l*100
   print ("\33[91m[\33[93m+\33[91m]\33[95m Precentage Of Capital Profit  \n \t\t out of inwesment :\33[91m ",o,"\33[93m%")
   print ("")
   q=p/inw
   u=q*100
   print ("\33[91m[\33[93m+\33[91m]\33[95m Precentage of profitable Money \n\t\t out of inwesment \33[91m: ",u,"\33[93m%")
   print ("")
b()
main()
