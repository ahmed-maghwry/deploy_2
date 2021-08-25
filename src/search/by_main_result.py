from django.shortcuts import get_object_or_404 , redirect
from ads.models import *
from django.shortcuts import render 
from .forms import * 
from django.core.paginator import Paginator
from django.db.models import Q
from operator import __or__ as OR1
from functools import reduce
import json



def change_form_search (request):
    range_price_form = price_form()
    sub_form_id = request.GET.get('subId')
    main_form_id = request.GET.get('mainId')
    
    forms_={
        '44' : car_search () , '45' : car_search () , '46' : motorcycles_search (), '47' : car_spare_parts_search (),
        '49' : Boats_search() , '48' : heavy_trucks_search (),
        '51' : mobile_phones_search (),
        '52' : mobile_accessories_search () ,
        '205' : properties_search (),'204' : properties_search (),'212' : properties_search (),'210' : properties_search (),'211' : properties_search (),'207' : properties_search () ,'208' : properties_ecommer_search () ,'209' : properties_ecommer_search () ,'206' : properties_buildings_lands_search () ,
        "213" : jops_services_search () ,"214" : jops_services_search (),"215" : jops_services_search (),"216" : jops_services_search (),"217" : jops_services_search (),"218" : jops_services_search (),"219" : jops_services_search (),"220" : jops_services_search (),"221" : jops_services_search (),"222" : jops_services_search (),"261" : jops_services_search (),"262" : jops_services_search (),"263" : jops_services_search (),"264" : jops_services_search (),"265" : jops_services_search (),"266" : jops_services_search (),"267" : jops_services_search (),"268" : jops_services_search (),"269" : jops_services_search (),"270" : jops_services_search (),"271" : jops_services_search (),"272" : jops_services_search (),"273" : jops_services_search (),"274" : jops_services_search (),"275" : jops_services_search (),"276" : jops_services_search (),"277" : jops_services_search (),"278" : jops_services_search (),"279" : jops_services_search (),"280" : jops_services_search (),"281" : jops_services_search (),"282" : jops_services_search (),"283" : jops_services_search (),"284" : jops_services_search (),"285" : jops_services_search (),"286" : jops_services_search () ,
        "203" : furnisher_search () ,"194" : furnisher_search () ,"199" : furnisher_search () ,"200" : furnisher_search () ,"201" : furnisher_search () ,"198" : furnisher_search () ,"197" : furnisher_search () ,"202" : furnisher_search () ,"196" : furnisher_search () ,"195" : furnisher_search () ,
        "246" : pets_search () ,"247" : pets_search () ,"248" : pets_search () ,"249" : pets_search () ,"250" : pets_search () ,
        "54" : general_search (),"55" : general_search (),"56" : general_search (),"57" : general_search (),"223" : general_search (),"224" : general_search (),"225" : general_search (),"226" : general_search (),"227" : general_search (),"228" : general_search (),"229" : general_search (),"230" : general_search (),"231" : general_search (),"232" : general_search (),"233" : general_search (),"234" : general_search (),"235" : general_search (),"236" : general_search (),"237" : general_search (),"238" : general_search (),"239" : general_search (),"240" : general_search (),"241" : general_search (),"242" : general_search (),"243" : general_search (),"244" : general_search (),"245" : general_search (),
        "287" : general_search (),"288" : general_search (),"289" : general_search (),"290" : general_search (),"291" : general_search (),"292" : general_search (),"293" : general_search (),"294" : general_search (),"295" : general_search (),"296" : general_search (),"297" : general_search (),"251" : general_search (),"252" : general_search (),"253" : general_search (),"254" : general_search () ,"255" : general_search (),"256" : general_search ()
    }
    if sub_form_id in forms_ :
        main_form_search=forms_[sub_form_id]  
    else:main_form_search=''
    context2 ={
        'main_form_search':main_form_search,
        'range_price_form':range_price_form,
        'sub_form_id':sub_form_id,
    }
    return render (request , 'change_form_search.html' , context2)

def check_is_number(number):
    
    if number != '0'and number != "0.0" :
        try:
            if float (number):return True
        except:return False
    else :return False

def by_main_result(request):
    main_id = request.GET.get('main')
    search_db_id = request.GET.get('sub')

    order_by = request.GET.get('order_by_options')
    query="" #IT IS USE INLINE 74 TO MAKE QUERY

    

    db_list={'':'no_form' ,
        '44' : 'db_car' , '45' : 'db_car' , '46' : 'db_motorcycles', '47' : 'db_car_spare_parts',
        '49' : 'db_Boat' , '48' : 'db_heavy_trucks',
        '51' : 'db_mobile_phones',
        '52' : 'db_mobile_accessories' ,
        '205' : 'db_properties','204' : 'db_properties' ,'212' : 'db_properties' ,'210' : 'db_properties' ,'211' : 'db_properties' ,'207' : 'db_properties'  ,'208' : 'db_properties_ecommer'  ,'209' : 'db_properties_ecommer'  ,'206' : 'db_properties_buildings_lands' ,
        "213" : 'db_jops_services'  ,"214" : 'db_jops_services' ,"215" : 'db_jops_services' ,"216" : 'db_jops_services' ,"217" : 'db_jops_services' ,"218" : 'db_jops_services' ,"219" : 'db_jops_services' ,"220" : 'db_jops_services' ,"221" : 'db_jops_services' ,"222" : 'db_jops_services' ,"261" : 'db_jops_services' ,"262" : 'db_jops_services' ,"263" : 'db_jops_services' ,"264" : 'db_jops_services' ,"265" : 'db_jops_services' ,"266" : 'db_jops_services' ,"267" : 'db_jops_services' ,"268" : 'db_jops_services' ,"269" : 'db_jops_services' ,"270" : 'db_jops_services' ,"271" : 'db_jops_services' ,"272" : 'db_jops_services' ,"273" : 'db_jops_services' ,"274" : 'db_jops_services' ,"275" : 'db_jops_services' ,"276" : 'db_jops_services' ,"277" : 'db_jops_services' ,"278" : 'db_jops_services' ,"279" : 'db_jops_services' ,"280" : 'db_jops_services' ,"281" : 'db_jops_services' ,"282" : 'db_jops_services' ,"283" : 'db_jops_services' ,"284" : 'db_jops_services' ,"285" : 'db_jops_services' ,"286" : 'db_jops_services'  ,
        "203" : 'db_furnisher' ,"194" : 'db_furnisher' ,"199" : 'db_furnisher' ,"200" : 'db_furnisher' ,"201" : 'db_furnisher' ,"198" : 'db_furnisher' ,"197" : 'db_furnisher' ,"202" : 'db_furnisher' ,"196" : 'db_furnisher' ,"195" : 'db_furnisher' ,
        "246" : 'db_pets' ,"247" : 'db_pets' ,"248" : 'db_pets' ,"249" : 'db_pets' ,"250" : 'db_pets' ,
        "54" : 'db_general',"55" : 'db_general',"56" : 'db_general',"57" : 'db_general',"223" : 'db_general',"224" : 'db_general',"225" : 'db_general',"226" : 'db_general',"227" : 'db_general',"228" : 'db_general',"229" : 'db_general',"230" : 'db_general',"231" : 'db_general',"232" : 'db_general',"233" : 'db_general',"234" : 'db_general',"235" : 'db_general',"236" : 'db_general',"237" : 'db_general',"238" : 'db_general',"239" : 'db_general',"240" : 'db_general',"241" : 'db_general',"242" : 'db_general',"243" : 'db_general',"244" : 'db_general',"245" : 'db_general',
        "287" : 'db_general',"288" : 'db_general',"289" : 'db_general',"290" : 'db_general',"291" : 'db_general',"292" : 'db_general',"293" : 'db_general',"294" : 'db_general',"295" : 'db_general',"296" : 'db_general',"297" : 'db_general',"251" : 'db_general',"252" : 'db_general',"253" : 'db_general',"254" : 'db_general',"255" : 'db_general',"256" : 'db_general',
    }
    


    if check_is_number(search_db_id)==True :
        db_search=db_list[search_db_id]
    general_search_list=[ 'main','sub' , 'end' ,'last']
    price_list=['to_price', 'from_price' ]
    signal=0
    if search_db_id !="" and search_db_id != None or main_id !="" and main_id !=None :

        if request.is_ajax() :
            query_string=''
            for key  in request.GET :
                if key != 'page'  :
                    for l in range(len(request.GET.getlist(key))) :
                        query="{}={}&".format(key , query_string.join(request.GET.getlist(key)[l]))+query
                else:pass
            if check_is_number(search_db_id)==False :
                main_catugry_q_complet=ads.objects.filter( main_id=main_id ).order_by(order_by)
            else: main_catugry_q_complet=ads.objects.filter( main_id=main_id ,sub_id=search_db_id).order_by(order_by)
            for search_key in request.GET : 
                search_value=request.GET.get(search_key)  
                if search_value != "" and search_value != None  and search_key != 'page' and search_key != 'order_by_options':
                    search_value=request.GET.get(search_key)
                    if search_key in general_search_list :
                        search_var={search_key : search_value}
                        q_list = [ Q (**{search_key: value}) for value in request.GET.getlist(search_key)]
                        or_q_list = reduce(OR1 , q_list)
                        signal=1
                        main_catugry_q_complet=main_catugry_q_complet.filter( or_q_list).order_by( order_by)
                    elif  search_key not in general_search_list and search_key not in price_list and search_value != 'on' :
                        signal=1
                        exe_search_var="{}__{}__iexact".format(db_search ,search_key)
                        q_list = [ Q (**{exe_search_var: value}) for value in request.GET.getlist(search_key)]
                        or_q_list = reduce(OR1 , q_list)
                        main_catugry_q_complet=main_catugry_q_complet.filter(or_q_list).order_by (order_by)
                    elif  search_key not in general_search_list and search_value == 'on' :
                        signal=1
                        bool_search_var="{}__{}__iexact".format(db_search ,search_key)
                        diction_bool_search_var={bool_search_var:1}
                        main_catugry_q_complet=main_catugry_q_complet.filter(** diction_bool_search_var ).order_by( order_by)
                    elif  search_key in price_list and check_is_number(search_value) == True  :

                        if search_key == 'from_price'  :
                            signal=1
                            bool_search_var="{}__{}__gte".format(db_search , 'price')
                            diction_bool_search_var={bool_search_var : search_value}
                            main_catugry_q_complet=main_catugry_q_complet.filter(** diction_bool_search_var ).order_by(order_by)
                        elif search_key == 'to_price' :
                            signal=1
                            bool_search_var="{}__{}__lt".format(db_search , 'price')
                            diction_bool_search_var={bool_search_var : search_value}
                            main_catugry_q_complet=main_catugry_q_complet.filter(** diction_bool_search_var ).order_by(order_by)
            if signal == 0 :
                main_catugry_q_complet=ads.objects.filter(main_id=main_id).order_by(order_by)
                pass

        else:pass
    
    else:

        main_catugry_q_complet=ads.objects.filter(main_id=main_id).order_by(order_by)
    

    paginator = Paginator (main_catugry_q_complet ,5 ) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    main_catugry_q = paginator.get_page(page_number)
    context = {'main_catugry_q' : main_catugry_q , 'query':query , 'count':main_catugry_q_complet.count()}
    return render(request, 'by_main_result.html',context)

