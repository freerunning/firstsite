#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from polls import models

# Create your views here.
ip_name = {'172.28.10.142':'丁宇', 
'172.28.10.74':'韩不举', 
'172.28.10.98':'傻逼熊波',
'172.28.10.102':'老卢', 
'172.28.10.46':'鲁大师', 
}

def index(request):
    latest_poll_list = models.Poll.objects.order_by('-pub_date')[:5]
    return render_to_response('index.html', {'latest_poll_list':latest_poll_list})

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def error404(request):
	html = '<tml><body>404</body></html>'
	#return HttpResponse(html)
	return Http404()

def test(request):
	html="<html><body><h1>{{name}}is a big SB.</h1></boty></html>" 
	t = Template(html)
	c= Context({'name':'xiongbo'})
	return HttpResponse(t.render(c))

def test_template(request):
	now = datetime.datetime.now()
	na = 'Django'
	fa = 'code'
	#t = get_template('template.html')
	#html = t.render(Context({'nowdate':now, 'name':na, 'favourite':fa}))
	#return HttpResponse(html)
	return render_to_response('template.html', {'nowdate':now, 'name':na, 'favourite':fa})
	#return render_to_response('template.html', locals())

def display_meta(request):
	values = request.META.items()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def detail(request, poll_id):
    p = get_object_or_404(models.Poll, pk=poll_id)
    ips = []
    for c in p.choice_set.all():
        ips += [i.ip for i in c.ip.all()] 
    
    ip = request.META.get("REMOTE_ADDR", None)
    if ip in ips:
        return render_to_response('results.html', {'poll':p})
    
    return render_to_response('detail.html', {'poll':p})

def results(request, poll_id):
    p = get_object_or_404(models.Poll, pk=poll_id)
    return render_to_response('results.html', {'poll':p})

def vote(request, poll_id):
    p = get_object_or_404(models.Poll, pk=poll_id)
    ips = []
    for c in p.choice_set.all():
        ips += [i.ip for i in c.ip.all()]

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render_to_response('detail.html', {'poll':p, 'error_message':"You didn't select a choice"})
    else:
        ip = request.META.get("REMOTE_ADDR", None)
        if ip in ip_name:
            name = ip_name.__getitem__(ip)
        else:
            name = ip
        #ips = [i.ip for i in selected_choice.ip.all()]
        if ip in ips:
            return render_to_response('detail.html', {'poll':p, 'already_vote': name, 'error_message':False})
        else:
            ipmodel = models.Ip(ip = ip, name = name)
            ipmodel.save()
            selected_choice.ip.add(ipmodel)
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def password_change(request):
    return render_to_response('password_change.html')

def error301(request):
    return HttpResponsePermanentRedirect('http://cidian.youdao.com/download/YoudaoDict.exe');

def error302(request):
    return HttpResponseRedirect('http://cidian.youdao.com/download/YoudaoDict.exe');

def error303(request):
    response = HttpResponse(content="", status=303)
    response["Location"] = 'http://172.28.10.142:8000/polls/e303/YoudaoDict.exe/';
    return response
    
def error(request, idx):
    httpcodelist = [100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 300, 301, 302, 303, 304, 305, 306, 307,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 449,
    500, 501, 502, 503, 504, 505, 506, 507, 509, 510,]

    httpcode = httpcodelist[int(idx)]

    html = '<tml><body>%s</body></html>' % httpcode
    response = HttpResponse(html, status=httpcode)
    return response
