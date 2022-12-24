salary=int(input("Enter salary"))
msalary=salary/12
basic=msalary/2
hra=basic/2
med_all=1250
balance=msalary-(basic+hra+med_all)
bonus=int(input("press 1 for bonus\n press 0 for no bonus"))
if bonus==0:
    a1=balance/5
    a2=balance/4
    a3=(2*balance)/5
    a4=(3*balance)/20
    print(basic,hra,med_all,a1,a2,a3,a4)
else:
    a1=balance/5
    a2=balance/4
    a3=balance/5
    a4=(3*balance)/20
    bonus=balance/5
    print(basic,hra,med_all,a1,a2,a3,a4)
