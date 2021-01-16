# fileWriter

import simplejson as json

def getContents(path):
    f = open(path, 'r')
    c = f.read()
    f.close()
    return c

def writeContents(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()


# reads data from file and returns it as a dictionary
def loadData(path):
    code = getContents(path)
    return json.loads(code)

# reads data from file and returns it as a dictionary
def dumpData(path, data):
    code = json.dumps(data, sort_keys=True, indent=4*' ')
    #  print(code)
    writeContents(path, code)
