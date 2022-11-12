import datetime


def consecutive_day(year, month, day):
    """
    Calcula el dia consecutivo
    """
    date = datetime.date(year, month, day)
    day_1 = datetime.date(year, 1, 1)
    conse_day = (date-day_1).days
    if conse_day > 364:
        conse_day = 364
    return conse_day, str(date)


def format_result(time, hour):
    """
    Funcion que lee la hora y el tiempo de la dosis y la da con el formato hh:mm
    """
    n = int(time/60)
    time += -n*60
    time = datetime.time(hour+n, time)
    return time


def text_warming(time, text):
    """
    Verifica si se cumple la dosis o si no existe riesgo
    """
    if int(str(time)[0:2]) >= 21:
        time = text
    return time


def date_format(date):
    year = int((date)[0:4])
    month = int((date)[5:7])
    day = int((date)[8:10])
    return year, month, day


def hour_format(hour_request):
    hour = int(hour_request[0:2])
    minute = int(hour_request[3:5])
    return hour, minute


class labels_formats:
    """
    Realiza el cambio de numero con el nombre correspondiente a
    cada valor
    """

    def __init__(self):
        self.phototypes = ["I", "II", "III", "IV", "V", "VI"]
        self.cloud_names = ["Despejado", "Medio nublado", "Nublado"]

    def obatin_phototype(self, number):
        """
        Obtiene el nombre del fototipo dependiendo del valor ingresado
        """
        self.phototype = self.phototypes[number]

    def obtain_cloud(self, number):
        """
        Obtiene el nombre de la condidcion del cielo dependiendo del valor ingresado
        """
        self.cloud = self.cloud_names[number]
