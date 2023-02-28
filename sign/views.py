from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import BaseRegisterForm

# D5.5 Connect to a premium group if user not premium
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    # модель формы, которую реализует данный дженерик;
    model = User
    # форма, которая будет заполняться пользователем;
    form_class = BaseRegisterForm
    # URL, на который нужно направить пользователя после успешного ввода данных в форму.
    success_url = '/'
    template_name = 'sign/signup.html'


# D5.5 Connect to a premium group if user not premium
@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='Premium')
    if not request.user.groups.filter(name='Premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')
