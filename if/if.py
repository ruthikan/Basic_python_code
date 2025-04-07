#1.Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#i) Write a program that asks user to enter a city name and it should tell which country the city belongs to
#ii) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#For example if I enter mumbai and chennai, it will print "Both cities are in India" 
#but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# i solution
city_name=input("enter city name:")
if city_name in india:
    print(f"the {city_name} belongs to india")
elif city_name in pakistan:
    print(f"the {city_name} belongs to pakistan")
elif city_name in bangladesh:
    print(f"the {city_name} belongs to bangladesh")
else:
    print(f"I won't be able to tell you which country {city_name} is in! Sorry!")
# ii solution
city_name1 = input("Enter city 1: ")
city_name2 = input("Enter city 2: ")
if city_name1 in india and city_name2 in india:
    print("Both cities are in india")
elif city_name1 in pakistan and city_name2 in pakistan:
    print("Both cities are in pakistan")
elif city_name1 in bangladesh and city_name2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")


#2.Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal
sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")