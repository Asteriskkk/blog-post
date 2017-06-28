from urllib.parse import quote_plus
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,Http404
from . models import post
from . forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.contenttypes.models import ContentType
from post.models import post
from django.contrib.auth.decorators import login_required


def homepage(request):
    queryset_list=post.objects.all().order_by("-timestamp")

    query = request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(Q(title__icontains=query)|
                                           Q(context__icontains=query)|
                                           Q(timestamp__icontains=query)|
                                           Q(update__icontains=query)

                                           )


    paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context={"object_list":contacts}
    return render(request,"homepage.html",context)



@login_required(login_url='/login/')
def create(request):
    #if not request.user.is_staff or not request.user.is_superuser:
     #   raise Http404
    if not request.user.is_authenticated:
        raise Http404
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.piyush())
    content={"form":form}
    return render(request,"form.html",content)


@login_required(login_url='/login/')
def update(request,id=None):
   # if not request.user.is_staff or not request.user.is_superuser:
    #    raise Http404
    if not request.user.is_authenticated:
        raise Http404
    content = get_object_or_404(post, id=id)
    form = PostForm (request.POST or None,request.FILES or None,instance=content)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.piyush())
    contexts = {"details": "detail","form":form,}
    return render(request, "form.html", contexts)





def detail(request, id,):

    content=get_object_or_404(post,id=id)
    #share_string=quote_plus(content.context)

    content_type=ContentType.objects.get_for_model(post)
    obj_id=content.id

    #initial_data={"content_type":content.get_content_type,
     #             "object_id":content.id,
      #            "parent_id":content.id,

    #}
    form=CommentForm(request.POST or None)
    if form.is_valid() and request.user.is_authenticated:
        #c_type = form.cleaned_data.get("content_type")
        #content_type = ContentType.objects.get(model=post)
       # obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("content")
        parent_obj = None
       # try:
        parent_id = request.POST.get("parent_id")
        #except:
         #   parent_id = None

       # if parent_id:
        parent_qs = Comment.objects.filter(id=parent_id)
        #    if parent_qs.exists() and parent_qs.count() == 1:
        parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return redirect(content.piyush())
    comments =Comment.objects.filter(content_type=content_type,object_id=obj_id).filter(parent=None)
    contexts={"form":form,"details":"detail","data_detail":content,"comments":comments}
    return render(request,"detail.html",contexts,)

@login_required(login_url='/login/')
def delete(request,abc):
   # if not request.user.is_staff or not request.user.is_superuser:
    #    raise Http404
    if not request.user.is_authenticated:
        raise Http404
    content = get_object_or_404(post, id=abc)
    content.delete()
    return redirect("post:homepage")



