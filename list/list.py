#1.Let us say your expense for every month are listed below,
"""January - 2200
February - 2350
March - 2600
April - 2130
May - 2190"""
#Create a list to store these monthly expenses and using that find out
exp=[2200,2350,2600,2130,2190]

#1. In Feb, how many dollars you spent extra compare to January?
print("dollars you spent extra in feb compared to jan:", exp[1]-exp[0])

#2.Find out your total expense in first quarter (first three months) of the year.
print("total expense in first quater(first 3 months):",exp[2]+exp[1]+exp[0])

#3.Find out if you spent exactly 2000 dollars in any month
print("did i spend 2000 in amy month",2000 in exp)

#4.June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("exp after adding june expense into the list",exp)

#5.You returned an item that you bought in a month of April andgot a refund of 200$. 
# Make a correction to your monthly expense list based on this
exp[3] = exp[3]-200
print("corrected mothly expense list:",exp)


#2.You have a list of your favourite marvel super heros.
#heros=['spider man','thor','hulk','iron man','captain america']
#Using this find out,

heros=['spider man','thor','hulk','iron man','captain america']

#1. Length of the list
length=len(heros)
print("length of the list:",length)

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print("heros list:",heros)

#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print("heros list after adding black panther after hulk:",heros)

#4. Now you don't like thor and hulk because they get angry easily :)
#  So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#  Do that with one line of code.
heros[1:3]=['doctor stranger']
print("modified list:",heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("sorted by alphabetical order:",heros)
print(dir(heros))