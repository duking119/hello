from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge_dict = {
    'january': 'Not eat meat for a month every day!',
    'february': 'Sleep at least 8 hour every day!',
    'march': 'Walk at least 20 min every day!',
    'april': 'Learn django every day!',
    'may': 'Not eat meat for a month every day!',
    'june': 'Sleep at least 8 hour every day!',
    'july': 'Walk at least 20 min every day!',
    'august': 'Learn django every day!',
    'september': 'Not eat meat for a month every day!',
    'october': 'Sleep at least 8 hour every day!',
    'november': 'Walk at least 20 min every day!',
    'december': None
}


def index(request):
    months = list(monthly_challenge_dict.keys())
    
    return render(request,"challenges/index.html",{
        "months":months,
    })

    # for month in months:
    #     captalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{captalized_month}</a></li>"

    # response_data = f"<url>{list_items}</url>"
    # return HttpResponse(response_data)

# Create your views here.


def monthly_challenge_number(request, month):
    months = list(monthly_challenge_dict.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month!')

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenge_dict[month]
        return render(request, "challenges/challenge.html/",{
            'text': challenge_text,
            'month_name': month
        })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
