class FormData:

    def __init__(self, land_abk, search_object, value_limit, btermin):
        self.ger_name = "-- Alle Amtsgerichte --"
        self.order_by = 2
        self.land_abk = land_abk
        self.ger_id = 0
        self.az1 = None
        self.az2 = None
        self.az3 = None
        self.az4 = None
        self.art = None
        self.obj = None
        # self.__setattr__("obj_arr[]", search_object)
        # self.obj_liste = search_object
        self.str = None
        self.hnr = None
        self.plz = None
        self.ort = None
        self.ortsteil = None
        self.hinweis = "on" if value_limit else None
        self.vtermin = None
        self.btermin = btermin # yyyy-mm-dd