from apiHandler import requestHandler
from geoComputer import geoComputer


class Business:
    _rh=requestHandler()
    _gc = geoComputer()
    _coordenates = []
    _distances = []
    def __init__(self):
        pass

    def test_string(self,address):
        t=type(address) == str
        assert t, "not a string"

    def test_alnum(self, address):
        t=address.replace(" ", "").isalnum()
        assert t, "it only accept digits and letters"

    def test_is_valid(self, address):
        self.test_string(address)
        self.test_alnum(address)

    # TODO: chanege name
    def process_request(self, address):
        self.test_is_valid(address)
        address=address.strip()
        response=self._rh.request_addresses(address.replace(" ", "+"))
        if response==None:
            return "No results found"
        else:
            self._coordenates.clear()
            for i in range(len(response)):
                aux1 = response[i]['pos'].split(" ")
                self._coordenates.append([float(aux1[0]), float(aux1[1])])
            #print(self._coordenates)

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
                    print("fazendo oq")
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


            return final




