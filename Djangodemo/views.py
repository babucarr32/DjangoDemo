from os import read
from django.http import HttpResponse
from django.shortcuts import render
import time
import os

def home(request):
    path = r"C:\Users\User\Desktop"
    new = []
    for root,dirs,file in os.walk(path):
        new.append(file)
    # search = input("Search:> ")
    # while search != "quit":
    #     search = input("Search:> ")
    #     for i in new:
    #         for x in i:
    #             if x.endswith(search):
    #                 print(x)

    return render(request, "home.html")

def contactFunc(request):
    num = "My name is Babucarr"
    return render(request, "contact.html",{
        "numberFull": num
    })