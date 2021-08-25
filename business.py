import sys
from apiHandler import requestHandler
from geoComputer import geoComputer


class Business:
    _rh=requestHandler()
    _gc = geoComputer()
    _coordenates = []
    _distances = []
    def __init__(self):
        pass

    def isvalid(self, address):
        if type(address) != str:
            return False
        elif not address.replace(" ","").isalnum():
            return False
        else:
            return True

    def sendyandex(self,address):

        if not self.isvalid(address):
            return "Invalid address, please try with a different one"

        response=self._rh.getAddesses(address.replace(" ", "+"))
        if response==None:
            return "No results found"
        else:
            self._coordenates.clear()
            for i in range(len(response)):
                aux1 = response[i]['pos'].split(" ")
                self._coordenates.append([float(aux1[0]), float(aux1[1])])
            print(self._coordenates)

            self._distances.clear()
            for i in self._coordenates:
                serie = self._gc.create_Geoseries(i[0], i[1])
                inMKD=self._gc.is_in_MKAD(serie)
                if inMKD.bool() == False:
                    k=self._gc.calculate_distance(serie)
                    kj=k.to_json()
                    self._distances.append(k.to_json())
                    print("***")
                    print(k.to_json())
                else:
                    self._distances.append(0)
            return self._distances




