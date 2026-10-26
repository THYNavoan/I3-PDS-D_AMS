#Problem2
#purple is function
#blue is variable
#yellow is object

total_seconds = 60434
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = (total_seconds % 3600) % 60 

print("===========================================")
print(hour,"hour",minute,"minute",second,"second")

#Check return value of the time (==) check it is true or false

(hour * 3600) + (minute * 60) + second == total_seconds
print("Check the statement:",(hour * 3600) + (minute * 60) + second == total_seconds)
print("===========================================")