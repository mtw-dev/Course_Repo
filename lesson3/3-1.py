
# If Else


age = 17

if age >= 18:
    print("Your an adult")
else:
    print("Too young")


print("This line always runs")

# Nested

is_logged_in = True
is_admin = False

if is_logged_in:
    print("User logged in")
    if is_admin:
        print("show admin panel")
    else:
        print("show regular")
else:
    print("redirect login page")

# Else if

score = 82

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


#comparison operators

a = 10
b =3

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

# Boolean operators

is_member = True
purchase_total = 120

if is_member and purchase_total >= 100:
    print("Discount applies")
else:
    print("No discount")

has_coupon = False
is_vip = True

if has_coupon or is_vip:
    print("discount applies")
else:
    print("no discount")

is_locked = False

if not is_locked:
    print("you can open the door")
else:
    print("the door is locked")


