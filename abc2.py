num=int(input("how many terms?"))
n1,n2= 0,1
count = 0
if num<=0:
    print("please enter a positive integer")
elif num == 1:
    print("fibonnaci number upto",num,":")
    print(n1)
else:
    print("fibonnaci sequence:")
    while count < num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2= nth
        count += 1

<!---
Vikashdwivedi123/Vikashdwivedi123 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
