from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from sales.forms import SalesForm
from sales.models import Person, Sale, 아이디

# Create your views here.


def 세일목록(request):
    사람 = Sale.objects.all()
    context = {'사람키': 사람,
               #    '사람first':사람.first,
               }
    return render(request, "newfolder/세일목록.html", context)


def 세일상세(request, pk):
    # print(pk)
    # print(세일)
    # return HttpResponse(pk+" : 여기 상세 정보입니다")
    사람 = Sale.objects.get(id=pk)
    context = {'사람키': 사람,
               }
    return render(request, "newfolder/세일상세.html", context)

# def 세일_입력(request):
#     print(request.POST)
#     context = {
#         "폼키":SalesForm
#     }
#     return render(request, "newfolder/세일_입력.html", context)

# def 세일_입력(request):     # 형석쌤 인프런
#     print(request.POST)
#     if request.method == "POST":
#         if SalesForm(request.POST).is_valid():
#             이름 = request.POST.get("first_name")
#             성 = request.POST.get("last_name")
#             나이 = request.POST.get("age")
#             new_sale = Sale()
#             new_sale.first_name = 이름
#             new_sale.last_name = 성
#             new_sale.age = 나이
#             new_sale.person =  Person.objects.first()
#             new_sale.save()
#             return redirect("/세일목록")
#     return render(request, "newfolder/세일_입력.html", context={"폼키":SalesForm})

def 세일_입력(request):  # 기초부터 제작하는 장고
    print(request.POST)  # 객체
    폼 = SalesForm()
    if request.method == "POST":
        print("포스트 메소드로 왔네요")
        폼 = SalesForm(request.POST)
        if 폼.is_valid():
            print("유효하네요")
            print(폼.cleaned_data)
            이름 = 폼.cleaned_data['first_name']
            성 = 폼.cleaned_data['last_name']
            나이 = 폼.cleaned_data['age']
            사람 =  Person.objects.first()
            Sale.objects.create(
                first_name = 이름,
                last_name = 성,
                age = 나이,
                person = 사람
            )
            print("세일이 입력되었습니다")
            return redirect("/세일목록")
    context = {
        "폼키": 폼
    }
    return render(request, "newfolder/세일_입력.html", context)


def 홈페이지(request):
    드실분 = 아이디.objects.all()
    # return HttpResponse("응 나야")
    # return render(request, "newfolder/아무거나1.html")
    context = {'메뉴': '짜장',
               '가격': 6000,
               '예산': '5000원',
               '손님들': 드실분,
               }
    return render(request, "아무거나2.html", context)

# class SalesCreateView(CreateView):
#     model = Sale
#     template_name = 'newfolder/아무거나1.html'
#     # success_url = reverse_lazy()
#     def etc(request):
#         context = {'메뉴':'짜장',
#             '가격':6000,
#             '예산':'5000원',
#             }
#         return render(request, "newfolder/아무거나1.html", context)


