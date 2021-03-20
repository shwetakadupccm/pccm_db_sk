import calendar


yyyy= 2021
mm = 1

obj = calendar.Calendar() 
  
# iteratign with itermonthdates 
for day in obj.itermonthdates(2021, 1): 
    print(day) 
