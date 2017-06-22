from django.shortcuts import render

# Create your views here.

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
