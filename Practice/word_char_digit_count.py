
# #! for loop

s="Kanji@12309"
u=""
l=""
d=""
sym=""

uc=lc=dc=symc=0


for i in s:
    if 'a'<=i<='z':
        l=l+i
        lc+=1
    elif 'A'<=i<='Z':
        u=u+i
        uc+=1
    elif '0'<=i<='9':
        d=d+i
        dc+=1
    else:
        sym=sym+i
        symc+=1

result=(u,uc,l,lc,d,dc,sym,symc)
u,uc,l,lc,d,dc,sym,symc=result
result = {
    "uppercase": (u, uc),
    "lowercase": (l, lc),
    "digits": (d, dc),
    "symbols": (sym, symc)
}

print(result)

# #! using while loop

# s="Kanji@12309"
# u=""
# l=""
# d=""
# sym=''
# i=0
# uc=lc=dc=symc=0

# while i <len(s):
#     if 'a'<=s[i]<='z':
#         l=l+s[i]
#         lc+=1

#     elif 'A'<=s[i]<='Z':
#         u=u+s[i]
#         uc+=1
#     elif '0'<=s[i]<='9':
#         d=d+s[i]
#         dc+=1
#     else:
#         sym=sym+s[i]
#         symc+=1
#     i+=1
# result=(u,uc,l,lc,d,dc,sym,symc)
# u,uc,l,lc,d,dc,sym,symc=result

# print(result)

# s = "Kanji@12309"

# u = ""
# l = ""
# d = ""
# sym = ""

# uc = lc = dc = symc = 0

# for i in s:
#     if 'a' <= i <= 'z':
#         l += i
#         lc += 1
#     elif 'A' <= i <= 'Z':
#         u += i
#         uc += 1
#     elif '0' <= i <= '9':
#         d += i
#         dc += 1
#     else:
#         sym += i
#         symc += 1

# result = {
#     "uppercase": (u, uc),
#     "lowercase": (l, lc),
#     "digits": (d, dc),
#     "symbols": (sym, symc)
# }

# print(result)

