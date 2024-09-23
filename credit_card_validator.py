# It looks like you're working on a Python credit card validator program. Here's what the steps in the image describe:
#steps for valid credit card number

#1. Remove any dashes ('-') or spaces (' ') from the credit card number.
# 2.Add all digits in the odd places (starting from the right to left).
# 3.Double every second digit from the right, and:
# ((If the result is a two-digit number, add those two digits together to get a single-digit number.)
# step 4.Sum the totals of steps 2 and 3.
# 5.If the sum is divisible by 10, the credit card number is valid.


# This is essentially the Luhn algorithm for validating credit card numbers.

sum_odd_digits=0
sum_even_digits=0
total=0

card_number=input("Enter a credit card number:")
card_number=card_number.replace("-","")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]
print(card_number)

#step 2:
for x in card_number[::2]:
    sum_odd_digits+=int(x)
#step3
for x in card_number[1::2]:
    x=int(x)*2
    if x>=10:
        sum_even_digits+=(1+(x%10))
    else:
        sum_even_digits+=int(x)
#step4
total=sum_even_digits+sum_odd_digits

if total % 10 == 0:
    print("VALID")
else:
    print("NOT VALID")





