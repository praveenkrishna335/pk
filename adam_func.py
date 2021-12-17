def square(num):
    sq = 0;
    sq = sq + (num ** 2);
    return sq
def rev(sq):
    reverse = 0;
    while (sq > 0) :
        reverse = (reverse * 10) + (sq % 10)
        sq //= 10;
    return reverse
def root(reverse):
    sqrt = int(reverse ** (1/2));
    return sqrt
num = int(input("Enter the number to check : "));

squa = square(num)
print(squa)
rever = rev(squa)
print(rever)
rt = root(rever)
print(rt)
ans = rev(rt)
print(ans)