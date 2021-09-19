
from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from ads.models import ads , catugry
from django.urls import reverse_lazy
from . forms import *
from user_profile.models import user_details
from django.core.paginator import Paginator

def by_catugry(request ):
    order_by_data = request.GET.get('order_by_options_data' , '-create_date' )
    catugry_1 = request.GET.get('cat')
    query2 = request.GET.get('query')
    catugry_1 = request.GET.get('cat')
    query=""
    if request.method == 'GET':
        if catugry_1 is not None or "" :
            for key  in request.GET :
                if key != 'page' or key!= 'order_by_options_data' :
                    query="{}={}&".format(key , request.GET.get(key))+query
                else:pass
            by_catugry_2_complet=ads.objects.filter(main_id=catugry_1).order_by(order_by_data)
            # by_catugry_2_complet=ads.objects.select_related('main_id').get(main_id=catugry_1).order_by(order_by_data)

            paginator = Paginator (by_catugry_2_complet ,2 ) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            by_catugry_2 = paginator.get_page(page_number)
            print(query)
    context = {
        'by_catugry_2' : by_catugry_2 ,
        'catugry_1':catugry_1 ,
        'query':query,
        'order_by_data':order_by_data,
    }
    return render(request, 'by_catugry.html',context)





def by_main_all(request , main_id_):
    try:
        user=request.user
        user_favoret=get_object_or_404(user_details , user=user).favoret_ads.all()
    except:pass
    general_search_form = general()
    order_by_form = order_by()
    main_id_=main_id_
    general_search_form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_ , sub_id=None).order_by('name')
    general_search_form.fields['end'].queryset = catugry.objects.none()
    general_search_form.fields['last'].queryset = catugry.objects.none()
    main_catugry_q_complet=ads.objects.filter(main_id=main_id_)
    paginator = Paginator (main_catugry_q_complet ,5 ) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    main_catugry_q = paginator.get_page(page_number)
    try:
        context = {
            'main_catugry_q' : main_catugry_q ,
            'general_search_form' : general_search_form,
            'main_id_':main_id_,
            'order_by_form':order_by_form,
            'user_favoret':user_favoret ,
        }
        print("aaaaa")
    except:
        context = {
            'main_catugry_q' : main_catugry_q ,
            'general_search_form' : general_search_form,
            'main_id_':main_id_,
            'order_by_form':order_by_form,
        }
    return render(request, 'by_main_all.html',context)

