from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings import choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_listed=True)[:3]

    context = {
        'listings': listings,
        'state_choices': choices.states,
        'bedroom_choices': choices.bedrooms,
        'price_choices': choices.prices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvpRealtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
