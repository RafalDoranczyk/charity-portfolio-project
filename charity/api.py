import json
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Institution, Donation, Category


def CategoriesAPI(request):
    ids = json.loads(request.GET.get('ids', None))
    num_ids = [int(i) for i in ids]
    institutions = Institution.objects.filter(pk__in=num_ids)
    data = {
        'institutions': serializers.serialize('json', institutions)
    }
    return JsonResponse(data)


def validate_donation():
    pass


@csrf_exempt
def DonationAPI(request):
    data = json.loads(request.POST.get('data', None))
    quantity = int(data['bagsNumber'])
    pk = data['pickedInstitution']['pk']
    institution = Institution.objects.get(pk=pk)
    address = data['address']['address']
    phone_number = data['address']['phone']
    city = data['address']['city']
    zip_code = data['address']['postcode']
    pick_up_date = data['address']['data']
    pick_up_time = data['address']['time']
    pick_up_comment = data['address']['more_info']
    user = request.user
    try:
        donation = Donation.objects.create(quantity=quantity, address=address, phone_number=phone_number, city=city, zip_code=zip_code,
                                pick_up_date=pick_up_date,pick_up_time=pick_up_time, pick_up_comment=pick_up_comment,
                                institution=institution, user=user)
        for i in data['pc']:
            category = Category.objects.get(pk=int(i))
            donation.categories.add(category)
        return JsonResponse({'status': 'ok'})
    except Exception as exc:
        return JsonResponse({'msg': exc.args})


def InstitutionsAPI(request):
    id = json.loads(request.GET.get('id', None))
    inst = Institution.objects.filter(institution_type=id)
    dataa = []
    for i in inst:
        categories = Category.objects.filter(institution=i)
        category_names = []
        for j in categories:
            category_names.append(j.name)
        dataa.append({'pk': i.pk, 'name': i.name, 'description': i.description, 'categories': category_names})
    return JsonResponse({'inst': json.dumps(dataa)})

