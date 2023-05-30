from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import vk_api


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class UserView(TemplateView):
    template_name = "user.html"

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




def logout_user(request):
    logout(request)
    return redirect('user')
