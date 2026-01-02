# #write nd writelines:-
# fo=open("pro.txt",'w')
# fo.write("hii, my name is kanji barad")
# fo.close()

# fo=open("pro.txt",'w')
# fo.writelines(["good\n",'badin\n','inugly'])
# fo.close()

# fo=open('pro.txt','r')
# res=fo.read()
# print(res)
# fo.close()

# fo=open('pro.txt','r')
# res=fo.readlines()
# print(res)
# fo.close()

# fo=open('pro.txt','r')
# res=fo.readline()
# print(res)
# fo.close()

#append file:-

# fo=open('pro.txt','a')
# fo.write("\nwe are appending")
# fo.close()

# import csv

# from urllib3.filepost import writer

# fo=open('emp.csv','w')
# f1=csv.writer(fo)
# f1.writerow(['ename','sal'])
# f1.writerow(['kanji',20000])
# fo.close()

# fo=open('emp.csv','r')
# f1=csv.reader(fo)
# print(list(f1))
# fo.close()

