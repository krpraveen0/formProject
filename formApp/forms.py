from django import forms
from django.core import validators


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    marks = forms.IntegerField()

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    #defining the clean method
    def clean_name(self):
        inputName = self.cleaned_data['name']
        if len(inputName) <4:
            raise forms.ValidationError('The minimum number of characters in the name field should be 4')
        return inputName
    #The returned value of clean method will be considered  by Django at The
    #time of submitting the form.

    def clean_rollno(self):
        inputRollno=self.cleaned_data['rollno']
        print('Validating the roll no')
        return inputRollno
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        print('VAlidating the email')
        return inputEmail
    def clean_feedback(self):
        inputFeedback = self.cleaned_data['feedback']
        print("Validating feedback field")
        return inputFeedback
        
