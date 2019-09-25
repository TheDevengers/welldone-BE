# -*- coding: utf-8 -*-
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.views.generic import FormView
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response



class PasswordRecoveryApi(APIView):
    email_template_name = 'registration/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    token_generator = default_token_generator

    def post(self, request):
        print(request.data.get('email'))
        form = PasswordResetForm(request.data)
        print(form)
        if form.is_valid():
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.subject_template_name,
                'request': self.request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
        return Response()
