
# def add(a=0,b=0):
#     return a+b
# def add(a=0,b=0,c=0):
#     return a+b+c+2

# print(add())

# def msg(*argv,**kwargs):
#     for arg in argv:
#         print(arg,type(argv))
#         print(kwargs,type(kwargs))

# msg("Hello","Kese","HO",abc=1,xyz=2)

def msglist(*args):
    print(args,type(args))
    print(args[0][0])
   
l1=["Hello","Kese","Ho"]
msglist(l1)