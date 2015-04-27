# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2

from medicament.models import Document,Doc_type, Hosp, Period, Role, Comment, Doc1, Doc2
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
# пагинация урок 12
from django.core.paginator import Paginator
from medicament.forms import CommentForm
# мой модуль для работы с базами
from medicament.oper_with_base import save_doc, get_ids
# по каждому типу докумпентов
from medicament.Form.form1 import create_report_form1, calc_sum_form1,\
    save_doc_form1,exp_to_excel_form1
from medicament.Form.form2 import create_report_form2, calc_sum_form2,\
    save_doc_form2,exp_to_excel_form2

import os
import mimetypes
from _overlapped import NULL

NUM_RECORD_ON_PAGE = 50   # число записей на странице списка


# простейший
def monitor_type_list(request):
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    args = {}
    args.update(csrf(request))
    
    args['doc_type_list']    =  Doc_type.objects.all()            
    args['username'] = auth.get_user(request).username       
    return render_to_response('medicament/monitor_list.html', args)


def monitoring_list(request, question_id ):
      
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    
# разбор параметра
# Разделим question id на части     xxx,yyy где xxx - тип мониторинга, yyy - номер страницы пагинации
    gid = get_ids(question_id)   
    type = int(gid[0])
    if len(gid) > 1:
        page_number = int(gid[1])
    else:
        page_number=1  
    region = 0
    m = 0
    period = 0
    status = '0'
    start_filter = False
    if len(gid) == 6:
        m = int(gid[2])
        period = int(gid[3])
        status = gid[4]
        region = gid[5]
        start_filter = True
        

#   Определение доступа
    usr =  auth.get_user(request)
    role = Role.objects.get(user=usr)
    if role.role == "К":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
    else:
        see_all = False
        user_hosp = role.hosp
        m = role.hosp.id
# По типам документов        
    if type==1:
        doc = Doc1                     # используемая модель
        new_doc =  create_report_form1   # функция создания новых отчетов
        calc_sum = calc_sum_form1
        result = [['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0]]
        html_response_rep = 'medicament/report_JQ_list1.html'       # Форма с JQuery
        export_to_excel = exp_to_excel_form1
    elif type==2:
        doc = Doc2                     # используемая модель
        new_doc =  create_report_form2   # функция создания новых отчетов
        calc_sum = calc_sum_form2
        result = [['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0]]
        html_response_rep = 'medicament/report_JQ_list2.html'
        export_to_excel = exp_to_excel_form2
 #### Далее не изменять без необходимости                    
    args = {}
    args.update(csrf(request))
    isOk = True 
    html_response = 'medicament/document_list.html'

    if  start_filter or request.POST:
        if see_all and 'button_create' in request.POST:
            if 'period_new' in request.POST:
                if request.POST['period_new']:
                    periodInt = int(request.POST['period_new'])
                    datef = request.POST['datef']
                    isOk = new_doc(periodInt, datef)          # создать новые мониторинги
        if request.POST: 
            page_number=1      # после нового отбора обязательно делать так!!!
            if not see_all:
                m = user_hosp.id  
            if 'region' in request.POST:
                region = int(request.POST['region'])
            if 'mo[]' in request.POST:
                mo1 = request.POST['mo[]']
                m = int(mo1)
            if 'period' in request.POST:
                period = int(request.POST['period'])
            if 'status' in request.POST:
                status = request.POST['status']
        is_filter = False 

#        if see_all and region > 0:
#        if see_all:
#            args['doc_list']    =  doc.objects.filter(hosp.region = 1)
#            is_filter = True
        
        if m > 0:
#        if m > 0 and is_filter==False:
            args['doc_list']    =  doc.objects.filter(hosp = m)
            is_filter = True
        if period > 0:
            if is_filter:
                args['doc_list']    =  args['doc_list'].filter(period = period)
            else:    
                args['doc_list']    =  doc.objects.filter(period = period)
                is_filter = True
        if status != '0':
            if is_filter:
                args['doc_list']    =  args['doc_list'].filter(status = status)
            else:    
                args['doc_list']    =  doc.objects.filter(status = status)
                is_filter = True
        if not is_filter:
            args['doc_list']    =  doc.objects.all()
# после выборки по фильтрам если надо считать отчет, то вызываю сответствующую функцию
        if see_all and period > 0 and 'button_report' in request.POST:
            html_response = html_response_rep
            args['period_name']  =  Period.objects.get(pk=period)            
            
            result = calc_sum(args['doc_list'])
        elif see_all and 'button_export' in request.POST:
            file_name = export_to_excel(args['doc_list']) 
            return redirect("/monitor/export/" + file_name)
    else:   # Первый вход по GET
        if see_all: 
            args['doc_list']    =  doc.objects.all()            
        else: 
            args['doc_list']    = doc.objects.filter(hosp = user_hosp)
# во всех случаях    
    args['doc_type']  =  Doc_type.objects.get(pk=type)
    
    if not see_all: 
        args['mo_list']  =  Hosp.objects.filter(id=user_hosp.id)
    else:                
        args['mo_list']  =  Hosp.objects.all()
    args['period_list']  =  Period.objects.all()            
    args['username'] = auth.get_user(request).username       
    args['right_all'] = see_all       
    args['isOk'] = isOk       
    
#    filtr = [m,period,status]
    args['page_number'] = page_number      
    args['period'] = period       
    args['status'] = status       
    args['hosp'] = m       

    args['result'] = result    
#   сортировка
    args['doc_list'] = args['doc_list'].order_by('-date_mod')    
#   пагинатор
    cur_page = Paginator(args['doc_list'], NUM_RECORD_ON_PAGE)  
    args['doc_page'] = cur_page.page(page_number)
     
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
# Разделим question id на части     xxx,yyy,zzz где xxx - тип мониторинга, yyy - номер страницы paginator - для возвращения на страницу
# zzz - сквозной номре документв

    gid = get_ids(question_id)   
    type = int(gid[0])
    doc_id = gid[1]
    if len(gid) == 6:
        page_number = int(gid[2])
        m = int(gid[3])  
        period = int(gid[4])
        status = gid[5]
    else:
        page_number=1  
        m = 0  
        period = 0
        status = '0'

# Настройка типа документа  
    if type == 1:
        doc = Doc1
        save_doc = save_doc_form1
        html_response = "medicament/doc_form1.html"
    elif type == 2: 
        doc = Doc2
        save_doc = save_doc_form2
        html_response = "medicament/doc_form2.html"
# конец настройки по типам!
                   
    args = {}
    args.update(csrf(request))
    isOk = True 
    actionComment =  Comment.EMPTY
    error = ''
    if request.POST:
        if  'button_addComment' in request.POST:
            add_comment(request, question_id)    # 
            mode_comment = False
        else:
            mode_comment = True

        ret_mess = save_doc(request,type,doc_id, mode_comment)
                    
        if ret_mess[0]:
            response = redirect('/form/' + str(type) + ',' + str(page_number) + ',' + str(m) \
                                + ',' + str(period) + ',' + status)
            return response
        else:
            args['doc']    =  doc.objects.get(pk=doc_id)
#            error = "Сумма по столбцам превышает итог"  
            error = ret_mess[1]
    else:   # Первый вход по GET
        args['doc']    =  doc.objects.get(pk=doc_id)            
# во всех случаях    
    args['doc_type']  =  Doc_type.objects.get(pk=type)
# ищем документ предыдущего периода 
    doc_prevList = doc.objects.filter(period = args['doc'].period.prev , hosp = args['doc'].hosp)
    if doc_prevList:
        args['doc_prev'] = doc_prevList[0]
# для визуального контроля

    args['username'] = auth.get_user(request).username       

    args['right_operator'] = not see_all       
    args['right_control'] = see_all       
    args['isOk'] = isOk  
    args['error']   =  error     
    args['page_number']   =  page_number       # для пагинации     
    
    comment_form = CommentForm      
    args['comment']  =  Comment.objects.filter(document = doc_id)            
    args['form']     =  comment_form     
  
    args['period'] = period       
    args['status'] = status       
    args['hosp'] = m       

    return render_to_response(html_response, args)


def add_comment(request, question_id):

    gid = get_ids(question_id)   
    stype = int(gid[0])
    sdoc_id = gid[1]
    if len(gid) == 6:
        spage_number = int(gid[2])
        shosp = int(gid[3])  
        speriod = int(gid[4])
        sstatus = gid[5]
    else:
        spage_number=1  
        shosp = 0  
        speriod = 0
        sstatus = '0'

    enable = request.user.is_active
    if request.POST and ('pause' not in request.session) and enable:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.document = Document.objects.get(id =  sdoc_id )
            comment.user = request.user
            comment.save()
            # далее работа с сессией, чтобы исключить повторную отправку комментария раньше чем через 20 секунд
            request.session.set_expiry(60);
            request.session['pause'] =  True;
# отладить -здесь не учитываются изменения, произошедшие за последне время        
    return redirect('/form/' + str(stype) + ',' + str(spage_number) + ',' + str(shosp) \
                                + ',' + str(speriod) + ',' + sstatus)

def export(request,question_id):
        ''' Загрузка сформированного файла Excel на клиент  с последующим его удалением с сервера
        '''
        excel_file_name = question_id
        fp = open(excel_file_name, "rb");
        response = HttpResponse(fp.read());
        fp.close();
        
        file_type = mimetypes.guess_type(excel_file_name);
        if file_type is None:
            file_type = 'application/octet-stream';
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(excel_file_name).st_size);
        response['Content-Disposition'] = "attachment; filename=report.xlsx";
        os.remove(excel_file_name)

        return response;

def contact_list(request):
    '''  Список контактов
    '''
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    args = {}
    args.update(csrf(request))
    
    args['username'] = auth.get_user(request).username       
    args['role']  =  Role.objects.all()
    return render_to_response('medicament/contact_list.html', args)





def index(request):
    return HttpResponse("Hello, world. You're at the album index.")


def test(request): 
    return render_to_response('albums/test.html', {})

    

