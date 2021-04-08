from django.shortcuts import render
from django.db.models import Max
from django.http import HttpResponse
from .models import pyt,user_n,category,question,answers,aptitude,gds,interviewer
import numpy as np
import pandas as pd 
from .func import verb,quant,logic,up,mode,inter
from django.views.generic import View
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
# Create your views here.
user=user_n.objects.get(email='ravindrareddy1217@gmail.com')
users=aptitude.objects.all()
pyts=pyt.objects.get(email='ravindrareddy1217@gmail.com')
dict={}
dict= {
    'ENFJ':'Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership.',
    'ENFP': 'Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency.',
    'ENTJ': 'Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas.', 
    'ENTP': 'Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another.', 
    'ESFJ': 'Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute.', 
    'ESFP' : 'Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people.', 
    'ESTJ': 'Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans.', 
    'ESTP' : 'Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them - they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing.', 
    'INFJ' : 'Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision.', 
    'INFP': 'Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened.', 
    'INTJ': 'Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance - for themselves and others.', 
    'INTP' : 'Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical.', 
    'ISFJ' : 'Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home.', 
    'ISFP' : 'Quiet, friendly, sensitive, and kind. Enjoy the present moment, what\'s going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others.', 
    'ISTJ' : 'Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized - their work, their home, their life. Value traditions and loyalty.', 
    'ISTP' : 'Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency.'
    }
feedp=dict[pyts.personality]
apti=aptitude.objects.get(email=user)
"""
for i in range(22) :
       tests=test.loc[i]   
       userss=pyt(email=tests[0],personality=tests[1],e_score=tests[2],n_score=tests[3],f_score=tests[4],j_score=tests[5],name=tests[6])
       userss.save()
test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/aptitude_test.csv")
for i in range(20):
        tests=test.loc[i]
        for j in range(65):  
            try:
                userss=answers(email=user_n.objects.get(email=tests[2]),spl_id=1,q_no=question.objects.get(q_no=j+1),marks=float(tests[j+8]))
            except:
                userss=answers(email=user_n.objects.get(email=tests[2]),spl_id=1,q_no=question.objects.get(q_no=j+1),marks=-1)
            userss.save()
test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/category.csv")
for i in range(32) :
        tests=test.loc[i]   
        userss=category(category=tests[2],par_cat=tests[3],cat_tag=tests[4])
        userss.save()
test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/category.csv")
for i in range(65) :
        tests=test.loc[i]   
        userss=question(cat_tag=category.objects.get(cat_tag=tests[1]),q_no=(i+1))
        userss.save()
test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/aptitude_test.csv")
for i in range(17) :
        tests=test.loc[i]   
        userss=aptitude(email=user_n.objects.get(email=tests[2]),timespent=tests[6],total=tests[7])
        userss.save()
test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/scoregd.csv")
for i in range(12) :
    tests=test.loc[i]
    if(user_n.objects.filter(email=tests[2]).exists()):
        userss=gds(spl_id=1,email=user_n.objects.get(email=tests[2]),topic=tests[3],analysis=tests[4],body_l=tests[5],team_s=tests[6],articulation=tests[7],participation=tests[8],total=tests[9]*10,feedback=tests[10],interviewer=interviewer.objects.get(id=1))
        userss.save()
    else:
        print(tests[2])
"""
user_avg=user_n.objects.filter(email='average@gmail.com')
gd=gds.objects.get(email=user)
gdt=(gd.total/10)*20
if(user_avg.exists()):
    pass
else:
    use=user_n(email='average@gmail.com',name='average',dept='average',spl_b=1,isadmin=False)
    use.save()
    test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/aptitude_test.csv")
    sum=0
    time=0
    apt=aptitude.objects.all()
    count=aptitude.objects.all().count()
    for ap in apt:
        sum=sum+ap.total
        time=time+ap.timespent
    sum=sum/count
    time=time/count
    userss=aptitude(email=user_n.objects.get(email='average@gmail.com'),timespent=time,total=sum)
    userss.save()
user_av=user_n.objects.get(email='average@gmail.com')
avg=aptitude.objects.get(email=user_av)
user_h=user_n.objects.filter(email='highest@gmail.com')
if(user_h.exists()):
    pass
else:
    use=user_n(email='highest@gmail.com',name='highest',dept='highest',spl_b=1,isadmin=False)
    use.save()
    test=pd.read_csv("C:/Users/ravin/report_/tsc/temp/aptitude_test.csv")
    high=aptitude.objects.order_by('-total')[0]
    userss=aptitude(email=user_n.objects.get(email='highest@gmail.com'),timespent=high.timespent,total=high.total)
    userss.save()
user_hi=user_n.objects.get(email='highest@gmail.com')
hig=aptitude.objects.get(email=user_hi)
v_count=category.objects.filter(par_cat='Verbal ability').count()
q_count=category.objects.filter(par_cat='Quantitative ability').count()
l_count=category.objects.filter(par_cat='Logical ability').count()
x=verb(user)
y=quant(user)
z=logic(user)
#a=up()
mod=mode()
n=inter(user)
data_all={'user':user,'pyts':pyts,'feedp':feedp,'apti':apti,'avg':avg,'hig':hig,'x':x,'y':y,'z':z,'mod':mod,'n':n,'gd':gd,'gdt':gdt,'users':users}
"""
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
use=user.objects.get(email='ravindrareddy1217@gmail.com')
idc=use.id
#ap=apt.objects.get(id=idc)
#feeda=ap.feedback
#gfeed=feeda
#splindex=feeda
#feedp=feeda

inter=interviewer.objects.all()
gds=gd.objects.get(id=idc)
feedg=gd.feedback
interr1=gds.interviewer1
interr2=gds.interviewer2
resum=resume.objects.get(id=idc)
essa=essay.objects.get(id=idc)
pii=pi.objects.get(id=idc)
interr11=pii.interviewer1
interr22=pii.interviewer2
data= {
'use':use,'gds':gds,'interr1':interr1,'interr2':interr2,'resum':resum,'essa':essa,'pii':pii,'interr11':interr11,'interr22':interr22
}
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
class Viewpdf(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('html.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
def home(request):
    return render(request,'home.html')
"""
def html(request):
    return render(request,'html.html',data_all)
def graphs(request):
   return render(request,'index.html',data_all)