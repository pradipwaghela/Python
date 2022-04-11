"""
The test has a total of N questions, each question carries 3 marks for a correct answer and −1 for an incorrect answer. 
The chef is a risk-averse person so he decided to attempt all the questions. 
It is known that Chef got X questions correct and the rest of them incorrect. 
For Chef to pass the course he must score at least P marks.
*Input
Will Chef be able to pass the exam or not?
First-line will contain T number of test cases. Then the test cases follow.
Each test case contains a single line of input, three integers N,X,P
*Output format 
For each test case output "PASS" if Chef passes the exam and "FAIL" if Chef fails the exam
.Note:- Use function passfail() which takes 3 arguments n,x,p and returns whether PASS or FAIL
"""
def passfail(tq,cq,pm):
    icq=tq-cq
    marks=(cq*3) - icq
    if (marks>=pm):
        print("PASS")
    else:
        print("FAIL")

test=int(input("Enter How many test ?"))
print(test)
for i in range(test):
    print("Enter total questions correct answer and passing marks (5 2 3)") 
    (tq,cq,pm)=map(int,input().split(' '))
    passfail(tq,cq,pm)

"""
Submission
def passfail(tq,cq,pm):
    icq=tq-cq
    marks=(cq*3) - icq
    if (marks>=pm):
        print("PASS")
    else:
        print("FAIL")

test=int(input())
print(test)
for i in range(test): 
    tq,cq,pm=input().split()
    passfail(int(tq),int(cq),int(pm))

"""