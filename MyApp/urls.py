"""MyExpense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('', v.home),
    path('addUser',v.addUser),
    path('addIncome',v.addIncome),
    path('addExpense',v.addExpense.as_view()),
    path('incomeList',v.incomeList),
    path('deleteIncome',v.deleteIncome),
    path('editIncome',v.editIncome),
    path('insertExpense',v.insertExpense.as_view()),
    path('expenseList',v.expenseList.as_view()),
    path('login_view',v.login_view),
    path('logout_view',v.logout_view),
    path('editProfile',v.editProfile),
]
