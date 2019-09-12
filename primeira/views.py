from django.shortcuts import render, redirect
#from . models import Paciente, Medico, Medicamento


def home(request):
    return render (request, 'home.html')

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render (request, 'paciente/list.html', {'pacientes': pacientes})

def paciente_show(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    return render (request, 'paciente/show.html', {'paciente': paciente})

def paciente_form(request):
    if (request.method == "POST"):
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/atendimento/paciente/')
        else:
            return render (request, 'paciente/form.html', {'form': form})
    else:
        form = PacienteForm()
        return render (request, 'paciente/form.html', {'form': form})

def medico_list(request):
    medicos = Medico.objects.all()
    return render (request, 'medico/list.html', {'medicos': medicos})

def medico_show(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    return render (request, 'medico/show.html', {'medico': medico})

def medico_form(request):
    if (request.method == "POST"):
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/atendimento/medico/')
        else:
           return render (request, 'medico/form.html', {'form': form}) 
    else:
        form = MedicoForm()
        return render (request, 'medico/form.html', {'form': form})
    

def agendamento_list(request):

    return render (request, 'agendamento/list.html')

def medicamento_list(request):
    medicamentos = Medicamento.objects.all()
    return render (request, 'medicamento/list.html', {'medicamentos': medicamentos})

def medicamento_show(request, medicamento_id):
    medicamento = Medicamento.objects.get(id=medicamento_id)
    return render (request, 'medicamento/show.html', {'medicamento': medicamento})

def medicamento_form(request):
    if (request.method == "POST"):
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/atendimento/medicamento/')
        else:
            return render (request, 'medicamento/form.html', {'form': form}) 
    else:
        form = MedicamentoForm()
        return render (request, 'medicamento/form.html', {'form': form})