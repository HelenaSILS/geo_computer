from apiHandler import requestHandler
from geoComputer import geoComputer
from tester import tester


class Business:
    """
    Business class calls and handles the classes apiHandler and geoComputer. It is where both classes are connected.
    """
    _rh = requestHandler()
    _gc = geoComputer()
    _tester = tester()
    _coordenates = []
    _distances = []
    def __init__(self):
        pass

    def process_request(self, address):
        """
        Calls the functions from the classes apiHandler and geoComputer that generates the data. Returns a list of
        dictionaries that contain a match for the requested address and its respectively distance (in longitude and
        latitude degrees) from MKAD. If no results is found, returns a simple string.
        :param address: string
        :return: list[dict]
        """
        self._tester.test_is_valid(address)
        address=address.strip()
        response=self._rh.request_addresses(address.replace(" ", "+"))
        if response == None:
            with open ('log.txt', 'a') as file:
                file.write(address + "not found\n")
            return "No results found"
        else:
            self._coordenates.clear()
            for i in range(len(response)):
                aux1 = response[i]['pos'].split(" ")
                self._coordenates.append([float(aux1[0]), float(aux1[1])])

            self._distances.clear()
            for i in self._coordenates:
                serie = self._gc.create_Geoseries(i[0], i[1])
                inMKD=self._gc.is_in_MKAD(serie)
                if inMKD.bool() == False:
                    k=self._gc.calculate_distance(serie)
                    kj=k.to_json()
                    kj=str(kj)
                    kj=kj[5:-1]
                    kj=float(kj)
                    self._distances.append(kj)
                else:
                    self._distances.append(0)

            final=[]
            for i in range(len(response)):
                aux1 = response[i]['address']['formatted']
                aux2= self._distances[i]
                aux_d={aux1:aux2}
                final.append(aux_d)
            for i in final:
                for k in i:
                    print(k, i[k])

            with open ('log.txt', 'a') as file:
                for i in final:
                    file.write(str(i)+"\n")

            return final




