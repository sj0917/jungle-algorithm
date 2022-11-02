A = int(input())
B = int(input())

hun_digit = B//100
ten_digit = (B - hun_digit*100)//10
unit_digit = B - hun_digit*100 - ten_digit*10

print(A*unit_digit)
print(A*ten_digit)
print(A*hun_digit)
print(A*B)