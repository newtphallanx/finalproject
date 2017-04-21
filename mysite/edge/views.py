from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CharacterForm
from .models import Character
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

#get character html form
def getCharacter(request, character_id):
    #If data was obtained using post then create a form instance
    character = Character.objects.get(id=character_id)

    return render(request, 'edge/detail.html',
                  {'character' : character,
                   })

def editCharacter(request, character_id):
    form = CharacterForm()
    #commented out for now because it doesn't work
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        #check if valid
        if form.is_valid():
            return HttpResponseRedirect('edge/characters/')
        #otherwise make form blank
        else:
            form = CharacterForm()
    return render(request, 'edge/edit.html', {'form': form})
"""
#add a weapon index
def weaponIndex(request):
    return HttpResponse("This is the weapons index")

#add an armor index
def armorIndex(request):
    return HttpResponse("this is the armor index")"""

#add a character view
def characterView(request, character_id):
    return HttpResponse("You're at the character view page")

#add a character edit view
def characterEdit(request, character_id):
      #makes 404 error with exception handling
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    return render(request, 'edge/detail.html', {'character': character})

#add a weapon view
#def weaponView(request, weapon_id):
#add a player view

#add a armor view

#add a gm view
#def GMView(request
#add a party view

#add a dice roller view

#add a gm dice roller view
