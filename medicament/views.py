# -*- coding: utf-8 -*-
import os
import mimetypes
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

from medicament.forms import CommentForm
from medicament.models import Document,Doc_type, Region, Hosp, Period, Role, Comment, Right_type, Doc1, Doc2, Doc3
from medicament.modelsDoc4 import Doc4, Doc4Tab1000, Doc4Tab2000, Doc4Tab3000, Doc4Tab4000, Doc4Tab5000, Doc4Tab5001, \
                                  Doc4Tab6000, Doc4Tab7000  
# мой модуль для работы с базами
from medicament.oper_with_base import save_doc, get_ids, statistic
# по каждому типу докумпентов
from medicament.Form.form1 import create_report_form1, calc_sum_form1,\
    save_doc_form1,exp_to_excel_form1,load_from_excel_form1
from medicament.Form.form2 import create_report_form2, calc_sum_form2,\
    save_doc_form2,exp_to_excel_form2,load_from_excel_form2
from medicament.Form.form3 import create_report_form3, calc_sum_form3,\
    save_doc_form3,exp_to_excel_form3
from medicament.Form.form4 import create_report_form4, calc_sum_form4,\
    save_doc_form4,exp_to_excel_form4

from medicament.forms import UploadFileForm
from medicament.oper_with_base import handle_uploaded_file



NUM_RECORD_ON_PAGE = 75   # число записей на странице списка


# простейший
def monitor_type_list(request):
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    args = {}
    args.update(csrf(request))
 #   для зарегисторированных групп свои мониторинги
#
#    art = Right_type.objects.filter( group =  5)   #doc.objects.filter(hosp__region = region)
    idgroup = request.user.groups.get_queryset()
#    assert False   
    irt = Right_type.objects.filter( group =  idgroup)   #doc.objects.filter(hosp__region = region)
    args['doc_type_list']    =  irt            
            
    
 #   args['doc_type_list']    =  Doc_type.objects.all()            
    args['username'] = auth.get_user(request).username       
    args['first_name'] = auth.get_user(request).first_name
    return render_to_response('medicament/monitor_list.html', args)


def monitoring_list(request, question_id ):
      
    if not request.user.is_authenticated():
        return redirect('/auth/login')
    
# разбор параметра
# Разделим question id на части     xxx,yyy где xxx - тип мониторинга, yyy - номер страницы пагинации
    gid = get_ids(question_id)   
    type = int(gid[0])

#   Определение доступа
    usr =  auth.get_user(request)
    try:
        role = Role.objects.get(user=usr,type=type);
    except ObjectDoesNotExist:
        html_response_err = 'medicament/error_access.html'      
        return render_to_response(html_response_err, {})

    
    if len(gid) > 1:
        page_number = int(gid[1])
    else:
        page_number=1  
    region = 0
    m = 0
    period = 0
    status = '0'
    start_filter = False
    if len(gid) >= 6:
        m = int(gid[2])
        period = int(gid[3])
        status = gid[4]
        region = int(gid[5])
        start_filter = True
        
    if len(gid) == 7:   # уточнение детализация в отчете
        detail = True
        detail_line = int(gid[6])
        detail_tab  = ''            # имя таблицы в табличной части для детализации 
    elif len(gid) == 8:
        detail = True
        detail_line = int(gid[6])
        detail_tab  = gid[7]            # имя таблицы в табличной части для детализации 
    else:
        detail = False
        detail_line = 0
        detail_tab  = ''            # имя таблицы в табличной части для детализации 

    if role.role == "К" or role.role == "F":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
    else:
        see_all = False
        user_hosp = role.hosp
        m = role.hosp.id


# По типам документов  
    tab = {}      
    if type==1:   # Лекарства
        doc = Doc1                     # используемая модель
        new_doc =  create_report_form1   # функция создания новых отчетов
        calc_sum = calc_sum_form1
        result = [['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0],['',0,0,0,0,0,0,0,0]]
        html_response_rep = 'medicament/report_form1.html'       # Форма с JQuery
        export_to_excel = exp_to_excel_form1
    elif type==2:  # кадры
        doc = Doc2                     # используемая модель
        new_doc =  create_report_form2   # функция создания новых отчетов
        calc_sum = calc_sum_form2
        result = [['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],\
                  ]
        html_response_rep = 'medicament/report_form2.html'
        export_to_excel = exp_to_excel_form2
    elif type==3:  # супертест
        doc = Doc3                    # используемая модель
        new_doc =  create_report_form3   # функция создания новых отчетов
        calc_sum = calc_sum_form3
        result = [['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0]]
        html_response_rep = 'medicament/report_form3.html'
        export_to_excel = exp_to_excel_form3
    elif type==4:  # Диспансеризация
        doc = Doc4     # используемая модель
        tab = {"tab1000":Doc4Tab1000, "tab2000":Doc4Tab2000,"tab3000":Doc4Tab3000, "tab4000":Doc4Tab4000,
               "tab5000":Doc4Tab5000, "tab5000":Doc4Tab5001,"tab6000":Doc4Tab6000, "tab7000":Doc4Tab7000,}
                       
        new_doc =  create_report_form4   # функция создания новых отчетов
        calc_sum = calc_sum_form4
        result = [['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0],['',0]]
        html_response_rep = 'medicament/report_form4.html'
        export_to_excel = exp_to_excel_form4

 #### Далее не изменять без необходимости                    
    args = {} 
    args.update(csrf(request))
    isOk = True 
    html_response = 'medicament/document_list.html'

    if  start_filter or detail or request.POST:
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

        if period > 0:
            stat = statistic()
            stat.rec_all =  doc.objects.filter(period = period).count();        

        if see_all and region > 0:
            args['doc_list']    =  doc.objects.filter(hosp__region = region)
            is_filter = True
        if m > 0:
            if is_filter:
                args['doc_list']    =  args['doc_list'].filter(hosp = m)
            else:    
                args['doc_list']    =  doc.objects.filter(hosp = m)
                is_filter = True
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
        if detail or (see_all and period > 0 and 'button_report' in request.POST):
            html_response = html_response_rep
            args['period_name']  =  Period.objects.get(pk=period)            
            if region > 0:
                args['region_name']  =  Region.objects.get(pk=region)            

            args['detail_tab']  =  detail_tab              # имеет доп смысл как стартовая вкладка            
            if detail:
                args['detail_line']  =  detail_line            
                args['detail']  =  True            
                if detail_tab.startswith('tab'):             ### ВНИМАНИЕ секции табличных частей должны вызывать detail_tab с именами tab* 
                    row_id = int(detail_line) 
                    args['tab'] = tab[detail_tab].objects.filter(doc__period=period, row = row_id)  
                    t = tab[detail_tab].objects.filter(doc__period=period, row = row_id)
 #                   assert False              
            result = calc_sum(args['doc_list'])
        if see_all and 'button_export' in request.POST:
#            assert False
            stat.rec_fltr = args['doc_list'].count();        
            stat.rec_complete =  args['doc_list'].filter(status = 'F').count();        
            stat.rec_soglas   =  args['doc_list'].filter(status = 'W').count();        
            stat.rec_correct  =  args['doc_list'].filter(status = 'C').count();        
            stat.rec_edit     =  args['doc_list'].filter(status = 'E').count();        
            file_name = export_to_excel(args['doc_list'],period,region, 0, stat) 
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
        args['region_list']  =  Region.objects.all()
    args['period_list']  =  Period.objects.all()            
    args['username'] = auth.get_user(request).username    
    args['first_name'] = auth.get_user(request).first_name	
    args['right_all'] = see_all       
    args['isOk'] = isOk       
    
#    filtr = [m,period,status]
    args['page_number'] = page_number      
    args['period'] = period       
    args['status'] = status       
    args['hosp'] = m  
    args['region'] = region       
     

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

    gid = get_ids(question_id)   
    type = int(gid[0])
    
#   Определение доступа
    usr =  auth.get_user(request)
    try:
        role = Role.objects.get(user=usr,type=type);
    except ObjectDoesNotExist:
        html_response_err = 'medicament/error_access.html'      
        return render_to_response(html_response_err, {})


# Разделим question id на части     xxx,yyy,zzz где xxx - тип мониторинга, yyy - номер страницы paginator - для возвращения на страницу
# zzz - сквозной номре документв

    doc_id = gid[1]
    if len(gid) == 7:
        page_number = int(gid[2])
        m = int(gid[3])  
        period = int(gid[4])
        status = gid[5]
        region = int(gid[6])
    else:
#       assert False
        page_number=1  
        m = 0  
        period = 0
        status = '0'
        region = 0

    if role.role == "F":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
        see_admin = True
    elif role.role == "К":
        see_all = True                # see_all  контроль и создание новых отчетов
        user_hosp = 0
        see_admin = False
    else:
        see_all = False
        user_hosp = role.hosp
        see_admin = False


# Настройка типа документа  
    if type == 1:
        doc = Doc1
        save_doc = save_doc_form1
        html_response = "medicament/doc_form1.html"
        export_to_excel = exp_to_excel_form1
    elif type == 2: 
        doc = Doc2
        save_doc = save_doc_form2
        html_response = "medicament/doc_form2.html"
        export_to_excel = exp_to_excel_form2
    elif type == 3: 
        doc = Doc3
        save_doc = save_doc_form3
        html_response = "medicament/doc_form3.html"
        export_to_excel = exp_to_excel_form3
    elif type == 4: 
        doc = Doc4
        save_doc = save_doc_form4
        html_response = "medicament/doc_form4.html"
        export_to_excel = exp_to_excel_form4
## конец настройки по типам!
                   
    args = {}
    args.update(csrf(request))
    isOk = True 
    actionComment =  Comment.EMPTY
    error = ''
    ret_mess = [True,'OK']
    
    if request.POST:
        if  'button_load' in request.POST:
#            assert False
#            load_from_excel(request, question_id)
            response = redirect('/load/' + str(type) + ',' + str(doc_id) + ','+ str(page_number) + ',' + str(m) \
                                + ',' + str(period) + ',' + status + ',' + str(region))
            return response
        if  'button_addComment' in request.POST:
            add_comment(request, question_id)    # 
            mode_comment = False
        else:
            mode_comment = True
        if  'button_export' in request.POST:                 # Кнопка Export доступна во всех режимах, поэтому работает без сохранения
            args['doc']    =  doc.objects.filter(pk=doc_id)  # выбор документа фильтром с списке, чтобы функция вывода в excel работала единообразно
            odoc = args['doc'][0];
            file_name = export_to_excel(args['doc'],odoc.period.id,region,1) 
            return redirect("/monitor/export/" + file_name)

        if  not 'button_load' in request.POST:
            ret_mess = save_doc(request,type,doc_id, mode_comment)
                    
        if ret_mess[0]:  # проверка прошла нормально
            if  'button_export' in request.POST:             # Эта ветка на память, сюда не должна попадать
                args['doc']    =  doc.objects.filter(pk=doc_id)
                file_name = export_to_excel(args['doc'], doc.period,region,1) 
                return redirect("/monitor/export/" + file_name)
            else:      
                response = redirect('/form/' + str(type) + ',' +  str(page_number) + ',' + str(m) \
                                + ',' + str(period) + ',' + status + ',' + str(region))
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
    args['first_name'] = auth.get_user(request).first_name    

    args['right_operator'] = not see_all       
    args['right_control'] = see_all       
    args['right_admin']   = see_admin
           
    args['isOk'] = isOk  
    args['error']   =  error     
    args['page_number']   =  page_number       # для пагинации     
    
    comment_form = CommentForm      
    args['comment']  =  Comment.objects.filter(document = doc_id)            
    args['form']     =  comment_form     
  
    args['period'] = period       
    args['status'] = status       
    args['hosp'] = m       
    args['region'] = region       
    args['doc_id'] = doc_id       

# Настройка типа документа  
    if type == 4:
        args['tab1000'] = Doc4Tab1000.objects.filter(doc=doc_id)       
        args['tab2000'] = Doc4Tab2000.objects.filter(doc=doc_id)        
# конец настройки по типу документа
    return render_to_response(html_response, args)


def add_comment(request, question_id):

    gid = get_ids(question_id)   
    stype = int(gid[0])
    sdoc_id = gid[1]
    if len(gid) == 7:
        spage_number = int(gid[2])
        shosp = int(gid[3])  
        speriod = int(gid[4])
        sstatus = gid[5]
        sregion = int(gid[6])
    else:
        spage_number=1  
        shosp = 0  
        speriod = 0
        sstatus = '0'
        sregion = 0
        
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
                                + ',' + str(speriod) + ',' + sstatus + ',' + str(sregion))

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
    args['first_name'] = auth.get_user(request).first_name	
    args['role']  =  Role.objects.all().order_by('hosp')
    return render_to_response('medicament/contact_list.html', args)

def document(request):
    '''  Список контактов
    '''
	
    return render_to_response('medicament/document_monit.html')
	
def FAQ(request):
    '''  Список контактов
    '''
    
    return render_to_response('medicament/FAQ.html')


def load_from_excel(request, question_id):

    args = {}
    args.update(csrf(request))
    gid = get_ids(question_id)
#    assert False   
    if request.user.is_authenticated() and len(gid) == 7:
#        assert False   
        stype = int(gid[0])
        if stype == 1:
           load_from_ex = load_from_excel_form1 
        elif stype == 2:
           load_from_ex = load_from_excel_form2
            
         
        sdoc_id = gid[1]
        spage_number = int(gid[2])
        shosp = int(gid[3])  
        speriod = int(gid[4])
        sstatus = gid[5]
        sregion = int(gid[6])
        if request.POST:
            if  'button_load' in request.POST:
#                assert False
                load_from_ex( int(sdoc_id), request.POST['filename'])
                return redirect('/monitor/' + question_id)
            else:
                return redirect('/monitor/'  + question_id)

        args['username'] = auth.get_user(request).username          
        args['first_name'] = auth.get_user(request).first_name      
        args['page_number']   =  spage_number       # для пагинации     
        args['period'] = speriod       
        args['status'] = sstatus       
        args['hosp'] = shosp       
        args['region'] = sregion       
        args['doc_type']  = stype
        if stype ==  1:
            doc = Doc1
        elif stype == 2:
            doc = Doc2
        args['doc']    =  doc.objects.get(pk=sdoc_id)            
        return render_to_response("medicament/dialog_load.html", args)
    else:
        return redirect('/')
        



def index(request):
    return HttpResponse("Hello, world. You're at the album index.")


def test(request, question_id):
    doc = Doc2.objects.get(pk=14)
    f2 = doc._meta.get_field('c2_1') # if you want one field    
    i = f2.value_from_object(doc)
    f3 = doc.c2_1
    assert False 
    return render_to_response('/', {})


# тест uoload  - взято из документации django 
def upload_file(request):
    args = {}
    args.update(csrf(request))
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render_to_response('/', {})
    else:
        form = UploadFileForm()
    args['form'] =  form

    return render_to_response('medicament/upload.html', args)
     


    

