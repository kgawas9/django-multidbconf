from django.shortcuts import render, HttpResponse

from i3l_automation.models import I3lBotmaster

def home(request):
    entries = I3lBotmaster.objects.all()
    print(entries)

    for entry in entries:
        print(" | ".join(str(getattr(entry, field.name)) for field in entry._meta.fields))

    context = {
        'entries': entries
    }
    return render(request, 'home.html', context=context)
