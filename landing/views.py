from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from decouple import config
import requests

from landing.forms import ContactForm


class LandingView(TemplateView):
    template_name = 'index.html'


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = f"""<b>Mensaje de Portafolio</b>
<b>Nombre:</b> {form.data['name']}
<b>Email:</b> {form.data['email']}
<b>Origen:</b> {request.META.get('REMOTE_ADDR')}
<b>Asunto:</b> {form.data['subject']}
<b>Mensaje:</b> {form.data['msg']}"""
            body = {
                "chat_id": -1001943113718,
                "parse_mode": "HTML",
                "text": msg
            }
            requests.post(f'https://api.telegram.org/{config("BOT_TOKEN")}/sendMessage',
                          json=body,
                          proxies={'http': 'http://localhost:4000', 'https': 'http://localhost:4000'})
            return JsonResponse({'success': True})
        else:
            print(form.errors)
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
