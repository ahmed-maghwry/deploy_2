from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from . models import *
from . forms import *
from django.urls import reverse_lazy


def check_is_number(number):
    if number != '0'and number != "0.0":
        try:
            if float(number):
                return True
            else:
                pass
        except:
            return False
    else:
        return False


def edit_ads(request, id):
    ads_edit = get_object_or_404(ads, id=id)
    forms_={
        '44' : [db_car , car ]   , '45' : [db_car , car ]  , '46' : [db_motorcycles  , motorcycles] , '47' : [db_car_spare_parts ,car_spare_parts ] ,
        '49' : [db_Boats , Boats ] , '48' : [db_heavy_trucks , heavy_trucks] ,
        '51' : [db_mobile_phones , mobile_phones ] ,
        '52' : [db_mobile_accessories , mobile_accessories ]   ,
        '205' : [db_properties , properties] ,'204' : [db_properties , properties] ,'212' : [db_properties , properties] ,'210' : [db_properties , properties] ,'211' : [db_properties , properties] ,'207' : [db_properties , properties] , '208' : [db_properties_ecommer , properties_ecommer]  ,'209' : [db_properties_ecommer , properties_ecommer ]  ,'206' : [db_properties_buildings_lands , properties_buildings_lands ]  ,
        "213" : [db_jops_services , jops_services]  ,"214" : [db_jops_services , jops_services] ,"215" : [db_jops_services , jops_services] ,"216" : [db_jops_services , jops_services] ,"217" : [db_jops_services , jops_services] ,"218" : [db_jops_services , jops_services] ,"219" : [db_jops_services , jops_services] ,"220" : [db_jops_services , jops_services] ,"221" : [db_jops_services , jops_services] ,"222" : [db_jops_services , jops_services] ,"261" : [db_jops_services , jops_services] ,"262" : [db_jops_services , jops_services] ,"263" : [db_jops_services , jops_services] ,"264" : [db_jops_services , jops_services] ,"265" : [db_jops_services , jops_services] ,"266" : [db_jops_services , jops_services] ,"267" : [db_jops_services , jops_services] ,"268" : [db_jops_services , jops_services] ,"269" : [db_jops_services , jops_services] ,"270" : [db_jops_services , jops_services] ,"271" : [db_jops_services , jops_services] ,"272" : [db_jops_services , jops_services] ,"273" : [db_jops_services , jops_services] ,"274" : [db_jops_services , jops_services] ,"275" : [db_jops_services , jops_services] ,"276" : [db_jops_services , jops_services] ,"277" : [db_jops_services , jops_services] ,"278" : [db_jops_services , jops_services] ,"279" : [db_jops_services , jops_services] ,"280" : [db_jops_services , jops_services] ,"281" : [db_jops_services , jops_services] ,"282" : [db_jops_services , jops_services] ,"283" : [db_jops_services , jops_services] ,"284" : [db_jops_services , jops_services] ,"285" : [db_jops_services , jops_services] ,"286" : [db_jops_services , jops_services]  ,
        "203" : [db_furnisher , furnisher]  ,"194" : [db_furnisher , furnisher]  ,"199" : [db_furnisher , furnisher]  ,"200" : [db_furnisher , furnisher]  ,"201" : [db_furnisher , furnisher]  ,"198" : [db_furnisher , furnisher]  ,"197" : [db_furnisher , furnisher]  ,"202" : [db_furnisher , furnisher]  ,"196" : [db_furnisher , furnisher]  ,"195" : [db_furnisher , furnisher]  ,
        "246" : [db_pets , pets] ,"247" :  [db_pets , pets]  ,"248" :  [db_pets , pets]  ,"249" :  [db_pets , pets]  ,"250" :  [db_pets , pets]  ,
        "54" : [db_general , general] ,"55" : [db_general , general] ,"56" : [db_general , general] ,"57" : [db_general , general] ,"223" : [db_general , general] ,"224" : [db_general , general] ,"225" : [db_general , general] ,"226" : [db_general , general] ,"227" : [db_general , general] ,"228" : [db_general , general] ,"229" : [db_general , general] ,"230" : [db_general , general] ,"231" : [db_general , general] ,"232" : [db_general , general] ,"233" : [db_general , general] ,"234" : [db_general , general] ,"235" : [db_general , general] ,"236" : [db_general , general] ,"237" : [db_general , general] ,"238" : [db_general , general] ,"239" : [db_general , general] ,"240" : [db_general , general] ,"241" : [db_general , general] ,"242" : [db_general , general] ,"243" : [db_general , general] ,"244" : [db_general , general] ,"245" : [db_general , general] ,
        "287" : [db_general , general] ,"288" : [db_general , general] ,"289" : [db_general , general] ,"290" : [db_general , general] ,"291" : [db_general , general] ,"292" : [db_general , general] ,"293" : [db_general , general] ,"294" : [db_general , general] ,"295" : [db_general , general] ,"296" : [db_general , general] ,"297" : [db_general , general] ,"251" : [db_general , general] ,"252" : [db_general , general] ,"253" : [db_general , general] ,"254" : [db_general , general]  ,"255" : [db_general , general] ,"256" : [db_general , general] 
            }
    signalf = 0

    if request.method == 'POST':
        form = adsform(request.POST, request.FILES, instance=ads_edit)
        sub_form_id = form.data['sub']
        
        if sub_form_id in forms_ and check_is_number(sub_form_id) == True:
            details_form_no_request = forms_[
                sub_form_id][1]  # 1 in list is FORM
            details_db_request = forms_[sub_form_id][0]  # 0 in list is DB NAME
            try:
                # it is take model name not form
                ads_exe_edit = get_object_or_404(
                    details_db_request, ad_id=ads_edit)
                details_form = details_form_no_request(
                    request.POST, instance=ads_exe_edit)
                signalf = 1
            except:
                details_form = details_form_no_request(request.POST)
                signalf = 1
        else:
            signalf = 0
        if signalf == 1:
            try:
                if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                    sub_instance_id = ads_edit.sub.id
                else:
                    pass
            except:pass
            if form.is_valid() and details_form.is_valid():
                # تاخير حفظ الفورم حتي تعديلها
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_details_form = details_form.save(commit=False)
                new_details_form.ad_id = form.save()
                try:
                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    # it is take model name not form
                    ads_exe_old = get_object_or_404(
                        details_db_request, ad_id=ads_edit)
                    ads_exe_old.delete()
                except:
                    pass
                form.save()
                details_form.save()
                return redirect('/')
            else:
                main_id_creat = form.data['main']
                sub_id_creat = form.data['sub']
                end_id_creat = form.data['end']
                if main_id_creat == "":
                    main_id_creat = 0
                else:
                    main_id_creat = form.data['main']
                if sub_id_creat == "":
                    sub_id_creat = 0
                else:
                    sub_id_creat = form.data['sub']
                if end_id_creat == "":
                    end_id_creat = 0
                else:
                    end_id_creat = form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(main_id=main_id_creat, sub_id=None
                                                                     ).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat
                                                                      ).order_by('name')
                context = {
                    'form': form,
                    'details_form': details_form,
                    'signalf': signalf,
                }
                pass
        else:
            try:
                if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                    sub_instance_id = ads_edit.sub.id
                else:
                    pass
            except:
                pass
            if form.is_valid():
                # تاخير حفظ الفورم حتي تعديلها
                new_form = form.save(commit=False)
                new_form.user = request.user
                try:

                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    # it is take model name not form
                    ads_exe_old = get_object_or_404(
                        details_db_request, ad_id=ads_edit)
                    ads_exe_old.delete()
                except:
                    pass
                form.save()
                return redirect('/')
            else:
                main_id_creat = form.data['main']
                sub_id_creat = form.data['sub']
                end_id_creat = form.data['end']
                if main_id_creat == "":
                    main_id_creat = 0
                else:
                    main_id_creat = form.data['main']
                if sub_id_creat == "":
                    sub_id_creat = 0
                else:
                    sub_id_creat = form.data['sub']
                if end_id_creat == "":
                    end_id_creat = 0
                else:
                    end_id_creat = form.data['end']
                form.fields['sub'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=None).order_by('name')
                form.fields['end'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
                form.fields['last'].queryset = catugry.objects.filter(
                    main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat).order_by('name')
    else:
        form = adsform(instance=ads_edit)
        main_id_creat = ads_edit.main
        sub_id_creat = ads_edit.sub
        end_id_creat = ads_edit.end
        if main_id_creat == "" or main_id_creat == None:

            main_id_creat = 0
            form.fields['sub'].queryset = catugry.objects.none()
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else:
            main_id_creat = ads_edit.main
        if sub_id_creat == "" or sub_id_creat == None:
            sub_id_creat = 0
            form.fields['end'].queryset = catugry.objects.none()
            form.fields['last'].queryset = catugry.objects.none()
        else:
            sub_id_creat = ads_edit.sub
        if end_id_creat == "" or end_id_creat == None:
            end_id_creat = 0
            form.fields['last'].queryset = catugry.objects.none()
        else:
            end_id_creat = ads_edit.end
        form.fields['sub'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=None).order_by('name')
        form.fields['end'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=sub_id_creat, end_id=None).order_by('name')
        form.fields['last'].queryset = catugry.objects.filter(
            main_id=main_id_creat, sub_id=sub_id_creat, end_id=end_id_creat).order_by('name')
        try:
            if ads_edit.sub.id != '' or ads_edit.sub.id != None:
                sub_instance_id = ads_edit.sub.id
                
                if str(sub_instance_id) in forms_ and check_is_number(sub_instance_id) == True:
                    details_form_no_request = forms_[
                        str(sub_instance_id)][1]  # 1 in list is FORM
                    details_db_request = forms_[
                        str(sub_instance_id)][0]  # 0 in list is DB NAME
                    try:
                        # it is take model name not form
                        ads_exe_edit = get_object_or_404(
                            details_db_request, ad_id=ads_edit)
                        details_form = details_form_no_request(
                            instance=ads_exe_edit)
                        signalf = 1
                    except:
                        pass
                else:
                    pass
            else:
                pass
        except:
            pass
    try:
        context = {
            'form': form,
            'details_form': details_form,
            'signalf': signalf,
        }
    except:
        context = {
            'form': form,
            'signalf': signalf,
        }
    return render(request, 'edit.html', context)
