import re

def AdquirirCorreos(Texto):
    """
    Función que nos permite encontrar correos en un texto
    tomando en cuenta las las tres opciones comentadas en la tarea
    Domino + 1 extensión
    Domino + 2 extensiones
    Subdomino +  dominio + 1 extensión
    """
    Regex = r"([a-z0-9]+[\.]?[a-z0-9]+[@][\w+.]+[\w+]?)"
    Correos = re.findall(Regex,Texto)
    return Correos


def AdquirirTelefonos(Texto):
    """
    Función que nos permite encontrar telefonos en un texto
    tomando en cuenta las cuatro opciones
    10 digitos.
    Lada entre parentesis 2 o 3 digitos.
    Pueden existir espacios o guiones.
    Los separadores son iguales.
    """
    Telefonos = []

    Regex = r"(\d{10})?"
    Busqueda = re.findall(Regex,Texto)
    for TelefonoEncontrado in Busqueda:
        if TelefonoEncontrado in Telefonos:
            continue
        elif TelefonoEncontrado == '':
            continue
        else:
            Telefonos.append(TelefonoEncontrado)

    Regex = r"([(]?\d{2,3}[)]?\d{6,7})"
    Busqueda = re.findall(Regex,Texto)
    for TelefonoEncontrado in Busqueda:
        if TelefonoEncontrado in Telefonos:
            continue
        elif TelefonoEncontrado == '':
            continue
        else:
            Telefonos.append(TelefonoEncontrado)

    Regex = r"([(]?\d{2,3}[)]?[ -]?\d{3,4}[ -]?\d{4})"
    Busqueda = re.findall(Regex,Texto)
    for TelefonoEncontrado in Busqueda:
        if TelefonoEncontrado in Telefonos:
            continue
        elif TelefonoEncontrado == '':
            continue
        else:
            Telefonos.append(TelefonoEncontrado)

    return Telefonos


def AdquirirCURP(Texto):
    """
    Función para encontrar CURPs
    """
    Regex = r"\w{4}\d{6}[HM]{1}\w{2}\w{3}\w{2}"
    CURPLista = re.findall(Regex,Texto)
    return CURPLista


def AdquirirRFC(Texto):
    """
    función para encontra RFCs
    """
    Regex = r"\w{4}\d{6}\w{3}"
    RFCLista = re.findall(Regex,Texto)
    return RFCLista


if __name__ == '__main__':
    '''
    #prueba de la función AdquirirCorreos
    string = """ ankitrai326@gmail.com my.ownsite@ourearth.org ankitrai326.com"""
    print(string ,"\n\n")
    print(AdquirirCorreos(string),"\n")

    #prueba de la función AdquirirTelefonos
    string = "(331)2345678"
    print(string,"\n\n")
    print(AdquirirTelefonos(string),"\n")

    #prueba de la función AdquirirRFC
    string = "VAGJ581104MJ8"
    print(string,"\n\n")
    print(AdquirirRFC(string),"\n")

    #prueba de la función AdquirirCURP
    string = "LOZL960208HGTPRS01"
    print(string,"\n\n")
    print(AdquirirCURP(string),"\n")
    '''

    #prueba correo Domino + 1 extensión
    Regex = r"([a-z0-9]+[\.]?[a-z0-9]+[@][\w+.]+[\w+]?)"
    string = "juan@padts.mx"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    #prueba correo Domino + 2 extensiones
    Regex = r"([a-z0-9]+[\.]?[a-z0-9]+[@][\w+.]+[\w+]?)"
    string = "juan@padts.com.mx"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    #prueba correo Subdomino +  dominio + 1 extensión
    Regex = r"([a-z0-9]+[\.]?[a-z0-9]+[@][\w+.]+[\w+]?)"
    string = "juan@padts.padts.mx"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    # 10 digitos.
    Regex = r"(\d{10})?"
    string = "3312345678"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    # Lada entre parentesis 2 o 3 digitos.
    Regex = r"([(]?\d{2,3}[)]?\d{6,7})"
    string = "(331)2345678"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    # Pueden existir espacios o guiones.
    Regex = r"([(]?\d{2,3}[)]?[ -]?\d{3,4}[ -]?\d{4})"
    string = "(33) 1234-5678"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    # Los separadores son iguales.
    Regex = r"([(]?\d{2,3}[)]?[ -]?\d{3,4}[ -]?\d{4})"
    string = "(33)-1234-5678"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    #prueba para el CURP
    Regex = r"\w{4}\d{6}[HM]{1}\w{2}\w{3}\w{2}"
    string = "LOZL960208HGTPRS01"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")

    #prueba para el RFC
    Regex = r"\w{4}\d{6}\w{3}"
    string = "VAGJ581104MJ8"
    print(string, end=" ")
    if(re.search(Regex,string)):
        print("Pass\n")
    else:
        print("Fails\n")
