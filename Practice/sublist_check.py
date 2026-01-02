
#! using for loop
main_list = [1, 2, 3, 4, 5]
sub_list = [2,3,4]

flag=True

for i in sub_list:
    if i not in main_list:
        flag=False
        break

if flag:
    print("sub list")
else:
    print("not a sublist")

#! using while loop

main_list = [1, 2, 3, 4, 5]
sub_list = [6,7,8,9]

flag=True
i=0

while i<len(sub_list):
    if sub_list[i] not in main_list:
        flag=False
        break
    i+=1
if flag:
    print("sub list")
else:
    print("not a sublist")
