from .models import Topic

import datetime


def create_calendar(year,month):

    #今月の初日を指定
    dt  = datetime.date(year,month,1)

    #calendarはweekのリスト、weekは日付のリスト
    calendar    = []
    week        = []

    #月始めが日曜日以外の場合、空欄を追加する。
    if dt.weekday() != 6:
        week    = [ {"day":""} for i in range(dt.weekday()+1) ]

    #1日ずつ追加して月が変わったらループ終了
    while True:

        week.append({"day":dt.day})
        dt += datetime.timedelta(days=1)

        #週末になるたびに追加する。
        if dt.weekday() == 6:
            calendar.append(week)
            week    = []

        #月が変わったら終了
        if month != dt.month:
            #一ヶ月の最終週を追加する。
            if dt.weekday() != 6:

                #最終週の空白を追加
                for i in range(6-dt.weekday()):
                    week.append({"day":""})

                calendar.append(week)

            break

    return calendar

    #最終的に作られるcalendarのイメージ。
    """
    [ [ {'day':''  }, {'day':''  }, {'day':'1' }, {'day':'2' }, {'day': '3' }, {'day':'4' }, {'day': '5' } ],
      [ {'day':'6' }, {'day':'7' }, {'day':'8' }, {'day':'9' }, {'day': '10'}, {'day':'11'}, {'day': '12'} ],
      [ {'day':'13'}, {'day':'14'}, {'day':'15'}, {'day':'16'}, {'day': '17'}, {'day':'18'}, {'day': '19'} ],
      [ {'day':'20'}, {'day':'21'}, {'day':'22'}, {'day':'23'}, {'day': '24'}, {'day':'25'}, {'day': '26'} ],
      [ {'day':'27'}, {'day':'28'}, {'day':'29'}, {'day':'30'}  ]
      ]
    """


#カレンダーの年の選択肢(リスト)を作る
def create_months_years(selected_date, today):

    months  = [ i for i in range(1,13) ]

    oldest  = Topic.objects.order_by( "dt").first()
    newest  = Topic.objects.order_by("-dt").first()

    #最新最古のデータと指定された日付を比較。選択肢を作る
    if oldest and newest:
        if selected_date < oldest.use_date:
            years = [ i for i in range(selected_date.year,   newest.use_date.year+1)]
        elif newest.use_date < selected_date:
            years = [ i for i in range(oldest.use_date.year, selected_date.year+1  )]  
        else:
            years = [ i for i in range(oldest.use_date.year, newest.use_date.year+1)]
    else:
        if selected_date < today:
            years = [ i for i in range(selected_date.year, today.year+1)]
        else:
            years = [ i for i in range(today.year, selected_date.year+1)]
    
    return months, years


#先月と来月のdatetimeオブジェクトを作る
def create_last_next_month(selected_date):

    if selected_date.month == 12: 
        next_month   = datetime.date( year=selected_date.year+1 , month=1                     , day=1 )
        last_month   = datetime.date( year=selected_date.year   , month=selected_date.month-1 , day=1 )
    elif selected_date.month == 1:
        next_month   = datetime.date( year=selected_date.year   , month=selected_date.month+1 , day=1 )
        last_month   = datetime.date( year=selected_date.year-1 , month=12 ,                    day=1 )
    else:
        next_month   = datetime.date( year=selected_date.year   , month=selected_date.month+1 , day=1 )
        last_month   = datetime.date( year=selected_date.year   , month=selected_date.month-1 , day=1 )
    
    return last_month, next_month

