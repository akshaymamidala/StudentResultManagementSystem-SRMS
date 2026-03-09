from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import *
from django.views.generic.detail import *
from django.urls import reverse_lazy,reverse
from .resources import *
from tablib import Dataset
from django.http import HttpResponse,HttpResponseBadRequest
from datetime import date as dt_date, datetime
from django.utils.dateparse import parse_date

def Base(request):
    return render(request,"base.html")

def login_view(request):
    res_form=GettingResult()
    stu_form=CreateStudent()

    if request.method=='POST':
        res_form=GettingResult(request.POST)
        stu_form=CreateStudent(request.POST)
        if res_form.is_valid() & stu_form.is_valid():
            HallTicketNo=stu_form.cleaned_data['HallTicketNo']
            sem=res_form.cleaned_data['sem']

            if GetResults.objects.filter(HallTicketNo=HallTicketNo,sem=sem):
                return redirect(reverse('student_result'))
        else:
            messages.info(request,' incorrect details...')
    context={
        'res_form':res_form,
        'stu_form':stu_form
    }
    return render(request,"student.html",context)

def student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            hall_ticket_no = form.cleaned_data['HallTicketNo']
            sem = form.cleaned_data['sem']  # Retrieve sem from the form
            student = get_object_or_404(Student, HallTicketNo=hall_ticket_no)
            request.session['student_id'] = student.id
            return redirect('student_result', student_id=student.id, sem=sem)  # Pass sem as parameter
    else:
        form = StudentLoginForm()
    
    return render(request, 'student.html', {'form': form})


def ResultPage1(request, student_id,sem):
    if request.method == 'GET':
        print(student_id, sem)  # Print for debugging purposes
        if student_id:
            student = get_object_or_404(Student, id=student_id)
            results = Results.objects.filter(HallTicketNo_id=student.id, sem=sem)
            context = {
                'student': student,
                'results': results,
                'sem': sem,  # Pass sem to the template context
            }
            return render(request, 'resultpage.html', context)
        else:
            return HttpResponseBadRequest('Missing student_id parameter')
    else:
        return HttpResponseBadRequest('GET method required')
def AdminLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('admin_page')
        else:
            messages.info(request,'username or password is incorrect...')
    return render(request,"admin_login.html")

def AdminPage(request):
    return render(request,"admin_page.html")

def CreateAdmin(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'**Account was created for '+user)
            return redirect('create_admin')
    context={'form':form}
    return render(request,"create_admin.html",context)


class StudentCreateView(CreateView):
    template_name="create_student.html"
    form_class=CreateStudent
    success_url=reverse_lazy("create_student")




headers = {'to':'asc',
         'date':'asc',
         'type':'asc',}

def DisplayStudents(request):
    studs=Student.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        studs = studs.filter(HallTicketNo__icontains=search_query)  # Adjust to your search criteria

    context = {
        'studs': studs,
        'search_query': search_query,
    }

    return render(request, "display_students.html", context)

class DeleteStudent(DeleteView):
    template_name="delete_form.html"
    model=Student
    def get_success_url(self):
        return reverse("display_students")

class DeleteSubjects(DeleteView):
    template_name="delete_form.html"
    model=Subjects
    def get_success_url(self):
        return reverse("manage_subjects")

class Deletebranch(DeleteView):
    template_name="delete_form.html"
    model=Branches
    def get_success_url(self):
        return reverse("manage_branches")

class Deletenotice(DeleteView):
    template_name="delete_form.html"
    model=Notices
    def get_success_url(self):
        return reverse("manage_notices")

class CreateSubject(CreateView):
    template_name="create_subjects.html"
    form_class=CreateSubjects
    success_url=reverse_lazy("create_subjects")

class UpdateSubjectview(UpdateView):
    template_name = "create_subjects.html"
    form_class = CreateSubjects
    model = Subjects
    success_url=reverse_lazy("manage_subjects")

class AddBranches(CreateView):
    template_name="add_branches.html"
    form_class=CreateBranch
    success_url=reverse_lazy("add_branches")

class UpdateBranch(UpdateView):
    template_name = "add_branches.html"
    form_class = CreateBranch
    model = Branches
    success_url=reverse_lazy("manage_branches")

class AddNotice(CreateView):
    template_name="add_notices.html"
    form_class=CreateNotice
    success_url=reverse_lazy("add_notices")

class UpdateNotice(UpdateView):
    template_name = "add_notices.html"
    form_class = CreateNotice
    model = Notices
    success_url=reverse_lazy("manage_notices")

def ManageSubjects(request):
    sub=Subjects.objects.all()
    context={
        'sub':sub
    }
    return render(request,"manage_subjects.html",context)

def ManageNotices(request):
    note=Notices.objects.all()
    context={
        'note':note
    }
    return render(request,"manage_notices.html",context)

def ManageBranches(request):
    br=Branches.objects.raw("select id,branchName from result_branches")
    context={
        'br':br
    }
    return render(request,"manage_branches.html",context)

def EditingStudents(reuqest):
    form6=EditStudent()

    context={
        'form6':form6
    }
    return render(reuqest,"edit_student.html",context)

class StudentUpdate(UpdateView):
    template_name = "create_student.html"
    form_class = CreateStudent
    model = Student
    success_url=reverse_lazy('display_students')


def Displayresults(request):
    
    res=Student.objects.all()

    search_query = request.GET.get('q')
    if search_query:
        res = res.filter(HallTicketNo__icontains=search_query)  
    context={
        'res':res,
        'search_query':search_query
    }

    return render(request,"manage_results.html",context)

def rs_view(request,student_id):

    if request.method == 'GET':
        print(student_id,) 
        if student_id:
            student = get_object_or_404(Student, id=student_id)
            results = Results.objects.filter(HallTicketNo_id=student.id)
            context = {
                'student': student,
                'results': results
            }
            return render(request, 'rs.html', context)
        else:
            return HttpResponseBadRequest('Missing student_id parameter')
    else:
        return HttpResponseBadRequest('GET method required')

    return render(request,"rs.html")
    
class AddResultView(CreateView):
    template_name="add_result.html"
    form_class=AddResult
    success_url=reverse_lazy("add_result")


class UpdateResultView(UpdateView):
    model = Results
    form_class = AddResult  # Form class used for updating results
    template_name = 'add_result.html'
    success_url=reverse_lazy('manage_results')

class ResultView(DetailView):
    template_name="ResultPage.html"
    model=Results

def ResultPage(request):
    rp=Results.objects.all()
    context={
        'rp':rp
    }
    return render(request,"resultpage.html",context)

def sort(request):
        sort = request.GET.get('sort')
        if sort is not None:
            if headers[sort] == "des":
                records = Student.objects.all().order_by(sort).reverse()
                headers[sort] = "asc"
            else:
                records = Student.objects.all().order_by(sort) 
                headers[sort] = "des"
        else:
            records = Student.objects.all()
        return render_to_response("table.html",{'user':request.user,'profile':request.user.get_profile(),'records':records})

def studentUpload(request):
    if request.method=="POST":
        student_resource=StudentResource()
        dataset=Dataset()
        new_student=request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'import.html')

        imported_data=dataset.load(new_student.read(),format='xlsx')
        for data in imported_data:
            value=Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
            )
            value.save()
    return render(request,'import.html')

def _clean_import_value(value):
    if value is None:
        return ""
    return str(value).strip()


def _coerce_int(value):
    cleaned = _clean_import_value(value)
    if not cleaned:
        return None
    try:
        return int(float(cleaned))
    except (TypeError, ValueError):
        return None


def _resolve_branch(value):
    cleaned = _clean_import_value(value)
    if not cleaned:
        return None

    branch = Branches.objects.filter(branchName__iexact=cleaned).first()
    if branch:
        return branch

    numeric = _coerce_int(cleaned)
    if numeric is None:
        return None

    return (
        Branches.objects.filter(branchCode=numeric).first()
        or Branches.objects.filter(pk=numeric).first()
    )


def _resolve_subject(value):
    cleaned = _clean_import_value(value)
    if not cleaned:
        return None

    subject = Subjects.objects.filter(subjectName__iexact=cleaned).first()
    if subject:
        return subject

    numeric = _coerce_int(cleaned)
    if numeric is None:
        return None

    return (
        Subjects.objects.filter(subjectCode=numeric).first()
        or Subjects.objects.filter(pk=numeric).first()
    )


def _coerce_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, dt_date):
        return value

    cleaned = _clean_import_value(value)
    if not cleaned:
        return dt_date.today()

    parsed = parse_date(cleaned)
    if parsed:
        return parsed

    return dt_date.today()


def resultUpload(request):
    if request.method == "POST":
        dataset = Dataset()
        new_result_file = request.FILES.get("myfile")

        if not new_result_file:
            messages.info(request, "Please choose a file.")
            return render(request, "result_import.html")

        if not new_result_file.name.endswith("xlsx"):
            messages.info(request, "Wrong format. Please upload an .xlsx file.")
            return render(request, "result_import.html")

        imported_data = dataset.load(new_result_file.read(), format="xlsx")
        valid_sems = {item[0] for item in sems}

        created_count = 0
        updated_count = 0
        skipped_count = 0
        row_errors = []

        for row_index, row in enumerate(imported_data, start=1):
            row_values = list(row)
            if not row_values or not any(_clean_import_value(cell) for cell in row_values):
                continue

            hall_ticket = _clean_import_value(row_values[0] if len(row_values) > 0 else "")
            sem_value = _clean_import_value(row_values[1] if len(row_values) > 1 else "")
            branch_value = row_values[2] if len(row_values) > 2 else ""
            subject_value = row_values[3] if len(row_values) > 3 else ""
            internal_value = row_values[4] if len(row_values) > 4 else ""
            external_value = row_values[5] if len(row_values) > 5 else ""
            posting_value = row_values[6] if len(row_values) > 6 else ""

            header_tokens = {"hallticketno", "hallticket", "hall_ticket_no", "hall ticket no"}
            normalized_header = hall_ticket.lower().replace("_", " ")
            if row_index == 1 and normalized_header in header_tokens:
                continue

            student = Student.objects.filter(HallTicketNo__iexact=hall_ticket).first()
            if not student:
                skipped_count += 1
                row_errors.append(f"Row {row_index}: Student '{hall_ticket}' not found.")
                continue

            if sem_value not in valid_sems:
                skipped_count += 1
                row_errors.append(f"Row {row_index}: Invalid semester '{sem_value}'.")
                continue

            branch = _resolve_branch(branch_value) or student.branchName
            subject = _resolve_subject(subject_value)

            if not subject:
                skipped_count += 1
                row_errors.append(
                    f"Row {row_index}: Subject '{_clean_import_value(subject_value)}' not found."
                )
                continue

            internal = _coerce_int(internal_value)
            external = _coerce_int(external_value)

            if internal is None or external is None:
                skipped_count += 1
                row_errors.append(f"Row {row_index}: Internal/External must be numeric.")
                continue

            posting_date = _coerce_date(posting_value)

            _, created = Results.objects.update_or_create(
                HallTicketNo=student,
                sem=sem_value,
                subjectCode=subject,
                defaults={
                    "branch": branch,
                    "internal": internal,
                    "external": external,
                    "postingDate": posting_date,
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        messages.success(
            request,
            f"Result import complete: {created_count} created, {updated_count} updated, {skipped_count} skipped.",
        )
        if row_errors:
            messages.warning(request, "Some rows were skipped. " + " | ".join(row_errors[:3]))

    return render(request, "result_import.html")
