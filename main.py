from zvgportal.query import ZvgSearch
from zvgportal.searchparams import BLand, SearchObject


def zvg_portal_search(name):

    query = ZvgSearch(bland=BLand.BY, search_object=SearchObject.GARAGE, value_limit=False)
    results = query.run()
    print(results)
    # print(results.request.body)


if __name__ == '__main__':
    zvg_portal_search('PyCharm')

