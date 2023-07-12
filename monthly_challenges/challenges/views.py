from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenge_dict = {
    'january':'Not eat meat for a month every day!',
    'february':'Sleep at least 8 hour every day!',
    'march':'Walk at least 20 min every day!',
    'april':'Learn django every day!',
    'may':'Not eat meat for a month every day!',
    'june':'Sleep at least 8 hour every day!',
    'july':'Walk at least 20 min every day!',
    'august':'Learn django every day!',
    'september':'Not eat meat for a month every day!',
    'october':'Sleep at least 8 hour every day!',
    'november':'Walk at least 20 min every day!',
    'december':'Learn django every day!',
}


def monthly_challenge_number(request, month):
    months = list(monthly_challenge_dict.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month!')
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect(reverse("month-challenge",args=[redirect_month]))

# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenge_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This is not a month")