#CONTENTdm API
from lxml import etree
from pprint import pprint
import json
from io import StringIO, BytesIO
from IPython.core.debugger import Tracer
import urllib.request as web

urlPrefix = 'https://server15963.contentdm.oclc.org'
collectionAlias = 'p15963coll9'

localdir = '/usr/local/hackathon/'
jsondir = localdir + 'json/'
jsonsubdirs = ['denison/', 'kenyon/', 'oberlin/', 'wesleyan/', 'wooster/']

xmldir = localdir + 'xml/'
xmlsubdirs = ['Denison University', 'Kenyon College', 'Oberlin College',\
             'Ohio Wesleyan University', 'The College of Wooster']

# //////////////////////////////////////
#General Access of API
def toJson(data):
    return json.loads(data.decode('utf-8'))

def toXmlTree(data):
    return etree.fromstring(data)

def runZeroParamFunction(function, fmt='xml'):
    fmtstr = "{0:}/dmwebservices/index.php?q={1:}/{2:}/{3:}"
    url = fmtstr.format(urlPrefix, function, collectionAlias, fmt)

    source = web.urlopen(url)
    data = source.read()

    if fmt == 'xml':
        return toXmlTree(data)
    elif fmt == 'json':
        return toJson(data)
    else:
        return None

    return None

def GetCollectionFieldInfo(fmt='xml'):
    function = 'dmGetCollectionFieldInfo'
    data = runZeroParamFunction(function, fmt)
    return data

def GetCollectionList(fmt='xml'):
    function = 'dmGetCollectionList'
    data = runZeroParamFunction(function, fmt)
    return data


# //////////////////////////////////////
#Query Variations
def QueryTitleYear(value, year, field = 'title', start = 1, maxrecs = 1024, xtrafields = '', fmt = 'json'):
    function = 'dmQuery'
    fmtstr = "{0:}/dmwebservices/index.php?q={1:}/{2:}/"
    url = fmtstr.format(urlPrefix, function, collectionAlias)
    search1 = "%s^%s^any^and!date^%s^any^and" %(field, value, str(year))
    retfields = "dmrecord!%s!date%s" % (field, xtrafields)
    sortby = "%s!date" % field
    suppress = 0
    docptr = 0
    spelling_suggestion = 0
    denorm = 0
    fmtstr2 = "{}/{}/{}/{}/{}/{}/{}/{}/{}/{}"
    urlsuffix = fmtstr2.format(search1, retfields, sortby, maxrecs, start, suppress,\
                              docptr, spelling_suggestion, denorm, fmt)
    print(url+urlsuffix)
    source = web.urlopen(url+urlsuffix)
    data = source.read()
    source.close()

    if fmt == 'xml':
        return toXmlTree(data)
    elif fmt == 'json':
        return toJson(data)
    else:
        return None

    return None


# //////////////////////////////////////
#Query Fields
def QueryFields(fieldvalue, start = 1, maxrecs = 1024, sortby = 'none', xtrafields = '', fmt = 'json'):
    function = 'dmQuery'
    fmtstr = "{0:}/dmwebservices/index.php?q={1:}/{2:}/"
    url = fmtstr.format(urlPrefix, function, collectionAlias)
    assert(len(fieldvalue) > 0)

    fields = list(fieldvalue.keys())
    field = fields[0]

    ssingle = "{}^{}^any^and"
    search = ssingle.format(field, fieldvalue[field])
    retfields = "dmrecord!date!{}".format(field)
    for field in fields[1:]:
        search += '!' + ssingle.format(field, fieldvalue[field])
        retfields += '!' + field

    suppress = 0
    docptr = 0
    spelling_suggestion = 0
    denorm = 0
    fmtstr2 = "{}/{}/{}/{}/{}/{}/{}/{}/{}/{}"
    urlsuffix = fmtstr2.format(search, retfields, sortby, maxrecs, start, suppress,\
                              docptr, spelling_suggestion, denorm, fmt)
    print(url+urlsuffix)
    source = web.urlopen(url+urlsuffix)
    data = source.read()
    source.close()

    if fmt == 'xml':
        return toXmlTree(data)
    elif fmt == 'json':
        return toJson(data)
    else:
        return None

    return None



# //////////////////////////////////////




def GetItemInfo(item, fmt='xml'):
    function = 'dmGetItemInfo'
    fmtstr = "{0:}/dmwebservices/index.php?q={1:}/{2:}/{3:}/{4:}"
    url = fmtstr.format(urlPrefix, function, collectionAlias, item, fmt)

    source = web.urlopen(url)
    data = source.read()
    source.close()

    if fmt == 'xml':
        return toXmlTree(data)
    elif fmt == 'json':
        return toJson(data)
    else:
        return None

    return None



# //////////////////////////////////////



def GetCompoundInfo(item, fmt='xml'):
    function = 'dmGetCompoundObjectInfo'
    fmtstr = "{0:}/dmwebservices/index.php?q={1:}/{2:}/{3:}/{4:}"
    url = fmtstr.format(urlPrefix, function, collectionAlias, item, fmt)

    source = web.urlopen(url)
    data = source.read()
    source.close()

    if fmt == 'xml':
        return toXmlTree(data)
    elif fmt == 'json':
        return toJson(data)
    else:
        return None

    return None


# //////////////////////////////////////

def getIssuePagePointers(collectioninfo):
    assert('page' in collectioninfo)
    pagelist = collectioninfo['page']
    pointerlist = []
    for page in pagelist:
        pointerlist.append(page['pageptr'])
    return pointerlist



# //////////////////////////////////////

def getTranscript(pagepointer):
    jdata = GetItemInfo(pagepointer, 'json')
    if 'transc' in jdata:
        return jdata['transc']
    else:
        return None

def getTranscriptSet(pointerlist):
    transcripts = []
    for page in pointerlist:
        transcripts.append(getTranscript(page))
    return transcripts
