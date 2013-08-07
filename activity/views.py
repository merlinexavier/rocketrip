from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from activity.models import Activity, ActivityForm


def home(request):
    if request.method == 'POST':
        # get the POST data
        name_value = request.POST.get('name', '')
        type_value = request.POST.get('type', '')
        date_value = request.POST.get('date', '')
        description_value = request.POST.get('description', '')

        # save the POST data

        activity = Activity(name=name_value,
                            type=type_value,
                            date=date_value,
                            description=description_value)

        activity.save()

        return HttpResponseRedirect('/table/')
    form = ActivityForm()
    return render(request, 'form.html', {'form': form})


def table(request):
    activities = Activity.objects.all().order_by('-date')

    return render(request, 'table.html', {'activities': activities})
