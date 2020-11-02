from django.shortcuts import render,redirect
from .forms import UserForm,IncomeForm,ExpenseForm
from .models import Expense,Income,User
from django.views.generic import FormView,CreateView,ListView
from django.contrib.auth import login,logout,authenticate

def home(request):
    userN=request.session.get("userName")
    uid=request.session.get("userId")
    il=Income.objects.filter(user_id=uid)
    el=Expense.objects.filter(user_id=uid)
    totalIncome=0
    totalExpense=0
    for i in il:
        totalIncome=totalIncome+i.income
    
    for j in el:
        totalExpense=totalExpense+j.expense 
    
    balance=totalIncome-totalExpense
    d={'bal':balance,"userN":userN}
    return render(request,"index.html",d)

def addUser(request):
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
    else:
        u=UserForm
        return render(request,'addUser.html',{'abc':u})


def addIncome(request):
    if request.method=='POST':
        u=IncomeForm(request.POST)
        u.save()
        return redirect("/")
    else:
        u=IncomeForm
        return render(request,'addIncome.html',{'form':u})


def incomeList(request):
    uid=request.session.get("userId")
    il=Income.objects.filter(user_id=uid)
    d={'incl':il}
    return render(request,'incomeList.html',d)

def deleteIncome(request):
    id=request.GET.get('id')
    u=Income.objects.get(id=id)
    u.delete()
    return redirect("/incomeList")

def editIncome(request):
    id=request.GET.get('id')
    u=Income.objects.get(id=id)
    if request.method=='POST':
        inc=IncomeForm(request.POST,instance=u)
        inc.save()
        return redirect("/incomeList")
    else:
        inc=IncomeForm(instance=u)
        return render(request,"updateIncome.html",{'form':inc})

class addExpense(FormView):
    template_name="addExpense.html"
    form_class=ExpenseForm

class insertExpense(CreateView):
    model=Expense
    fields='__all__'
    success_url="/"

class expenseList(ListView):
    model=Expense
    template_name="expenseList.html"



def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        print(uname,passw)
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['userId']=user.id
            request.session['userName']=user.username
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html")

    else:
        return render(request,"login.html")


def logout_view(request):
    sl=list(request.session.keys())
    for i in sl:
        del request.session[i] 
    logout(request)
    return redirect("/")

def editProfile(request):
    userN=request.session.get("userName")
    user=User.objects.get(username=userN)
    u=UserForm(instance=user)
    return render(request,'updateUser.html',{'form':u})