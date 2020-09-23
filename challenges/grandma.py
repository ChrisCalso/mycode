#!/usr/bin/env python3

room =['mug', 'plate', 'forks']
count = 0
for dish in room:
    count +=1
    print(f'You left your {dish} in your room')

       
print(f"I'm going to whoop your ass {count} times")

#For every [light] I find in an empty [room] I'm going to take a [dollar]

lights = ['light on', 'light off', 'light off', 'light on']

dollars = 5
print(f"\nGrandma is about to start her rounds, you have ${dollars} so far, she'll be taking one dollar when the light is turned on")
for bulb in lights:
    if bulb =="light on":
        dollars=-1
        print(f"That's another light, You now have ${dollars}!")

report_card = ['a', 'b', 'c', 'f', 'f', 'd', 'b','f']
snakes = 0;
print(f'\nSo far there are {snakes} in your bed, lets see how that changes once grandma looks at your report card!')


