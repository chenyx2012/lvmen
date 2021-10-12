from scancode import api

if __name__ == '__main__':
    location = "D:/IDEWORK/fossology/atarashi-master/atarashi/license/license_merger.py"
    result = api.get_licenses(location)
    copy = api.get_copyrights(location)
    print(result)
    print(copy)