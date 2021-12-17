a = [20,39,45,57,65,45,5,46,57,53,454]
b = [11,22,33,44,55]
# print(a);
# print(a[0]);
# print(a[2]);
# print(a[8]);
# print(a[0 : ]);
# print(a[ : ]);
# print(a[1 : 8]);
# print(a[-5 : -1]);
# print(a[-8 : ]);
# print(a[2 : -1]);


a.append(1);
print(a);

a.append([5,6,7,8,9]);
print(a);

a.append(b);
print(a);

a.extend(b);
print(a);