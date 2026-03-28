meals = ('carrywurst', 'pommes', 'salat', 'pizza', 'schnitzel')

#

for meal in meals:
    print(meal)

# 

# meals[0] = 'wurst' # TypeError: 'tuple' object does not support item assignment

# 

meals = ('wurst', 'pommes', 'salat', 'hamburger', 'schnitzel')

for meal in meals:
    print(meal)