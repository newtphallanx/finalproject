from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CharacterForm
from .models import Character
from .forms import gmRollerForm
from .models import red
from .models import yellow
from .models import green
from .models import purple
from .models import blue
from .models import black
from .models import dice

# adds character index
def characterIndex(request):
    #makes a list of characters
    latest_character_list = Character.objects.order_by('id')[:]
    #gets template from the edge/index
    template = loader.get_template('edge/index.html')
    context = {
        'latest_character_list': latest_character_list,
    }
    return HttpResponse(template.render(context, request))

def diceResults(request):
    resultsList = diceResults.objects.order_by('id')[::-1]
    template = loader.get_template('edge/results.html')
    centext = {
        'resultsList':resultsList,
    }
    return HttpResponse(template.render(context, request))



#get character html form
def getCharacter(request, character_id):
    #If data was obtained using post then create a form instance
    character = Character.objects.get(id=character_id)

    return render(request, 'edge/detail.html',
                  {'character' : character,
                   })

def editCharacter(request, character_id):
    form = CharacterForm()
    #If data was obtained using post then create a form instance
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        #check if valid
        if form.is_valid():
            return HttpResponseRedirect('edge/characters/')
        #otherwise make form blank
        else:
            form = CharacterForm()
    return render(request, 'edge/edit.html', {'form': form})


#add a gm dice roller view
def gmRoller(request):
    form = gmRollerForm
    if request.method == 'POST':
        form = gmRollerForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['aim'] == True
                form.cleaned_data['boost'] = form.cleaned_data['boost'] + 1
            theResults = diceResults(results = dice.aggregate(form.cleaned_data['charactersList'], form.cleaned_data['skillsList'], form.cleaned_data[diff], form.cleaned_data['reds'], form.cleaned_data['boost'], form.cleaned_data['setback']))
            theResults.save()
            return HttpResponseRedirect('edge/dice/results')
        else:
            form = gmRollerForm()
    return render(request, 'edge/gmRoller.html', {'form': form})
