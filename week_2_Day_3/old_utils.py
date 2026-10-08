# 7. Part E – Modules
# Create utils.py with small reusable functions such as:
# •	clean_name(name)
# •	calculate_average(numbers)
# •	is_valid_email(email)
def clean_name(name):
    return name.strip().title()
def calculate_average(numbers):
    total=0
    count=0
    for i in numbers:
        total=total+i
        count=count+1
    avg_marks=total/count
    return avg_marks

def is_valid_email(email):
    return "@" in email and "." in email