#Chapter 1
#How many seconds are there in 42 minutes 42 seconds?
seconds = 42*60 + 42
print('seconds: ', seconds)
#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
miles = 10*1.61
print('miles: ', miles)
#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your avarage pace (time per mile in minutes and seconds)? 
average_pace_seconds = miles / seconds
print('average_pace_seconds: ', average_pace_seconds)
minutes = 42 + (42 / 60)
average_pace_minutes = miles / minutes
print('average_pace_minutes: ', average_pace_minutes)
#What is your avarage speed in miles per hour?
hours = seconds / 3600
average_speed = miles / hours
print('average_speed: ', average_speed)
