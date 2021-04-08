from .models import question,answers,category,user_n,aptitude
from django.db.models import Q
import pandas as pd
def verb(a):
    cat_tag_v=category.objects.filter(category="Verbal ability")
    i=0
    q_n={}
    for cat in cat_tag_v:
        q_n[i]=question.objects.filter(cat_tag=cat)
        i+=1
    global cat_v
    global count
    count=0
    cat_v=0
    for j in range(len(q_n)):
        for q in q_n[j]:
            c1=Q(email=a.email)
            cat=answers.objects.filter(email=a.email).filter(q_no=q)
            count+=answers.objects.filter(email=a.email).filter(q_no=q).count()
            for caa in cat:
               cat_v+=caa.marks
    return cat_v*100/count
def quant(a):
    cat_tag_v=category.objects.filter(category="Quantitative ability")
    i=0
    q_n={}
    for cat in cat_tag_v:
        q_n[i]=question.objects.filter(cat_tag=cat)
        i+=1
    global cat_v
    cat_v=0
    global count
    count=0
    for j in range(len(q_n)):
        for q in q_n[j]:
            c1=Q(email=a.email)
            cat=answers.objects.filter(email=a.email).filter(q_no=q)
            count+=answers.objects.filter(email=a.email).filter(q_no=q).count()
            for caa in cat:
               cat_v+=caa.marks
    return cat_v*100/count
def logic(a):
    cat_tag_v=category.objects.filter(category="Logical ability")
    i=0
    q_n={}
    for cat in cat_tag_v:
        q_n[i]=question.objects.filter(cat_tag=cat)
        i+=1
    global cat_v
    global count
    count=0
    cat_v=0
    for j in range(len(q_n)):
        for q in q_n[j]:
            c1=Q(email=a.email)
            cat=answers.objects.filter(email=a.email).filter(q_no=q)
            count+=answers.objects.filter(email=a.email).filter(q_no=q).count()
            for caa in cat:
               cat_v+=caa.marks
    return cat_v*100/count 
def up():
    user_mode=user_n.objects.filter(email='mode@gmail.com')
    if(user_mode.exists()):
        return 0
    else:
        use=user_n(email='mode@gmail.com',name='mode',dept='mode',spl_b=1,isadmin=False)
        use.save()
        test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/aptitude_test.csv")
        i=16
        tests=test.loc[i]
        for j in range(65):  
            userss=answers(email=user_n.objects.get(email='mode@gmail.com'),spl_id=1,q_no=question.objects.get(q_no=j+1),marks=float(tests[j+8]))
            userss.save()
    return 0
def mode():
    global mark
    mark=0
    mod=answers.objects.filter(email='mode@gmail.com')
    for mo in mod:
        mark+=mo.marks
    return mark
def inter(a):
    mod=answers.objects.filter(email='mode@gmail.com')
    use=answers.objects.filter(email=a.email)
    global i
    i=0
    for mo in mod:
        for us in use:
            if(mo.q_no.q_no==us.q_no.q_no):
                if(mo.marks==us.marks and mo.marks==1):
                    i+=1
                break
    return i
