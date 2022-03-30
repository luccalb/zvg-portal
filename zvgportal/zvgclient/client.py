import requests

from zvgportal.zvgclient.formdata import FormData

SEARCH_URL = "https://www.zvg-portal.de/index.php"


class ZvgClient:

    def __init__(self, query):
        self.query = query

    def search(self):
        params = {"button": "Suchen", "all": 1}
        data = FormData(
            land_abk=self.query.bland,
            search_object=self.query.search_object,
            value_limit=self.query.value_limit,
            btermin=self.query.btermin)
        r = requests.post(SEARCH_URL, data=data.__dict__, params=params)
        return r
