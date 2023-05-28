from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "common/home.html"

    def get(self, request):
        context = {
            "button_text": "저를 눌러주세요",
            "board_url": "/pybo",
        }
        return render(request, self.template_name, context)

    def post(self):
        return redirect(self.board_url)
