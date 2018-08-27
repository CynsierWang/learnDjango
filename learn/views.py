# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from learn.models import Person,Coach,duty,bus_list
from learn.models import booking as booking_model
# Create your views here.
def addUser(request):
    return render(request,'addUser.html')

def addPerson(request):
    n = request.GET['name']
    g  = int(request.GET['group'])
    if n=="":
        return render(request,'addUser.html')
    np = Person(name=n,group=g)
    np.save()
    return HttpResponse(n+"添加成功")

def addCoach(request):
    n = request.GET['name']
    g = int(request.GET['group'])
    if n=="":
        return render(request,'addUser.html')    
    nc = Coach(name=n,group=g)
    nc.save()
    nd = duty(id=nc.id)
    nd.save()
    return HttpResponse(n+"添加成功")

def loginCoach(request):
    return render(request,'loginCoach.html')

def loginPerson(request):
    return render(request,'loginPerson.html')

def home(request):
    Info_dict = {'key1':u'value1','key2':u'value2'}
    return render(request,'home.html',{'info_dict':Info_dict})

def check(request):
    return render(request,'check.html')

def check_result(request):
    g = int(request.GET['group'])
    List = booking_model.objects.filter(group=g)
    book_list = []
    for l in List:
        book_list.append([Coach.objects.get(id=l.coach).name,Person.objects.get(id=l.person),l.class_time])
    return render(request, 'check_result.html', {'booking_list': book_list,"group":g})

def adjust(request):
    n = request.GET['name']
    if n=="":
        return render(request,'loginCoach.html')
    g = int(request.GET['group'])
    Coach.objects.get_or_create(name=n,group=g)
    nc = Coach.objects.get(name=n,group=g).id
    nd = duty(id=nc)
    nd.save()
    nd = duty.objects.get(id=nc)
    s = ""
    if (nd.class_1==0 and nd.class_2==0 and nd.class_3==0 and nd.class_4==0):
        s = s+" 休假"
    elif (nd.day_off==1):
        s = s+" 休假"
    else:
        if nd.class_1!=0:
            s = s+" 8~10点"
        if nd.class_2!=0:
            s = s+" 10~12点"
        if nd.class_3!=0:
            s = s+" 14~16点"
        if nd.class_4!=0:
            s = s+" 16~18点"
    return render(request, 'adjust.html', {'cid': nc,'content':s})

def adjust_result(request,cid):
    s='您已选择 '
    c1=2
    c2=2
    c3=2
    c4=2
    df=0
    if 'dayoff' in request.GET:
        s=s+"休假"
        df=1
    else:
        if 'duty1' in request.GET:
            s=s+"上午8-10点 "
        else:
            c1=0
        if 'duty2' in request.GET:
            s=s+"上午10-12点 "
        else:
            c2=0
        if 'duty3' in request.GET:
            s=s+"下午2-4点 "
        else:
            c3=0
        if 'duty4' in request.GET:
            s=s+"下午4-6点 "
        else:
            c4=0
    coach = duty.objects.get(id=cid)
    coach.class_1 = c1
    coach.class_2 = c2
    coach.class_3 = c3
    coach.class_4 = c4
    coach.day_off = df
    coach.save()
    url = "/loginCoach"
    dis = "点击重新选择时段"
    return render(request,'home.html',{'content':s,'url':url,'dis':dis})

def booking(request):
    group = int(request.GET['group'])
    name = request.GET['name']
    if name=="":
        return render(request,'loginPerson.html')
    Person.objects.get_or_create(name=name,group=group)
    p = Person.objects.get(name=name,group=group)
    pid = p.id
    have_booked = booking_model.objects.filter(person=pid)
    if len(have_booked)!=0:
        cid=booking_model.objects.get(person=pid).coach
        class_time=booking_model.objects.get(person=pid).class_time
        cname = Coach.objects.get(id=cid).name
        content = "已预约 "+cname+" 教练 第"+str(class_time)+"节 练车"
        url     = "/cancal/?pid="+str(pid)
        dis     = "点击取消预约"
        return render(request,"home.html",{'content':content,'url':url,'dis':dis})

    coachs = Coach.objects.filter(group=group)
    coach_list = {}
    for coach in coachs:
        coach_duty = duty.objects.get(id=coach.id)
        if coach_duty.day_off:
            continue
        num = [coach_duty.class_1,coach_duty.class_2,coach_duty.class_3,coach_duty.class_4]
        coach_list[coach.name]={'cid':coach.id,'num':num}
    return render(request, 'booking.html', {'group':group,'pid': pid,'coach_list':coach_list})

def booking_result(request):
    s=''
    group = int(request.GET['group'])
    pid = int(request.GET['pid'])

    have_booked = booking_model.objects.filter(person=pid)
    if len(have_booked)!=0:
        return book_result(request)

    cid = int(request.GET['cid'])
    class_time = int(request.GET['class'])
    num = 0
    if class_time==1:
        c = duty.objects.get(id=cid)
        num = c.class_1
        if num>0:
            c.class_1=num-1;
            c.save()
            booking_model.objects.get_or_create(group=group,person=pid,coach=cid,class_time=class_time)
            s=s+"预约成功，8~10点，继续"
            url = "/bus/?pid="+str(pid)
            dis = "预约班车"
    elif class_time==2:
        c = duty.objects.get(id=cid)
        num = c.class_2
        if num>0:
            c.class_2=num-1;
            c.save()
            booking_model.objects.get_or_create(group=group,person=pid,coach=cid,class_time=class_time)
            s=s+"预约成功，10~12点，继续"
            url = "/bus/?pid="+str(pid)
            dis = "预约班车"
    elif class_time==3:
        c = duty.objects.get(id=cid)
        num = c.class_3
        if num>0:
            c.class_3=num-1;
            c.save()
            booking_model.objects.get_or_create(group=group,person=pid,coach=cid,class_time=class_time)
            s=s+"预约成功，14~16点，继续"
            url = "/bus/?pid="+str(pid)
            dis = "预约班车"
    else:
        c = duty.objects.get(id=cid)
        num = c.class_4
        if num>0:
            c.class_4=num-1;
            c.save()
            booking_model.objects.get_or_create(group=group,person=pid,coach=cid,class_time=class_time)
            s=s+"预约成功，16~18点，继续"
            url = "/bus/?pid="+str(pid)
            dis = "预约班车"

    if num==0:
        s="没抢到最后一个..."
        return HttpResponse(s)
    return render(request,'home.html',{'content':s,'url':url,'dis':dis})

def book_result(request):
    s=''
    pid = int(request.GET['pid'])

    person = booking_model.objects.get(person=pid)

    class_time= person.class_time
    s=s+"预约第"+str(class_time)+"节练车，继续"
    url = "/bus/?pid="+str(pid)
    dis = "预约班车"
    
    return render(request,'home.html',{'content':s,'url':url,'dis':dis})

def bus(request):
    pid = request.GET['pid']
    return render(request,'bus.html',{'pid':pid})

def bus_result(request,pid):
    route = request.GET['route']
    bus_list.objects.get_or_create(id=pid)
    b = bus_list.objects.get(id=pid)
    b.route = route
    b.save()
    return HttpResponse('预约班车成功')

def cancal(request):
    pid = request.GET['pid']
    person = booking_model.objects.get(person=pid)
    pname = Person.objects.get(id=pid).name
    cid = person.coach
    cname = Coach.objects.get(id=cid).name
    d = duty.objects.get(id=cid)
    class_time = person.class_time
    group = person.group

    booking_model.objects.get(person=pid).delete()
    bus_list.objects.get(id=pid).delete()
    s="已取消 "+cname+" 教练 第"+str(class_time)+"节 练车"

    if class_time==1:
        d.class_1 = d.class_1+1
    elif class_time==2:
        d.class_2 = d.class_2+1
    elif class_time==2:
        d.class_3 = d.class_3+1
    else:
        d.class_4 = d.class_4+1
    d.save()

    url = "/booking/?name="+pname+"&group="+str(group)
    return render(request,'home.html',{'content':s,'url':url,'dis':"重新约车"})

