#1.After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

#Using for loop figure out how many times you got heads
count=0
for i in result:
    if i=='heads':
        count=count+1
print("count of heads:",count)

#2.Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)

#3.Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount
# program should tell you in which month that expense occurred. 
# If expense is not found then it should print that as well.

month=['jan','feb','march','april','may']
expense_list = [2340, 2500, 2100, 3100, 2980]
amount=int(input("enter your month expense_amount:"))
m=-1
for i in range(len(expense_list)):
    if amount==expense_list[i]:
        m=i
        break
if m!=-1:
    print(f'You spent {amount} in {month[m]}')
else:
    print(f'You didn\'t spend {amount} in any month')

# 4. Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    print(f"you completed {i}km")
    tired=input("Are you tired:")
    if tired=='yes':
        break
if i==5:
    print("Hurray!! Congratualtions You completed 5km race")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i}km")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)