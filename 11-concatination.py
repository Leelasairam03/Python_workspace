#concatination- uses + operator to join 2 or more strings
#syntax: newstring="s1"+"s2"+"s3"+ .....

playername=input("enter the player name:")
age=int(input("enter the player's age:"))
average=float(input("enter the player average:"))
team=input("enter the player team:")
is_genius=eval(input("is he a genius?"))

print("player name is "+playername + " whose age is "+ str(age) + " and batting average is "+ str(average)+ " and plays for team "+team + " and he is a "+str(is_genius)+" genius ")
print()

#f strings- format method,auto convert data types,{}-placeholder should not be left empty
print(f"player name is {playername} whose age is {age} and batting average is {average}  and plays for team {team} and he is a {is_genius} genius")
print()
'''
#using .format()
print("player name is {} whose age is {} and batting average is {}  and plays for team {} and he is a {} genius".format(playername,age,average,team,is_genius))

'''
print("player name is {} whose age is {} and batting average is {}  and plays for team {} and he is a {} genius".format(playername,age,average,team,is_genius))
print()
