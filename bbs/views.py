from django.shortcuts import render,redirect
from django.views import View

from .models import Topic
from .forms import TopicForm, YearMonthForm

from . import calendar

import datetime

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}

        #指定した年月をバリデーション
        form    = YearMonthForm(request.GET)
        today   = datetime.date.today()

        if form.is_valid():
            cleaned         = form.clean()
            selected_date   = datetime.datetime(year=cleaned["year"], month=cleaned["month"], day=1)
        else:
            selected_date   = datetime.datetime(year=today.year, month=today.month, day=1)

        context["selected_date"]                        = selected_date
        context["month_date"]                           = calendar.create_calendar(selected_date.year, selected_date.month)
        context["months"], context["years"]             = calendar.create_months_years(selected_date, today)
        context["last_month"], context["next_month"]    = calendar.create_last_next_month(selected_date)

        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("bbs:index")

index   = IndexView.as_view()

