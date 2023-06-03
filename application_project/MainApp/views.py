from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Places
from .utils import *
from .forms import *
import vk_api


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class UserView(CreateView):
    template_name = "user.html"
    form_class = AddPost
    model = Places
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_social_auth = self.request.user.social_auth.get(provider='vk-oauth2')
            user_id = user_social_auth.uid
            access_token = user_social_auth.extra_data['access_token']
            vk_session = vk_api.VkApi(token=access_token)
            vk = vk_session.get_api()
            user_info = vk.users.get(user_ids=user_id, fields='photo_max_orig')
            photo_url = user_info[0]['photo_max_orig']
            context['photo_url'] = photo_url
        return context

    def form_valid(self, form):
        return super(UserView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        author = self.request.user
        place_name = request.POST['place_name']
        comment = request.POST['comment']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        Places.objects.create(author=author,
                              place_name=place_name,
                              comment=comment,
                              latitude=latitude,
                              longitude = longitude)
        return redirect('home')



def logout_user(request):
    logout(request)
    return redirect('user')
