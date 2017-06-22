# django imports

from django.shortcuts import render
  
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View, generic
from .models impor UserProfile

class HomepageView(generic.TemplateView):
	
	"""
	Homepage View
	"""

	# template_name = 'forum/index.html'

	def get(self, *args, **kwargs):
		"""
		check if user is already loggedin then redirect to dashboard
		"""

		if self.request.user.is_authenticated():
			return redirect('')
		return super(HomepageView, self).get(*args, **kwargs)



class DashboardView(LoginRequiredMixin, generic.ListView):
	
	"""
	Dashboard View
	"""

	# template_name = 'forum/DASHBOARD.html'

	def get_queryset(self)
		return UserProfile.objects.all()


