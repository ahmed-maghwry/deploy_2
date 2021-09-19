from django.shortcuts import render ,HttpResponse
from django.shortcuts import get_object_or_404
from ads.models import ads
from .models import user_details
from allauth.account.forms import ChangePasswordForm
# from django.contrib.auth.models import User

def favoret(request) :
    now_user=request.user
    user_details.objects.get_or_create( user_id=now_user.id)
    ad_id=request.GET.get('ad_id')
    user_detail=get_object_or_404(user_details , user=now_user)
    ads_fav=get_object_or_404(ads , id=ad_id)
    if user_detail.favoret_ads.all().filter(id=ad_id).exists() :
        user_detail.favoret_ads.remove(ad_id)
        maseg='remove'
    else :
        user_detail.favoret_ads.add(ad_id)
        maseg='add'
    return HttpResponse(maseg)


def user_profile_sittings (request  ) :
    change_password=ChangePasswordForm()
    user=request.user
    # user_ads=get_user_ads(user)
    user_favoret=get_object_or_404(user_details.objects.only('favoret_ads') , user_id=user).favoret_ads.only('title','description','ad_option','img')
    context={ 'user_favoret':user_favoret , 'change_password':change_password  }
    return render(request , 'user_profile_sittings.html' , context)


def get_user_ads (user):
    user_ads_filter=ads.objects.filter(user=user )
    return user_ads_filter

