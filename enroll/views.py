from django.shortcuts import render

# Create your views here.
def showinfo(request):
    return render (request, 'enroll/home.html')


#def showdata(request, students_roll):
 #   std = {'student':students_roll}
  #  return render (request, 'enroll/showdetails.html', std)

def showdata(request, students_id):
    if students_id == 1:
        std = {'id': students_id , 'name': 'Shakhawat'}
    if students_id == 2:
        std = {'id': students_id , 'name': 'Arafat'}
    if students_id == 3:
        std = {'id': students_id , 'name': 'Mamun'}
    return render (request, 'enroll/showdetails.html', std)

#use sub id
def showsubdata(request,students_id, students_subid):
    if students_id == 1 and students_subid == 7:
        std = {'id': students_id , 'name': 'Shakhawat', 'info':'sub details'}
    if students_id == 2 and students_subid == 8:
        std = {'id': students_id , 'name': 'Arafat', 'info':'sub details'}
    if students_id == 3 and students_subid == 9:
        std = {'id': students_id , 'name': 'Mamun', 'info':'sub details'}
    return render (request, 'enroll/showdetails.html', std)
    