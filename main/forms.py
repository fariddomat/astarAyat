from faulthandler import disable
from logging import PlaceHolder
from django import forms
from .search import getH,heuristicValue

from main.search import heuristic

class SearchMap(forms.Form):
    # choices = []
    # user_choices = heuristicValue
    # for choice in user_choices:
    #     choices.append((choice, choice))
    start=forms.ChoiceField(label = 'Start',choices=[],  widget=forms.Select(attrs={'class':'form-control'}))
    goal=forms.ChoiceField(label = 'Goal',choices=[], initial='Bucharest',  widget=forms.Select(attrs={'class':'form-control'}))
     
    def __init__(self, *args, **kwargs):
        super(SearchMap, self).__init__(*args, **kwargs)
        self.fields['start'].choices = [(x, x) for x in getH()]
        self.fields['goal'].choices =  self.fields['start'].choices
 
class AddRomania(forms.Form):
    
    distance=forms.CharField(disabled=disable,widget=forms.Textarea(attrs={'name':'distance','class':'form-control disabled', 'rows':'10', 'cols':'50', 'placeholder':"Arad-Sibiu-value\nArad-Timisoara-value\n"})
                          ,initial='Arad Sibiu 140\nArad Timisoara 118\nArad Zerind 75\nBucharest Fagaras 211\nBucharest Giurgiu 90\nBucharest Pitesti 101\nBucharest Urziceni 85\nCraiova Dobreta 120\nCraiova Pitesti 138\nCraiova Rimnicu_Vilcea 146\nDobreta Mehadia 75\nEforie Hirsova 86\nFagaras Sibiu 99\nHirsova Urziceni 98\nIasi Neamt 87\nIasi Vaslui 92\nLugoj Mehadia 70\nLugoj Timisoara 111\nOradea Zerind 71\nOradea Sibiu 151\nPitesti Rimnicu_Vilcea 97\nRimnicu_Vilcea Sibiu 80\nUrziceni Vaslui 142')
    
    straight_line=forms.CharField(disabled=disable,widget=forms.Textarea(attrs={'name':'straight_line','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"Arad value\nIasi value\n"}), initial='Arad 366\nBucharest 0\nCraiova 160\nDobreta 242\nEforie 161\nFagaras 178\nGiurgiu 77\nHirsova 151\nIasi 226\nLugoj 244\nMehadia 241\nNeamt 234\nOradea 380\nPitesti 98\nRimnicu_Vilcea 193\nSibiu 253\nTimisoara 329\nUrziceni 80\nVaslui 199\nZerind 374')
    
class AddCountry(forms.Form):
    
    distance=forms.CharField(widget=forms.Textarea(attrs={'name':'distance','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"Arad Sibiu value\nArad Timisoara value\n"})
                         )
    
    straight_line=forms.CharField(widget=forms.Textarea(attrs={'name':'heuristic_value','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"Arad value\nBucharest value\n"}))