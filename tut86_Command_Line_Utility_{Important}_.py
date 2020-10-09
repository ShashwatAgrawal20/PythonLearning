# Making of Command Line Utility!!!!!!

# (Ye maiko smj me aaya hai jaruri nhi hai ki aaisa hi honga iss ka mtlb)Command line means jaise powershell me aapan kaise pip likhte hai to vo aapne ko dialog box dikhata hai . vo jo aata hai --v vgere vo sb hota hai command line utility.. bhot kam ka hai ye .. important hai ye .. video ek aur bar dheke.. 

# we can read command line Utility using different softwares


# ye jo agrparse module hai ye command line utility banane kye lye use hota hai ..

# ye jo sys hai ye command line pr print kr ne ke kam aata hai ye .. 
import argparse
import sys

def calc (agrs):
    if agrs.o == 'add':
        return agrs.s + agrs.a
    elif agrs.o == 'mul':
        return agrs.s * agrs.a
    elif agrs.o == 'sub':
        return agrs.s - agrs.a
    elif agrs.o == 'div':
        return agrs.s / agrs.a
    else:
        return"Something went wrong "
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', type=float, default=1.0, help="Enter the first number or Costumer care number")


    parser.add_argument('--a', type=float, default=3.0, help="Enter the second nubmer or Costumer care number")


    parser.add_argument('--o', type=str, default="add", help="This is a command line utility if you had any problem call Costumer care number")


args = parser.parse_args()
sys.stdout.write(str(calc(args)))