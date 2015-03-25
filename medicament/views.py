# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2

from medicament.models import Document,Doc_type, Hosp, Period, Role, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
# пагинация урок 12
from django.core.paginator import Paginator
from medicament.forms import CommentForm
# мой модуль для работы с базами
from medicament.oper_with_base import create_new_report, add_action_in_comment, save_doc, calc_sum, export_to_excel


# Начинаем со списка Альбомов
# простейший
def monitor_type_list(request):
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    args = {}
    args.update(csrf(request))
    
    args['doc_type_list']    =  Doc_type.objects.all()            
    args['username'] = auth.get_user(request).username       
    return render_to_response('medicament/monitor_list.html', args)


def monitoring_list(request):
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    
#   Определение доступа
    usr =  auth.get_user(request)
    role = Role.objects.get(user=usr)
    if role.role == "К":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
    else:
        see_all = False
        user_hosp = role.hosp
   
                 
    args = {}
    args.update(csrf(request))
    m = 0
    period = 0
    status = 0
    isOk = True 
    result = [['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0]]
    html_response = 'medicament/document_list.html'

    if request.POST:
        if see_all and 'button_create' in request.POST:
            if 'period_new' in request.POST:
                if request.POST['period_new']:
                    periodInt = int(request.POST['period_new'])
                    datef = request.POST['datef']
                    isOk = create_new_report(1, periodInt, datef)          # тип 1 мониторинга
        if not see_all:
            m = user_hosp.id  
        if 'mo[]' in request.POST:
            mo1 = request.POST['mo[]']
            m = int(mo1)
        if 'period' in request.POST:
            period = int(request.POST['period'])
        if 'status' in request.POST:
            status = request.POST['status']
        is_filter = False 
        if m > 0:
            args['doc_list']    =  Document.objects.filter(hosp = m)
            is_filter = True
        if period > 0:
            if is_filter:
                args['doc_list']    =  args['doc_list'].filter(period = period)
            else:    
                args['doc_list']    =  Document.objects.filter(period = period)
                is_filter = True
        if status != '0':
            if is_filter:
                args['doc_list']    =  args['doc_list'].filter(status = status)
            else:    
                args['doc_list']    =  Document.objects.filter(status = status)
                is_filter = True
        if not is_filter:
            args['doc_list']    =  Document.objects.all()
# после выборки по фильрам если надо считать отчет, то вызываю сответствующую функцию
        if see_all and 'button_report' in request.POST:
            html_response = 'medicament/report_list.html'
            result = calc_sum(args['doc_list'])
        elif see_all and 'button_export' in request.POST:
            export_to_excel(args['doc_list'])   
    else:   # Первый вход по GET
        if see_all: 
            args['doc_list']    =  Document.objects.all()            
        else: 
            args['doc_list']    = Document.objects.filter(hosp = user_hosp)
# во всех случаях    
    if not see_all: 
        args['mo_list']  =  Hosp.objects.filter(id=user_hosp.id)
    else:                
        args['mo_list']  =  Hosp.objects.all()
    args['period_list']  =  Period.objects.all()            
    args['username'] = auth.get_user(request).username       
    args['right_all'] = see_all       
    args['isOk'] = isOk       
    
#    filtr = [m,period,status]
    args['period'] = period       
    args['status'] = status       
    args['hosp'] = m       

    args['result'] = result       
    
    return render_to_response(html_response, args)

def monitoring_form(request, question_id):
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    
#   Определение доступа
    usr =  auth.get_user(request)
    role = Role.objects.get(user=usr)
    if role.role == "К":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
    else:
        see_all = False
        user_hosp = role.hosp
   
                 
    args = {}
    args.update(csrf(request))
    m = 0
    period = 0
    status = 0
    isOk = True 
    actionComment =  Comment.EMPTY
    error = ''
    if request.POST:
        ret_mess = save_doc(request,question_id)
        if ret_mess[0]:
            response = redirect('/form1')
            return response
        else:
            args['doc']    =  Document.objects.get(pk=question_id)
#            error = "Сумма по столбцам превышает итог"  
            error = ret_mess[1]
    else:   # Первый вход по GET
        args['doc']    =  Document.objects.get(pk=question_id)            
# во всех случаях    
    if not see_all: 
        args['mo_list']  =  Hosp.objects.filter(id=user_hosp.id)
    else:                
        args['mo_list']  =  Hosp.objects.all()
    args['period_list']  =  Period.objects.all()            
    args['username'] = auth.get_user(request).username       

    args['right_operator'] = not see_all       
#    args['right_operator'] = True       
    args['right_control'] = see_all       
    args['isOk'] = isOk  
    args['error']   =  error     
    
    comment_form = CommentForm      
    args['comment']  =  Comment.objects.filter(document = question_id)            
    args['form']     =  comment_form     
  
    return render_to_response('medicament/document_form.html', args)


def add_comment(request, question_id):
    enable = request.user.is_active
    if request.POST and ('pause' not in request.session) and enable:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.document = Document.objects.get(id = question_id)
            comment.user = request.user
            comment.save()
            # далее работа с сессией, чтобы исключить повторную отправку комментария
            request.session.set_expiry(60);
            request.session['pause'] =  True;
        
    return redirect('/monitor/' + question_id)







def index(request):
    return HttpResponse("Hello, world. You're at the album index.")

# возращает 5 последних элементов
def index1(request):
    latest_albums_list = Album.objects.order_by('-id')[:5]
    output = ', '.join([p.album_text for p in latest_albums_list])
    return HttpResponse(output)
# использует шаблон + контекст
def index2(request):
    latest_albums_list = Album.objects.order_by('-id')[:5]
    template = loader.get_template('albums/index2.html')
    context = RequestContext(request, {
        'latest_albums_list': latest_albums_list,
    })
    return HttpResponse(template.render(context))
# с использованием render
def index3(request):
#   latest_albums_list = Album.objects.order_by('-id')[:5]
#   latest_albums_list = Album.objects.all();
    latest_albums_list = Album.objects.order_by('-photo_date').all()
    context = {'latest_albums_list': latest_albums_list }
    return render(request, 'albums/index2.html', context)
# Варианты перехода к деталям
def detail(request, question_id):
    try:
        question = Album.objects.get(pk=question_id)
    except Album.DoesNotExist:
        raise Http404
    return render(request, 'albums/detail.html', {'question': question}) 
   
def detail1(request, question_id):
    question = get_object_or_404(Album, pk=question_id)
    return render(request, 'albums/detail.html', {'question': question})

#-----Далее по входу сразу имееем список фотографий с комментариями ############################################
def photo_list(request,page_number=1):
#   photo_list = Photo.objects.all();
    photo_list = Photo.objects.order_by('-photo_date').all()
    cur_page = Paginator(photo_list, 3)  
    # по 3 фотки на станицу    
    
    context = {'photo_list': cur_page.page(page_number),  'username': auth.get_user(request).username }
    
    return render(request, 'albums/photo_list.html', context)
# вариант 1
#def photo_detail(request, question_id):
#    photo = Photo.objects.get(id = question_id) 
#    comment = Comment.objects.filter(comment_photo_id = question_id)
#    comment_form = Comment 
##    assert False        При False останавливает и  выводит состояние
#    context = {'photo': photo, 'comment': comment, 'form': comment_form }
#    return render(request, 'albums/photo_detail.html', context)

def photo_detail(request, question_id):
#    photo = Photo.objects.get(id = question_id) 
#    comment = Comment.objects.filter(comment_photo_id = question_id)
 
    comment_form = CommentForm 
    args = {}
    args.update(csrf(request))
    
    args['photo']    =  Photo.objects.get(id = question_id)            
    args['comment']  =  Comment.objects.filter(comment_photo_id = question_id)            
    args['form']     =  comment_form     
    args['username'] = auth.get_user(request).username   
   
    return render_to_response('albums/photo_detail.html', args)

def add_like(request, question_id):
    try:
        if not question_id in request.COOKIES:
            photo = Photo.objects.get(id = question_id) 
            photo.photo_rating_num += 1
            photo.save()
            # далее рабта с куками
            response = redirect('/albums/' + question_id)
            response.set_cookie(question_id, "TestCookie")
            return response
        
    except ObjectDoesNotExist:
        raise Http404  
    return redirect('/albums/' + question_id)



def search(request): 
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            photos = Photo.objects.filter(photo_title__icontains=q)
#            return render_to_response('albums/search_result.html', {'Photo': photos, 'query': q})   рабочий
            return render_to_response('albums/photo_list.html', {'photo_list': photos, 'path2': ""})
        else:
            return render_to_response('albums/search.html', {'Error': True})
    else:
        return render_to_response('albums/search.html', {'Error': True})

def test(request): 
    return render_to_response('albums/test.html', {})

    

