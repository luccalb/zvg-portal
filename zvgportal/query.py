from zvgportal.parser.parser import parse_html
from zvgportal.searchparams import BLand, SearchObject
from zvgportal.zvgclient import ZvgClient


class ZvgSearch:

    def __init__(self, bland=BLand.BY, search_object=SearchObject.GARAGE, value_limit=False, btermin="2025-12-31"):
        self.bland = bland.value
        self.search_object = search_object.value
        self.value_limit = value_limit
        self.btermin = btermin

    def run(self):
        client = ZvgClient(self)
        html = client.search()
        parsed_objects = parse_html(html)
        return parsed_objects
