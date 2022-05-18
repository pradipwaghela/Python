from turtle import *
Screen()
bgcolor("white")

fillcolor("#ffffff")
begin_fill()
tracer(False)
a=2.5
for i in range(120):
    if 0<= i <= 30 or 60 <=i <=90:
        a-=0.05
        lt(3)
        fd(a)
    else:
        a+=0.05
        lt(3)
        fd(a)
tracer(True)
end_fill()


done()