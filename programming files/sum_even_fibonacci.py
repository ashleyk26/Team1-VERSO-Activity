a, b = 0, 1
sum_even = 0
# Only sum fibonacci values up to 4,000,000
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
