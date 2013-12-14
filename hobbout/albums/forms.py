from django import forms

from .models import Album


class AlbumCreateForm(forms.ModelForm):

    description = forms.CharField(max_length=255, widget=forms.Textarea)

    class Meta:
        model = Album
        fields = ('name', 'description', 'is_public')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(AlbumCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        album = super(AlbumCreateForm, self).save(commit=False)
        if commit:
            album.owner = self.owner
            album.save()
        return album
