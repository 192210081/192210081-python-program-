def calculate_users(total_users, staff_users):
    # Calculate student users
    student_users = total_users - staff_users

    # Calculate non-teaching staff users
    non_teaching_staff_users = staff_users // 3

    return student_users, non_teaching_staff_users

# Sample input
total_users = int(input("Enter the total number of users: "))
staff_users = int(input("Enter the number of staff users: "))

# Calculate the number of student users and non-teaching staff users
student_users, non_teaching_staff_users = calculate_users(total_users, staff_users)

# Output the results
print("Number of Student Users:", student_users)
print("Number of Non-Teaching Staff Users:", non_teaching_staff_users)
