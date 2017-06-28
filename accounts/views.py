from django.shortcuts import render,redirect
from django.contrib.auth import (login,logout,authenticate,get_user_model)
from .forms import UserLoginForm,Register

def Login_View(request):
    form=UserLoginForm(request.POST or None)
    next=request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect("/")
  #      print(request.user.is_authenticated())
    context={"form":form}
    return render(request,"loginform.html",context)


def Register_View(request):
    form=Register(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        if next:
            return redirect(next)
        return redirect("/")
       # new_user=authenticate(username=user.username,password=password)
       # login(request,new_user)
    context={"form":form}
    return render(request,"loginform.html",context)




def Logout_View(request):
   logout(request)
   return render(request, "loginform.html",{})