

# |  \/  (_) (_)_ _  __| | /_\  _ _  __ _ _ _| |___ __ ____ _ _ _
# | |\/| | | | | ' \/ _` |/ _ \| ' \/ _` | ' \  _\ V  V / _` | '_|
# |_|  |_|_|_|_|_||_\__,_/_/ \_\_||_\__,_|_||_\__|\_/\_/\__,_|_|

import xml.etree.ElementTree as ET;
from pymongo import MongoClient;
import re;

# 1: Load entities project XML#
xmlTree = ET.parse('exceptiontest.xml');
xmlRoot = xmlTree.getroot()
csFilesList = [];

# 2: Get All cs files in xml#
for child in xmlRoot:
    for csfile in child:
        if 'Include' in csfile.attrib:
          fileName = csfile.attrib["Include"];
          if fileName.endswith(".cs"):
            csFilesList.append(fileName);

dict = {};
# 3: Iterate Over each list element and get its count in mongo db database
try:
    client = MongoClient();
    db = client.admin;
    coll = db.Exceptions;
    for csfile in csFilesList:
        search_this_string = csfile.replace(".cs","");
        collCount = coll.find({"$text": {"$search": search_this_string}}).count()
        if collCount > 0:
            dict[csfile] = collCount;
except:
    print('Error occurs')

# 4: sort dictionary in desceding order to print result
sortedList = sorted(dict.items(), key=lambda x: x[1], reverse=True)

#5: Print sorted list
for obj in sortedList:
    print(obj[0], obj[1])
