from .format_data import *
from flask import request
import numpy as np


class TES_solario:
    """
    Busca la informacion de las dosis en los archivos y los prepara con el formato de salida
    """

    def __init__(self, request):
        self.request = request
        self.get_initial_data()

    def get_initial_data(self):
        self.treatment = request.form["treatment"]
        self.date = request.form["date"]
        self.hour = request.form["hour"]
        self.skin = int(request.form["skin"])

    def get_data_cabin(self):
        self.get_initial_data()
        self.namecab = request.form["cabin"]

    def get_final_data(self):
        self.get_data_cabin()
        self.n_cloud = int(request.form["cloud"])
        self.year, self.month, self.day = date_format(self.date)
        self.hour, self.minute = hour_format(self.hour)
        self.labels = labels_formats()
        self.labels.obatin_phototype(self.skin)
        self.labels.obtain_cloud(self.n_cloud)
        self.search_data()

    def search_data(self):
        """
        Recolenta la información dependiendo de los datos obtenidos de la request de la página
        """
        date_num, date = consecutive_day(self.year,
                                         self.month,
                                         self.day)
        self.hour_num = (self.hour-8)*60+self.minute
        date = "{}/{}/{}".format(self.date[8:10],
                                 date[5:7],
                                 date[0:4])
        """
        <---------------------------------------------->
        Se suman los minutos para obtener los minutos medidos desde la hora de inicio
        <--------------------------------------------->
        """
        # Se suma 2 a la dosis para tener un rango efectivo
        doses_filename = "{}-{}-{}.txt".format(self.namecab,
                                               self.treatment,
                                               self.n_cloud)
        max_filename = "{}-{}-{}.txt".format(self.namecab,
                                             self.labels.phototype,
                                             self.n_cloud)
        self.doses_time = int(np.loadtxt("Data/dosis{}".format(doses_filename),
                                         skiprows=self.hour_num,
                                         max_rows=1,
                                         usecols=date_num)+2+self.minute)
        self.max_time = int(np.loadtxt("Data/Max{}".format(max_filename),
                                       skiprows=self.hour_num,
                                       max_rows=1,
                                       usecols=date_num)+2+self.minute)
        # Da formato a el tiempo maximo y de dosis
        self.max_time = format_result(self.max_time,
                                      self.hour)
        self.doses_time = format_result(self.doses_time,
                                        self.hour)
        self.hour = datetime.time(self.hour,
                                  self.minute)
        self.doses_time = text_warming(self.doses_time,
                                       "No se completará la dosis")
        self.max_time = text_warming(self.max_time,
                                     "Sin riesgo")
