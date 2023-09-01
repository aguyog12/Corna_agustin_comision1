def datosPaciente(nombreDelPaciente, fechaNacimiento, direccionClinica):
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("DATOS DEL PACIENTE")
    print(nombreDelPaciente)
    print(fechaNacimiento)
    print(direccionClinica)

def datosMedicamento(nombreMedicamento, dosisMedicamento, instruccionesDeUso):
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("MEDICAMENTO RECETADO")
    print(nombreMedicamento)
    print(dosisMedicamento)
    print(instruccionesDeUso)

def siguienteTurno(fecha, hora):
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("SU SIGUIENTE TURNO SERA:")
    print(fecha)
    print(hora)
    print("+++++++++++++++++++++++++++++++++++++++++++++")

def datosConsultorio():
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("CONSULTORIO MEDICO")
    print('numero de telefono: 12345')
    print('correo electronico: consultorio@hotmail.com')

nombreDelPaciente = input("ingrese el nombre del paciente: ")
fechaNacimiento = input("ingrese la fecha de nacimiento del paciente: ")
direccionClinica = input("ingrese la direccion de la clinica medica: ")

nombreMedicamento = input("ingrese el nombre del medicamento: ")
dosisMedicamento = input("ingrese la dosis: ")
instruccionesDeUso = input("ingrese las instrucciones de uso: ")

fecha = input("ingrese la fecha de la siguiente consulta: ")
hora = input("ingrese la hora de la siguiente consulta: ")

datosConsultorio()
datosPaciente(nombreDelPaciente, fechaNacimiento, direccionClinica)
datosMedicamento(nombreMedicamento, dosisMedicamento, instruccionesDeUso)
siguienteTurno(fecha, hora)


