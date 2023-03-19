from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		InternshipExperience,
		PersonalProject
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		internshipExperiences = InternshipExperience.objects.filter(is_active=True)
		personalProjects = PersonalProject.objects.filter(is_active=True)
		
		
		context["internshipExperiences"] = internshipExperiences
		context["personalProjects"] = personalProjects
		
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank your suggestions.')
		return super().form_valid(form)


