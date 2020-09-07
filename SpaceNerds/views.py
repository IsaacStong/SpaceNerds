from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_view = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
