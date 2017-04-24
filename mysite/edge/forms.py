from django import forms
from django.forms import ModelForm
from edge.models import Character

#making form for characters
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name','species','career','specializationTrees','soak', 'woundsThreshold', 'woundsCurrent','strainThreshold','strainCurrent','defenseRanged','defenseMelee','creator','brawn','agility','intellect','cunning','willpower','presence','astrogation','athletics','charm','coercion','computers','cool','coordination','deception','discipline','leadership','mechanics','medicine','negotiation','perception','pilotingPlanetary','pilotingSpace','resilience','skulduggery','stealth','streetwise','survival','vigilance','brawl','gunnery','melee','rangedLight','rangedHeavy','coreWorlds','education','lore','outerRim','underworld','xenology']

class gmRollerForm(ModelForm):
    #make field of choices for drop down
    characters = Character.objects.order_by('id')
    #make field of choices for skills
    skills = Character().__dict__.keys()

    charactersList = forms.ChoiceField(choices = characters, required = True)
    skillsList = forms.ChoiceField(choices = skills, required = True)
    aim = forms.BooleanField(required = False)
    diff = forms.IntegerField(required = True)
    reds = forms.IntegerField(required = True)
    boost = forms.IntegerField(required = True)
    setback = forms.IntegerField(required = True)
