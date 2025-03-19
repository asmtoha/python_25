def check_first():
    print("check_first() called")
    return False

def check_second():
    print("check_second() called")
    return True

if check_first() and check_second():
    print("Both conditions are True")
else:
    print("At least one condition is False")