from django.shortcuts import render
import datetime
from record_store.models import Song


def index_view(request):
    context = {
        'my_name': "TYLER MAKIN DAT MONEY",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }
    return render(request, "index.html", context)
    # return HttpResponse('i love web programming')


def lyrics_view(request, song_id):
    context = {
        "song": Song.objects.get(id=song_id)

    }
    return render(request, "lyrics.html", context)
