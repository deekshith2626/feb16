year = int(input("enter a year: "))
def is_leap(year):
    if(year%4==0) and (year%1==0):
        return True


    return False


if is_leap(year):
    print("it is an leap year")
else:
    print("it is not a leap year")
   
