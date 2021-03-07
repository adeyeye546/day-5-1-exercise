# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# for heights in student_heights:
#   print(heights)
# print(student_heights)
# # print(heights)

# newheight0 = student_heights[0]
# newheight1 = student_heights[1]
# newheight2 = student_heights[2]
# newheight3 = student_heights[3]
# newheight4 = student_heights[4]

# totalheight = (newheight0 + newheight1 + newheight2 + newheight3 + newheight4) / 5

# print(f"Your average height is {round(totalheight)}") 

total_heights = 0
for height in student_heights:
  total_heights = total_heights + height
# print(total_heights)

number_of_students = 0
for student in student_heights:
  number_of_students = number_of_students + 1
# print(number_of_students)

average_height = round(total_heights/number_of_students)

print(average_height)


