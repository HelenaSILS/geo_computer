import requests
import json


class requestHandler():
    """requestHandler is responsible for making a request to the Yandex api, using the key of my (HelenaSILS)
    account to request it."""
    _KEY = "4625ae9b-8da6-4d36-96de-823cd5a3732d"

    def __init__(self):
        pass

    #examples of possible addresses to use in request_addresses:
    #
    #needed: Moskovskaya+Kol+tsevaya+Avtomobil+naya+Doroga
    #original: Moskovskaya Kol tsevaya Avtomobil naya Doroga
    #
    #need: Sultanahmet+Camii+İç+Yolları
    #original: Sultanahmet Camii İç Yolları

    def request_addresses(self, address):
        """
        request_address communicates with the Yandex API, requesting a JSON in english answer, that contains all the
        matches for the address and their requested data. It return a piece of the JSON, as a list of dictionaries.
        If nothing if found, it returns "None".
        :param address: string
        :return: list[dict]
        """
        url = "https://geocode-maps.yandex.ru/1.x/?apikey={0}&format=json&geocode={1}&lang=en-US".format(self._KEY, address)
        response = requests.get(url)

        rJson = response.content
        r=json.loads(rJson)

        n_found = (r["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"])
        n_found = int(n_found)

        #When a result is not found, the key "found" is 0
        if n_found==0:
            return None

        featureMembers = r["response"]["GeoObjectCollection"]["featureMember"]
        addresses_found=[dict() for n in range(n_found)]

        for i in range(len(featureMembers)):
            aux1=featureMembers[i]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
            aux2=featureMembers[i]["GeoObject"]["Point"]["pos"]
            addresses_found[i]={"address":aux1, "pos": aux2}

        return addresses_found






