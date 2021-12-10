from django.shortcuts import render
from formApp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    sent = False
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and printing the data")
            print("Name:",form.clean_data['name'])
            print("Marks:",form.clean_data['marks'])
            sent = True
    form = StudentForm()
    return render(request,'formApp/input.html',{'from':form,'sent':sent})
