from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from sales.forms import SalesForm
from sales.models import Sale, 아이디

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


def 세일_입력(request):
    print(request.POST)  # 객체
    # if request.method == "POST":
    #     temp = request.POST.get("세일목록_input")
    #     print(temp)
    #     new_sale = Sale()
    #     # new_sale = temp
    #     # new_sale.save()
    context = {
        "폼키": SalesForm
    }
    render(request, "newfolder/세일_입력.html", context)
    # else:
    #     render(request, "newfolder/세일_입력.html", context={"text":"Get method"})


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


