from django import forms
from .models import Report
#pip install django-multiupload  or add to requirements.txt (yusuf)
from multiupload.fields import MultiFileField
from .models import Report, Folder, File

class reportForm(forms.Form):
    tile = forms.CharField(label="Report Title: ", max_length=255)
    compName = forms.CharField(label="Company Name: ", max_length=255)
    ceo = forms.CharField(label="CEO: ", max_length=255)
    phoneNum = forms.NumberInput(blank=True)
    email = forms.CharField(label="CEO: ", max_length=255)
    location = forms.CharField(label = "Location: ", max_length=255)
    country = forms.CharField(label= "Country: ", max_length=255)
    sector = forms.CharField(label="Sector: ", max_length=255)
    projects = forms.CharField(label="Current Project(s): ", widget=forms.Textarea)
    private = forms.BooleanField(label="Private: ", required=False)
    files = MultiFileField(min_num=1, max_num=15, max_file_size=1024*1024*5)

TITLE = 1
COMPNAME = 2
LOCATION = 3
SECTOR = 4
CEO= 5

SEARCH_CHOICES = (
    (TITLE, 'Report Title'),
    (COMPNAME, 'Company Name'),
    (LOCATION, 'Location'),
    (SECTOR, 'Sector'),
    (CEO, "CEO"),
    )


class new_folder_form(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']


class folder_select(forms.ModelForm):
    folder = forms.ModelChoiceField(queryset=Folder.objects.filter())

#Was trying to do some search forms, ignore or alter
class single_search_query(forms.Form):
    search_input = forms.CharField(label="Enter a search string ")
    category = forms.ChoiceField(label ="Search Category", choices = SEARCH_CHOICES)
