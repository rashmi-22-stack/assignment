# part 1:--

##1. variable for every player
a = 'Ruud Gullit'    
b = 'Marco van Baston'

## 2. variable for each minute scored
goal_1 = '1st in 32'
goal_2 = '2nd in 54'

## 3. using + oprater
scorers = a + goal_1 , b + goal_2
print(scorers)

## 4. using f.strings or + operator

report = a +" "+ "scored " + goal_1 +"nd minute."+"\n"+ b +" "+ "scored" + " "+ goal_2+"th minute."
print(report)



##  part 2 :--

# 1. 
player = "Ruud Gullit"

# 2.
first_name = player[:player.find(" ")]
print(first_name)

# 3.
last_name = player[player.find(" "):]
print(last_name)

# 4. 
name_short = (first_name[0]+"."+" "+last_name)
print(name_short)

# 5.  
print(len(first_name))
x = len(first_name)
chant = first_name+'!'
print((chant)*x)

# 6.
good_chant = chant + " "
print(good_chant)
print(good_chant != chant)

