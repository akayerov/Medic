from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2

from medicament.models import Document,Doc_type, Hosp
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
# пагинация урок 12
from django.core.paginator import Paginator


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
    args = {}
    args.update(csrf(request))

    if request.POST:
        args['doc_list']    =  Document.objects.filter(hosp = 1)            
    else:
        args['doc_list']    =  Document.objects.all()            
    args['mo_list']  =  Hosp.objects.all()            
    args['username'] = auth.get_user(request).username       
    
    return render_to_response('medicament/document_list.html', args)


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

def add_comment(request, question_id):
#    if request.POST and ('pause' not in request.session):
# теперь отправка только авторизованным пользоавтелям разрешена
    enable = request.user.is_active
    if request.POST and ('pause' not in request.session) and enable:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comment_photo = Photo.objects.get(id = question_id)
            comment.comment_user = request.user
            comment.save()
            # далее работа с сессией, чтобы исключить повторную отправку комментария
            request.session.set_expiry(60);
            request.session['pause'] =  True;
        
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

    

