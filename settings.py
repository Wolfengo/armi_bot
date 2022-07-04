TEST = True

""" name1 """
Test_TOKEN = ''
folder_path_test = 'armi_driver_db.db'
""" name2 """
TOKEN = ''
folder_path = ''

URL = ''
URL_PARK = ""


def test():
    if TEST is True:
        return Test_TOKEN
    elif TEST is False:
        return TOKEN


def folder():
    if TEST is True:
        return folder_path_test
    elif TEST is False:
        return folder_path
