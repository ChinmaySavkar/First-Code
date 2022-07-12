My_age = int(input("What is your age? "))
Age_at_elementary_school = 6
Age_at_middle_school = 12
Age_at_high_school = 15
Age_at_college = 18

if My_age >= Age_at_elementary_school and My_age < Age_at_middle_school:
    print('You should be in Elementary School')
elif My_age >= Age_at_middle_school and My_age < Age_at_high_school:
    print('You should be in Middle School')
elif My_age >= Age_at_high_school and My_age <= Age_at_college:
    print('You should be in High School')
elif My_age >= Age_at_college:
    print('You should be in College')
elif My_age < 0:
    print('Age cannot be negative')
else:
    print('You are not in school yet')
