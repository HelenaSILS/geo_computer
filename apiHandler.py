import requests
import json


class requestHandler():
    _KEY = "4625ae9b-8da6-4d36-96de-823cd5a3732d"

    def __init__(self):
        pass

    #Moskovskaya+Kol+tsevaya+Avtomobil+naya+Doroga
    #Sultanahmet+Camii+İç+Yolları

    def getAddesses(self, string):
        address = "Sultanahmet+Camii+İç+Yolları"
        url = "https://geocode-maps.yandex.ru/1.x/?apikey={0}&format=json&geocode={1}&lang=en-US".format(self._KEY, address)
        response = requests.get(url)
        #TODO: VERIFICAR SE A RESPOSTA É JSON MESMO
        rJson = response.content
        r=json.loads(rJson)

        n_found = (r["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"])
        n_found = int(n_found)

        if n_found==0:
            return None

        featureMembers = r["response"]["GeoObjectCollection"]["featureMember"]
        addresses_found=[dict() for n in range(n_found)]

        for i in range(len(featureMembers)):
            aux1=featureMembers[i]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
            aux2=featureMembers[i]["GeoObject"]["Point"]["pos"]
            addresses_found[i]={"address":aux1, "pos": aux2}
            print(addresses_found[i])

        return addresses_found






