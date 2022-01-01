from django.shortcuts import render

# Create your views here.
def display(req):
    name = { 'emp_id':101, 'emp_Name':'Rahul Gandhi'}
    a = 10
    my_Data = { 'value':a,'Emp_Data':name, 'message':"Enjoy Last Working Day, and See you next Year!"}

    my_value = { 'value':a}
    return render(req, 'dataapp/index.html', context=my_Data)