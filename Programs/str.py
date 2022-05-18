str1="My name is Lala"
print(len(str1))
strl=len(str1)
rstr=strl
type(rstr)
for i in range(strl):
    print("str1[{0}]=  {1}  =str1[-{2}]".format(i,str1[i],rstr))
    rstr-=1
print(str1[0::2])
print(str1[::-2])