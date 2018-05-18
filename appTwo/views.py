from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.models import LogEntry, ADDITION

# from appTwo.models import User
from appTwo.forms import NewUserForm
from appTwo.models import EspTest, AccModel, GpsModel

# Create your views here.
acc_count = AccModel.objects.count()
gps_count = GpsModel.objects.count()


def index(request):
    new_acc = 'False'
    new_gps = 'False'
    acc_list = AccModel.objects.order_by('-updated')
    gps_list = GpsModel.objects.order_by('-updated')

    global acc_count
    global gps_count
    if acc_count != AccModel.objects.count():
        # global new_acc
        new_acc = 'True'
        acc_count = AccModel.objects.count()

    if gps_count != GpsModel.objects.count():
        # global new_gps
        new_gps = 'True'
        gps_count = GpsModel.objects.count()

    obj_dict = {'accVal': acc_list, 'gpsVal': gps_list, 'new_acc': new_acc, 'new_gps': new_gps, 'range10': range(10)}
    # if new_acc == 'True':
    #     input("updated")
    if request.is_ajax():
        # print(acc_count)
        return render(request, 'appTwo/indexBody.html', context=obj_dict)
    return render(request, 'appTwo/index.html', context=obj_dict)


def test(request):
    acc_list = AccModel.objects.order_by('updated').last()
    gps_list = GpsModel.objects.order_by('updated').last()
    obj_dict = {'accVal': acc_list, 'gpsVal': gps_list}
    # print('Before ajax')
    # print(gps_list.id)
    # if request.is_ajax():
    #     print('After Ajax')
    #     print(gps_list.id)
    #     return render(request, 'appTwo/testDiv.html', context=obj_dict)
    return render(request, 'appTwo/test.html', context=obj_dict)
    # return render_to_response('appTwo/test.html', context=obj_dict)


@csrf_exempt
def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form Invalid")
    return render(request, 'appTwo/users.html', {'form': form})


@csrf_exempt
def esp(request):
    if request.method == "POST":
        b = EspTest()
        print(request.POST)
        mydict = dict(request.POST.lists())
        print(mydict)
        b = EspTest(
            isTremor=mydict['isTremor'][0],
            isFall=mydict['isFall'][0],
            latValue=mydict['latValue'][0],
            longValue=mydict['longVal'][0],
            safeDist=mydict['safeDist'][0],
            isSafe=mydict['isSafe'][0],
            bpm=mydict['bpm'][0],
        )
        b.save()
        return render(request, 'appTwo/index.html')


@csrf_exempt
def acc(request):
    if request.method == "POST":
        b = AccModel()
        print(request.POST)
        mydict = dict(request.POST.lists())
        print(mydict)
        b = AccModel(
            isTremor=mydict['isTremor'][0],
            isFall=mydict['isFall'][0],
            isPressed=mydict['isPressed'][0],
        )
        b.save()
        return render(request, 'appTwo/index.html')


@csrf_exempt
def gps(request):
    if request.method == "POST":
        b = GpsModel()
        print(request.POST)
        mydict = dict(request.POST.lists())
        if mydict['isSafe'][0] == 'T':
            mydict['isSafe'][0] = 'True'
        elif mydict['isSafe'][0] == 'F':
            mydict['isSafe'][0] = 'False'
        print(mydict)
        b = GpsModel(
            latValue=mydict['latValue'][0],
            longValue=mydict['longVal'][0],
            safeDist=mydict['safeDist'][0],
            isSafe=mydict['isSafe'][0],
            bpm=mydict['bpm'][0],
        )
        b.save()
        return render(request, 'appTwo/index.html')


@csrf_exempt
def main(request):
    acc_list = AccModel.objects.order_by('-updated')[:10]
    gps_list = GpsModel.objects.order_by('-updated')[:10]
    obj_dict = {'accVal': acc_list, 'gpsVal': gps_list}
    return render(request, 'appTwo/main.html', context=obj_dict)
