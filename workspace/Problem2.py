def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

test_numbers = [15, -7, 0, 42.5, -18.2]
print("Number Classification Check:")
print("=" * 35)
for num in test_numbers:
    result = check_number(num)
    print(f"Number: {num:>6} -> {result}")
