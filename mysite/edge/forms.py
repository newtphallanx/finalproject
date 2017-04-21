from django import forms
from django.forms import ModelForm
from edge.models import Character

#making form for characters
class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name','species','career','specializationTrees','soak', 'woundsThreshold', 'woundsCurrent','strainThreshold','strainCurrent','defenseRanged','defenseMelee','creator','brawn','agility','intellect','cunning','willpower','presence','astrogation','athletics','charm','coercion','computers','cool','coordination','deception','discipline','leadership','mechanics','medicine','negotiation','perception','pilotingPlanetary','pilotingSpace','resilience','skulduggery','stealth','streetwise','survival','vigilance','brawl','gunnery','melee','rangedLight','rangedHeavy','coreWorlds','education','lore','outerRim','underworld','xenology']
