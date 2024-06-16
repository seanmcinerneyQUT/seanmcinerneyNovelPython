monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91,3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
Sem1=0.0
Sem2=0.0
S=0.0
for i, amount in enumerate(monthly_spending):
    if i < 6:
        Sem1+=amount
    else:
        Sem2+=amount
    S+=amount
Sem1avg=Sem1/6
Sem2avg=Sem2/6
print("Semester 1 average: $"+str(round(Sem1avg,2)))
print("Semester 2 average: $"+str(round(Sem2avg,2)))
if S == Sem1 + Sem2:
    print("check is good")
else:
    print("check is no good, total was meant to be: "+str(S))