from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import MediaFrame
from albums.models import Album
from mediabox.models import MediaImage, MediaVideo


class MediaFrameCreateForm(forms.ModelForm):

    description = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)
    video_code = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    album = forms.ModelChoiceField(queryset=None, empty_label=None)

    class Meta:
        model = MediaFrame
        fields = ('description', 'image', 'video_code', 'album')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(MediaFrameCreateForm, self).__init__(*args, **kwargs)
        self.album = Album.objects.filter(owner=self.owner).order_by('-created')
        self.fields['album'].queryset = self.album
        if len(self.album) > 0:
            self.fields['album'].initial = self.album[0]

    def clean(self):
        image = self.cleaned_data['image']
        video_code = self.cleaned_data['video_code']
        if not image and not video_code:
            raise forms.ValidationError(_('Please choose a valid image file'))
        return self.cleaned_data

    def save(self, commit=True):
        media_frame = super(MediaFrameCreateForm, self).save(commit=False)
        if commit:
            image = self.cleaned_data['image']
            video_code = self.cleaned_data['video_code']
            if image:
                image_item = MediaImage(image=image, owner=self.owner)
                image_item.save()
                media_frame.content_type = 'I'
                media_frame.image_item = image_item
            elif video_code:
                video_item = MediaVideo(video_code=video_code, owner=self.owner)
                video_item.save()
                media_frame.content_type = 'V'
                media_frame.video_item = video_item
            else:
                raise
            media_frame.owner = self.owner
            media_frame.save()
        return media_frame


class VideoFrameCreateForm(forms.ModelForm):

    description = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    video = forms.FileField(required=False)
    video_code = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    album = forms.ModelChoiceField(queryset=None, empty_label=None)

    class Meta:
        model = MediaFrame
        fields = ('description', 'video', 'video_code', 'album')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(VideoFrameCreateForm, self).__init__(*args, **kwargs)
        self.album = Album.objects.filter(owner=self.owner).order_by('-created')
        self.fields['album'].queryset = self.album
        if len(self.album) > 0:
            self.fields['album'].initial = self.album[0]

    def clean_video(self):
        video = self.cleaned_data['video']
        if not video:
            return None
        content_type = video.content_type
        if content_type not in settings.UPLOAD_VIDEO_TYPES:
            raise forms.ValidationError(_('Video file type is not supported'))
        return video

    def clean(self):
        video = self.cleaned_data.get('video', None)
        video_code = self.cleaned_data['video_code']
        if not video and not video_code:
            raise forms.ValidationError(_('Please choose a valid video file or enter a video code'))
        return self.cleaned_data

    def save(self, commit=True):
        media_frame = super(VideoFrameCreateForm, self).save(commit=False)
        if commit:
            video = self.cleaned_data['video']
            video_code = self.cleaned_data['video_code']
            media_frame.content_type = 'V'
            if video:
                video_item = MediaVideo(video=video, owner=self.owner)
                video_item.save()
                media_frame.video_item = video_item
            elif video_code:
                video_item = MediaVideo(video_code=video_code, owner=self.owner)
                video_item.save()
                media_frame.video_item = video_item
            else:
                raise
            media_frame.owner = self.owner
            media_frame.save()
        return media_frame
