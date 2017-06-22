from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View, generic
from .models impor UserProfile


class DashboardView(LoginRequiredMixin, generic.ListView):
	
	"""
	Dashboard View
	"""

	# template_name = 'forum/DASHBOARD.html'

	def get_queryset(self)
		return UserProfile.objects.all()



