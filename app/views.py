from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    return render(request,'app/register.html',context={})
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Sai !Bạn vui lòng kiểm tra tài khoản và mật khẩu !')
    context = {}
    return render(request,'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):

    return render(request,'app/home.html',context= {})
def cart(request):
    context= {}
    return render(request,'app/cart.html',context)
def checkout(request):
    return render(request,'app/checkout.html',context={})
def video18(request):
    return render(request,'app/video18.html',context={})
def diemdanh(request):
    return render(request,'app/diemdanh.html',context={})
def sukem(request):
    context = {}
    return render(request,'app/quiz/sukem.html',context)
def cv(request):
    context = {}
    return render(request,'app/quiz/cv.html',context)
def link1(request):
    context = {}
    return render(request,'app/quiz/link1.html',context)
def link2(request):
    context = {}
    return render(request,'app/quiz/link2.html',context)
def nut1(request):
    context = {}
    return render(request,'app/quiz/button/nut1.html',context)
def nut2(request):
    context = {}
    return render(request,'app/quiz/button/nut2.html',context)
def nut1k1(request):
    context = {}
    return render(request,'app/quiz/button/nut1k1.html',context)
def nut2k2(request):
    context = {}
    return render(request,'app/quiz/button/nut2k2.html',context)
def video1(request):
    context = {}
    return render(request,'app/video/video1.html',context)
def video2(request):
    context = {}
    return render(request,'app/video/video2.html',context)
def video3(request):
    context = {}
    return render(request,'app/video/video3.html',context)
def video4(request):
    context = {}
    return render(request,'app/video/video4.html',context)
def video5(request):
    context = {}
    return render(request,'app/video/video5.html',context)
def video6(request):
    context = {}
    return render(request,'app/video/video6.html',context)
def video7(request):
    context = {}
    return render(request,'app/video/video7.html',context)
def video8(request):
    context = {}
    return render(request,'app/video/video8.html',context)
def video9(request):
    context = {}
    return render(request,'app/video/video9.html',context)
def video10(request):
    context = {}
    return render(request,'app/video/video10.html',context)
def video11(request):
    context = {}
    return render(request,'app/video/video11.html',context)
def video12(request):
    context = {}
    return render(request,'app/video/video12.html',context)
def tab2(request):
    context= {}
    return render(request,'app/menuvideo/tab2/menu2.html',context)
def tab2video1(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video1.html',context)
def tab2video2(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video2.html',context)
def tab2video3(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video3.html',context)
def tab2video4(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video4.html',context)
def tab2video5(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video5.html',context)
def tab2video6(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video6.html',context)
def tab2video7(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video7.html',context)
def tab2video8(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video8.html',context)
def tab2video9(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video9.html',context)
def tab2video10(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video10.html',context)
def tab2video11(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video11.html',context)
def tab2video12(request):
    context= {}
    return render(request,'app/menuvideo/tab2/video12.html',context)
def tab3(request):
    context= {}
    return render(request,'app/menuvideo/tab3/menu3.html',context)
def tab3video1(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video1.html',context)
def tab3video2(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video2.html',context)
def tab3video3(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video3.html',context)
def tab3video4(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video4.html',context)
def tab3video5(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video5.html',context)
def tab3video6(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video6.html',context)
def tab3video7(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video7.html',context)
def tab3video8(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video8.html',context)
def tab3video9(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video9.html',context)
def tab3video10(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video10.html',context)
def tab3video11(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video11.html',context)
def tab3video12(request):
    context= {}
    return render(request,'app/menuvideo/tab3/video12.html',context)
def tab4(request):
    context= {}
    return render(request,'app/menuvideo/tab4/menu4.html',context)
def tab4video1(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video1.html',context)
def tab4video2(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video2.html',context)
def tab4video3(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video3.html',context)
def tab4video4(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video4.html',context)
def tab4video5(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video5.html',context)
def tab4video6(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video6.html',context)
def tab4video7(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video7.html',context)
def tab4video8(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video8.html',context)
def tab4video9(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video9.html',context)
def tab4video10(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video10.html',context)
def tab4video11(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video11.html',context)
def tab4video12(request):
    context= {}
    return render(request,'app/menuvideo/tab4/video12.html',context)
def tab5(request):
    context= {}
    return render(request,'app/menuvideo/tab5/menu5.html',context)
def tab5video1(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video1.html',context)
def tab5video2(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video2.html',context)
def tab5video3(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video3.html',context)
def tab5video4(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video4.html',context)
def tab5video5(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video5.html',context)
def tab5video6(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video6.html',context)
def tab5video7(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video7.html',context)
def tab5video8(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video8.html',context)
def tab5video9(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video9.html',context)
def tab5video10(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video10.html',context)
def tab5video11(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video11.html',context)
def tab5video12(request):
    context= {}
    return render(request,'app/menuvideo/tab5/video12.html',context)
def tab6(request):
    context= {}
    return render(request,'app/menuvideo/tab6/menu6.html',context)
def tab6video1(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video1.html',context)
def tab6video2(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video2.html',context)
def tab6video3(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video3.html',context)
def tab6video4(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video4.html',context)
def tab6video5(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video5.html',context)
def tab6video6(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video6.html',context)
def tab6video7(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video7.html',context)
def tab6video8(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video8.html',context)
def tab6video9(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video9.html',context)
def tab6video10(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video10.html',context)
def tab6video11(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video11.html',context)
def tab6video12(request):
    context= {}
    return render(request,'app/menuvideo/tab6/video12.html',context)