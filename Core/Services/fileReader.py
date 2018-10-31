
import csv


class FLRead:
    def __init__(self,filePath):
        with open(filePath,'r') as fl:
            self.FL = list(csv.reader(fl))

