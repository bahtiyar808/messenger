import secrets
import string

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from .models import Room, Profile
from .forms import ProfileForm


@login_required
def index(request):
    if request.method == 'POST':
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room)

        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room)
    return render(request, 'index.html')


@login_required
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'user': request.user,
    })


# def upload_pic(request, pk):
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#
#     else:
#         form = ProfileForm()
#     return render(request, 'create_profile.html', {'form': form})

class UpdateUser(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'


class ShowProfilePageView(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Profile
    template_name = 'user_profile.html'
    context_object_name = 'user'


class UsersList(ListView):
    model = Profile
    template_name = 'users_list.html'
    context_object_name = 'users'

    def generate_random_string(self, length=12):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for i in range(length))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for user in context['users']:
            user.random_string = self.generate_random_string()
        return context

class RoomsList(ListView):
    model = Room
    template_name = 'rooms_list.html'
    context_object_name = 'rooms'

class RoomDelete(DeleteView):
    model = Room
    template_name = 'room_delete.html'
    success_url = reverse_lazy('rooms_list')