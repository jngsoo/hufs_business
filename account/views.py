from django.views import generic
from .forms import ProfileForm,UserCreationMultiForm,LoginForm
from .models import Profile,Origin_users
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

class UserSignupView(generic.CreateView):
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self,form):
        if Origin_users.objects.filter(origin_num =form['profile'].cleaned_data['num']):        
            user = form['user'].save()
            profile = form['profile'].save(commit=False)
            profile.user = user
            profile.save()
            return redirect(self.success_url)
        else:
            return redirect('/')

def Login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponse('로그인 성공.')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})



def locker(request):
    return render(request, 'locker.html')