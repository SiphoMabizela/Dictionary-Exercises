'''
Create a dictionary representing a coding bootcamp student:
Must include:
    name (string)   
    email (string)
    course (string)
    completed_projects (list of strings)
    is_active (boolean)

Then:
1. Update the course name
2. Add a new project to the list
3. Remove the is_active key
'''

student = {
    'name': 'Sipho',
    'email': 'sipho@gmail.com',
    'course': 'Software Engineering',
    'completed_projects': ['Gilded Rose', 'Spam Detection', 'Bank', 'Uno'],
    'is_active': True
}

# 1. Update course
student.update({'course': 'Cyber-security'})

# 2. Add project
student['completed_projects'].append('Anagrams')

# 3. Remove key
student.pop('is_active', None)



# print(sorted(student.items()))
print(student)