
def formatNamesList(dataList, recursive = False):

    numNames = len(dataList)

    if(numNames > 1):

        head = dataList[0]
        tail = dataList[1:]

        if len(tail) > 1:
            return head + ', ' + formatNamesList(tail, recursive = True)
        else:
            return head + formatNamesList(tail, recursive = True)
        
    elif(recursive and numNames == 1):
        return ' and ' + dataList[0] 
    elif(not recursive and numNames == 1):
        return dataList[0]
    else:
        return '(None)'


def oneType(type, dataList):

    start = type + ': '
    
    namesString = formatNamesList(dataList)
    

    return start + namesString

def formatDictNames(dataDict, seperator, valueFunction):

    namesString = ''

    stringsList = ['  ' + name + seperator + valueFunction(dataDict[name]) for name in dataDict.keys()]
    
    return '\n'.join(stringsList)


def dictSingleKey(attribute,dataDict):

    start = attribute + ':\n'
    names = formatDictNames(dataDict, ': ', str)

    return start + names

def formatRelationships(relationShipType, relation, dataDict):
    
    start = relationShipType + ':\n'
    lines = formatDictNames(dataDict, ' ' + relation, formatNamesList)

    return start + lines