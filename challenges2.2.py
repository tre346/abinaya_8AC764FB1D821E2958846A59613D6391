def Isleapyear(year):
  if (year / 4 == 0 and year / 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
year = int(input("Enter the year:"))
if Isleapyear(year):
  print("{} Is a leapyear".format(year))
else:
  print("{} Is not a leapyear".format(year))