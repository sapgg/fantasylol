from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect

from .forms import PointForm
# Create your views here.
def home(request):
    form = PointForm(request.POST or None)

    #get vars from here later?
    if form.is_valid():
        #summoner_name = form.cleaned_data['summoner_name']

        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/search/')

    return render_to_response("point.html",
                              locals(),
                              context_instance=RequestContext(request))

def search(request):

    return render_to_response("search.html",
                              locals(),
                              context_instance=RequestContext(request))