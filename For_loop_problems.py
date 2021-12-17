#FOR loop for EVEN numbers
for i in range(0, 10):
    if (i % 2 == 0):
        print(i);

# FOR loop for ODD numbers
for i in range(0, 10):
    if (i % 2 != 0):
        print(i);

# FOR loop for SUM & AVG
sum = 0;
for i in range(0, 10):
    print(i);
    sum = sum + i;
print("The total is : ", sum);
avg = sum / 10;
print("The average of sum is : ", avg);