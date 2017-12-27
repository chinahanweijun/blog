from django.shortcuts import render

# Create your views here.
def Index(request):
    # 逻辑处理
    datas = [2, ' white', 5]
    return render(request, 'index.html', locals())
    # locals() 返回局部变量 globals() 全局变量