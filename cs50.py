from datetime import date
import inflect
import re
import sys

'''
calulate the age in minutes

ask the user for input in YYYY-MM-DD, else raise exception

prints how old are they in minutes to the nearest  integer in english

midnight to midnight'''
def main():
  print(cal_age(input("enter your dob : ")))

def cal_age(pr) :
  if len(pr.split('-')) !=3:
      sys.exit("invalid date")
  else:
      yr,mn,day= pr.split('-')

  age = date(int(yr), int(mn), int(day)) - date.today()
  mins= -int (age.days) * 24 * 60
  inf = inflect.engine()
  min_words = inf.number_to_words(mins)

  min_words = min_words.replace(' and','').capitalize()

  return min_words + ' minutes'

if __name__ ==  "__main__":
   main()