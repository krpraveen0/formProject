from django.shortcuts import render
from formApp.forms import StudentForm,FeedBackForm, SignupForm

# Create your views here.
def student_input_view(request):
    sent = False
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and printing the data")
            print("Name:",form.cleaned_data['name'])
            print("Marks:",form.cleaned_data['marks'])
            sent = True
    form = StudentForm()
    return render(request,'formApp/input.html',{'form':form,'sent':sent})

#create a view for the feedback form
def feedback_input_view(request):
    sent = False
    if request.method=='POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and printing the data")
            print("Name:",form.cleaned_data['name'])
            print("RollNo:",form.cleaned_data['rollno'])
            print("EmailId:",form.cleaned_data['email'])
            print("FeedBack:",form.cleaned_data['feedback'])
            sent = True
    form = FeedBackForm()
    return render(request,'formApp/feedback.html',{'form':form,'sent':sent})

#view for signup form
def signup_form_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed... Printing your data')
            print('Name:',form.cleaned_data['name'])
            print('Password:',form.cleaned_data['password'])
            print('Email:',form.cleaned_data['email'])
    return render(request,'formApp/signup.html',{'form':form})
