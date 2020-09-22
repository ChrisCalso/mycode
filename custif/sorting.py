#!/usr/bin/env python3

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer1 = input("You've made it to  Hogwarts, which means you've already bought a wand from Ollivander's. What material is at it's core? \na)Phoenix Feather \nb)Dragon Heartstring \nc)Unicorn Hair")

if answer1 == "a":
  gryffindor += 1
elif answer1 == "b":
  ravenclaw += 1
elif answer1 == "c":
  hufflepuff += 1
elif answer1 == "d":
  slytherin += 1
else:
  print("Invalid answer please use lower case letters")

answer2 = input("During the end-of-year exams, you notice that one of your classmates was using an enchanted quill. You come top of the class anyway, but they are second. What do you do? \na)Tell the professor immediately - cheating is wrong, no matter what. \nb) Nothing, but if I hadn't come top of the class,I'd definitely tell the professor. \nc)Encourage the other student to admit what they'd done to the professor. \nd)Give them a high five for managing to sneak the quill into the exam.")
	
if answer2  == "a":
    gryffindor = gryffindor + 1
elif answer2 == "b":
     hufflepuff +=1 
elif answer2 =="c":
    ravenclaw +=1
elif answer2  =="d":
    slythering +=1



if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("GRYFFINDOR!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
   print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("SLYTHERIN!!!!!!")

