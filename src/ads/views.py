from django.shortcuts import render , HttpResponse
from django.shortcuts import get_object_or_404 , redirect
from . models import *
from user_profile.models import user_details
from . forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from search.forms import order_by_no_ajax


from django.urls import reverse_lazy
# cat=""# Empty variable use like signal and i think it is not important but i'm afraid to delete it
# Create your views here.
def all_ads(request):
    try:
        if request.user.id != None :
            user=request.user.id
            user_favoret=get_object_or_404(user_details , user=user).favoret_ads.id()
        else:pass
    except:pass

    order_by_no_ajax_get = order_by_no_ajax ()
    order_by_data = request.GET.get('order_by_options', '-create_date' )
    order_by_no_ajax_get.fields["order_by_options"].choices



    ads_all_complet=ads.objects.only('title','description','ad_option','img').order_by(order_by_data)
    paginator = Paginator(ads_all_complet ,5 ) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    ads_all = paginator.get_page(page_number)
    try:
        context = {'ads_all' : ads_all , 'order_by_no_ajax_get':order_by_no_ajax_get,'order_by_data':order_by_data,'user_favoret':user_favoret}
    except:
        context = {'ads_all' : ads_all , 'order_by_no_ajax_get':order_by_no_ajax_get,'order_by_data':order_by_data,}
    return render(request , 'all.html' , context)
    #########################################f################################
def ads_detail(request , id):
    detail=get_object_or_404(ads , id=id)
    sub_form_id = str(detail.sub.id)
    try:
        user=request.user
        user_favoret=get_object_or_404(user_details , user=user).favoret_ads.all()
    except:pass

    forms_={
        '44': db_car , '45' : db_car , '46' : db_motorcycles, '47' : db_car_spare_parts,
        '49': db_Boats , '48' : db_heavy_trucks,
        '51': db_mobile_phones,
        '52': db_mobile_accessories ,
        '205' : db_properties,'204' : db_properties ,'212' : db_properties ,'210' : db_properties ,'211' : db_properties ,'207' : db_properties  ,'208' : db_properties_ecommer  ,'209' : db_properties_ecommer  ,'206' : db_properties_buildings_lands ,
        "213" : db_jops_services  ,"214" : db_jops_services ,"215" : db_jops_services ,"216" : db_jops_services ,"217" : db_jops_services ,"218" : db_jops_services ,"219" : db_jops_services ,"220" : db_jops_services ,"221" : db_jops_services ,"222" : db_jops_services ,"261" : db_jops_services ,"262" : db_jops_services ,"263" : db_jops_services ,"264" : db_jops_services ,"265" : db_jops_services ,"266" : db_jops_services ,"267" : db_jops_services ,"268" : db_jops_services ,"269" : db_jops_services ,"270" : db_jops_services ,"271" : db_jops_services ,"272" : db_jops_services ,"273" : db_jops_services ,"274" : db_jops_services ,"275" : db_jops_services ,"276" : db_jops_services ,"277" : db_jops_services ,"278" : db_jops_services ,"279" : db_jops_services ,"280" : db_jops_services ,"281" : db_jops_services ,"282" : db_jops_services ,"283" : db_jops_services ,"284" : db_jops_services ,"285" : db_jops_services ,"286" : db_jops_services  ,
        "203" : db_furnisher ,"194" : db_furnisher ,"199" : db_furnisher ,"200" : db_furnisher ,"201" : db_furnisher ,"198" : db_furnisher ,"197" : db_furnisher ,"202" : db_furnisher ,"196" : db_furnisher ,"195" : db_furnisher ,
        "246" : db_pets ,"247" : db_pets ,"248" : db_pets ,"249" : db_pets ,"250" : db_pets ,
        "54" : db_general,"55" : db_general,"56" : db_general,"57" : db_general,"223" : db_general,"224" : db_general,"225" : db_general,"226" : db_general,"227" : db_general,"228" : db_general,"229" : db_general,"230" : db_general,"231" : db_general,"232" : db_general,"233" : db_general,"234" : db_general,"235" : db_general,"236" : db_general,"237" : db_general,"238" : db_general,"239" : db_general,"240" : db_general,"241" : db_general,"242" : db_general,"243" : db_general,"244" : db_general,"245" : db_general,
        "287" : db_general,"288" : db_general,"289" : db_general,"290" : db_general,"291" : db_general,"292" : db_general,"293" : db_general,"294" : db_general,"295" : db_general,"296" : db_general,"297" : db_general,"251" : db_general,"252" : db_general,"253" : db_general,"254" : db_general,"255" : db_general,"256" : db_general,
    }
    if sub_form_id in forms_ and check_is_number(sub_form_id) == True :
        details_form=forms_[sub_form_id]
        detail_exet=get_object_or_404(details_form , ad_id=id)
        all_field={}
        for field in details_form._meta.fields :
            if field.name != 'id' and field.name != 'ad_id' :
                field_val=getattr(detail_exet , field.name )
                if field_val != None and field_val != "" and field_val != False :
                    all_field[field.name] = field_val

    else:details_form=''
    try:

        try:
            context={'detail':detail , 'all_field':all_field,'user_favoret':user_favoret}
        except:context={'detail':detail , 'all_field':all_field,}
    except:
        try: context={'detail':detail ,'user_favoret':user_favoret}
        except:context={'detail':detail }


    return render(request,'detail.html', context)
    #########################################################################
    # THIS Function USE TO CHANGE THE EXTENSION FORMS FOR VARIABLE OPTIONS
    # LIKE SOME FIELDS FOR CARS ADS AND ANTHER FOR MOBILE ADS AND FOR JOB ADS
        # FOR MORE DETAILS {CARS FIELDS :Model , Model Year ,Kilometers  ,
        # Transmission Type ,Body Type ,Engine Capacity (CC)}
    # FOR MORE DETAILS {MOPILE FIELDS :Brand , RAM , processor Model }
    ###############
    # HOW IT WORK #
    ###############
    # 1- make ajax Function to return the id of chosen category if we have it
    #    and that to selected The right fields for the chosen category
    #    If the identifier is 8, then this means that the user chooses cars ads
    #    and so on for each category number
    # 2-and if the category doesn't have special fields then return signalf context as zero
    # finally  if signalf context == zero there are no special fields for this ad
def check_is_number(number):
    if number != '0'and number != "0.0" :
        try:
            if float (number):return True
        except:return False
    else :return False

def change_form (request):
    sub_form_id = request.GET.get('subId')
    # if int(sub_form_id) in range (213 , 286) :
    #     sub_form_id= "213"
    forms_={
        '44' : car () , '45' : car () , '46' : motorcycles (), '47' : car_spare_parts (),
        '49' : Boats() , '48' : heavy_trucks (),
        '51' : mobile_phones (),
        '52' : mobile_accessories () ,
        '205' : properties (),'204' : properties (),'212' : properties (),'210' : properties (),'211' : properties (),'207' : properties () ,'208' : properties_ecommer () ,'209' : properties_ecommer () ,'206' : properties_buildings_lands () ,
        "213" : jops_services () ,"214" : jops_services (),"215" : jops_services (),"216" : jops_services (),"217" : jops_services (),"218" : jops_services (),"219" : jops_services (),"220" : jops_services (),"221" : jops_services (),"222" : jops_services (),"261" : jops_services (),"262" : jops_services (),"263" : jops_services (),"264" : jops_services (),"265" : jops_services (),"266" : jops_services (),"267" : jops_services (),"268" : jops_services (),"269" : jops_services (),"270" : jops_services (),"271" : jops_services (),"272" : jops_services (),"273" : jops_services (),"274" : jops_services (),"275" : jops_services (),"276" : jops_services (),"277" : jops_services (),"278" : jops_services (),"279" : jops_services (),"280" : jops_services (),"281" : jops_services (),"282" : jops_services (),"283" : jops_services (),"284" : jops_services (),"285" : jops_services (),"286" : jops_services () ,
        "203" : furnisher () ,"194" : furnisher () ,"199" : furnisher () ,"200" : furnisher () ,"201" : furnisher () ,"198" : furnisher () ,"197" : furnisher () ,"202" : furnisher () ,"196" : furnisher () ,"195" : furnisher () ,
        "246" : pets () ,"247" : pets () ,"248" : pets () ,"249" : pets () ,"250" : pets () ,
        "54" : general (),"55" : general (),"56" : general (),"57" : general (),"223" : general (),"224" : general (),"225" : general (),"226" : general (),"227" : general (),"228" : general (),"229" : general (),"230" : general (),"231" : general (),"232" : general (),"233" : general (),"234" : general (),"235" : general (),"236" : general (),"237" : general (),"238" : general (),"239" : general (),"240" : general (),"241" : general (),"242" : general (),"243" : general (),"244" : general (),"245" : general (),
        "287" : general (),"288" : general (),"289" : general (),"290" : general (),"291" : general (),"292" : general (),"293" : general (),"294" : general (),"295" : general (),"296" : general (),"297" : general (),"251" : general (),"252" : general (),"253" : general (),"254" : general (),"255" : general (),"256" : general (),
    }
    if sub_form_id in forms_ and check_is_number(sub_form_id) == True :
        details_form=forms_[sub_form_id]
    else:details_form=''
    context2 ={
        'details_form':details_form,
        'signalf' :0  #variable use like signal to make me actually know is there sub_form_id variable come with response or not
    }
    return render (request , 'change_form.html' , context2)
    #########################################################################







def creat_ads(request):
    signalf=0
    if request.method =='POST':
        form = adsform(request.POST , request.FILES )
        sub_form_id=form.data['sub']
        forms_= {
        '44' : car  , '45' : car  , '46' : motorcycles , '47' : car_spare_parts ,
        '49' : Boats , '48' : heavy_trucks ,
        '51' : mobile_phones ,
        '52' : mobile_accessories  ,
        '205' : properties ,'204' : properties ,'212' : properties ,'210' : properties ,'211' : properties ,'207' : properties  ,'208' : properties_ecommer  ,'209' : properties_ecommer  ,'206' : properties_buildings_lands  ,
        "213" : jops_services  ,"214" : jops_services ,"215" : jops_services ,"216" : jops_services ,"217" : jops_services ,"218" : jops_services ,"219" : jops_services ,"220" : jops_services ,"221" : jops_services ,"222" : jops_services ,"261" : jops_services ,"262" : jops_services ,"263" : jops_services ,"264" : jops_services ,"265" : jops_services ,"266" : jops_services ,"267" : jops_services ,"268" : jops_services ,"269" : jops_services ,"270" : jops_services ,"271" : jops_services ,"272" : jops_services ,"273" : jops_services ,"274" : jops_services ,"275" : jops_services ,"276" : jops_services ,"277" : jops_services ,"278" : jops_services ,"279" : jops_services ,"280" : jops_services ,"281" : jops_services ,"282" : jops_services ,"283" : jops_services ,"284" : jops_services ,"285" : jops_services ,"286" : jops_services  ,
        "203" : furnisher  ,"194" : furnisher  ,"199" : furnisher  ,"200" : furnisher  ,"201" : furnisher  ,"198" : furnisher  ,"197" : furnisher  ,"202" : furnisher  ,"196" : furnisher  ,"195" : furnisher  ,
        "246" : pets  ,"247" : pets  ,"248" : pets  ,"249" : pets  ,"250" : pets  ,
        "54" : general ,"55" : general ,"56" : general ,"57" : general ,"223" : general ,"224" : general ,"225" : general ,"226" : general ,"227" : general ,"228" : general ,"229" : general ,"230" : general ,"231" : general ,"232" : general ,"233" : general ,"234" : general ,"235" : general ,"236" : general ,"237" : general ,"238" : general ,"239" : general ,"240" : general ,"241" : general ,"242" : general ,"243" : general ,"244" : general ,"245" : general ,
        "287" : general ,"288" : general ,"289" : general ,"290" : general ,"291" : general ,"292" : general ,"293" : general ,"294" : general ,"295" : general ,"296" : general ,"297" : general ,"251" : general ,"252" : general ,"253" : general ,"254" : general  ,"255" : general ,"256" : general
    }
        if sub_form_id in forms_ and check_is_number(sub_form_id) == True:
            details_form=forms_[sub_form_id] (request.POST)
            signalf=1
        else: signalf=0
        if signalf == 1 :
            if form.is_valid() and details_form.is_valid() :
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                new_details_form=details_form.save(commit=False)

#######################333
############################
############################33
                # new_form.description= {**form.data, **details_form.data}
                new_form.description= details_form.data

                #######################333
############################
############################33


                new_details_form.ad_id=form.save()
                form.save()
                details_form.save()
                return redirect('/')
                form.data
            else:
                main_id_creat=form.data['main']
                sub_id_creat=form.data['sub']
                end_id_creat=form.data['end']
                if main_id_creat == "" : main_id_creat=0
                else: main_id_creat=form.data['main']
                if sub_id_creat == "" : sub_id_creat=0
                else: sub_id_creat=form.data['sub']
                if end_id_creat == "" : end_id_creat=0
                else: end_id_creat=form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
                ).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
                ).order_by('name')
                context = {
                    'form': form,
                    'details_form': details_form,
                    'signalf': signalf,
                }
                pass
        else:
            if form.is_valid() :
                new_form = form.save(commit=False)  # تاخير حفظ الفورم حتي تعديلها
                new_form.user=request.user
                form.save()
                return redirect('/')
            else:
                main_id_creat=form.data['main']
                sub_id_creat=form.data['sub']
                end_id_creat=form.data['end']
                if main_id_creat == "" : main_id_creat=0
                else: main_id_creat=form.data['main']
                if sub_id_creat == "" : sub_id_creat=0
                else: sub_id_creat=form.data['sub']
                if end_id_creat == "" : end_id_creat=0
                else: end_id_creat=form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat , sub_id=None
                ).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat ,sub_id=sub_id_creat ,end_id=end_id_creat
                ).order_by('name')
    else:
        form= adsform()
        form.fields['sub'].queryset = catugry.objects.none()
        form.fields['end'].queryset = catugry.objects.none()
        form.fields['last'].queryset = catugry.objects.none()
    try:
        context = {
            'form': form ,
            'details_form': details_form,
            'signalf': signalf,
        }
    except :
        context = {
        'form': form ,
        'signalf': signalf,
    }
    return render (request , 'creat.html' , context)
    ##################################################  edit_ads  #######################


def load_sub(request):
    main_idt = request.GET.get('main')
    sub_idt = request.GET.get('sub')
    end_idt = request.GET.get('end')
    if main_idt :
        sub = catugry.objects.filter(main_id=main_idt , sub_id=None).order_by('id')
        end=[]
        last=[]
    else:
        sub=[]
        end=[]
        last=[]

    if sub_idt :
        end = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=None).order_by('id')
        sub=[]
        last=[]
    else:
        end=[]
        last=[]
    if end_idt:
        last = catugry.objects.filter( main_id=main_idt ,sub_id=sub_idt ,end_id=end_idt).order_by('id')
        sub=[]
        end=[]
    else:
        last=[]
    context={
        'sub': sub ,
        'end': end ,
        'last': last,

    }
    return render(request, 'load_sub_list_options.html',context)
