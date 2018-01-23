import json
import urllib.parse
import urllib.request
import json
import os, sys
import random
 
#
 
API_URL_GOOG = 'https://www.googleapis.com/customsearch/v1?'
API_KEY_GOOG = 'AIzaSyDVLECqO2pDdoee3B1p5yfY8GdDEzBR22I'
CUSTOM_SEARCH_KEY_GOOG = '007419050581642401712:cnepvkurzja'
EngDictFilename = '20k.txt'
 
def load_words():
    with open(EngDictFilename,"r") as english_dictionary:
        return english_dictionary.readlines();
     
def buildNewUrl(queryString):
    return 'https://www.google.com/complete/search?client=psy-ab&hl=en&gs_rn=64&gs_ri=psy-ab&tok=FSWp5p7c_g8ifdeQMa3WWg&pq=' + queryString + '&cp=2&gs_id=u&q=' + queryString + '&xhr=t'
 
def getJsonDict(url):
    print(url);
    response = urllib.request.urlopen(url);
    print(response)
    readResponse = response.read()#BYTES
    json_text = readResponse.decode(encoding = 'utf-8')#THIS IS JSON
    print(json_text)
    return json.loads(json_text)#THIS IS A List
 
def getAllAutocompleteFromJson(jsonList):
    print(jsonList)
    allAutocompleteOptions = [];
    for i in jsonList[1]:
        allAutocompleteOptions.append((i[0].replace('<b>','')[:-4]))
    return allAutocompleteOptions;

def getRandomWord(): 
    english_words = load_words();
    return english_words[random.randint(1,19990)][:-1]
 
def getAllAutoFromRandomWord(randomWord):
    finalList = [];
    fullist = getAllAutocompleteFromJson(getJsonDict(buildNewUrl(randomWord)));
    for item in fullist:
        finalList.append(item.replace(randomWord,"").strip())
    set(finalList);
    for item in finalList:
        if item=="":
            finalList.remove(item);
    return list(finalList);
word = getRandomWord()
print(word);
getAllAutoFromRandomWord(word)






#main();
    
    



 
#import proj3classes 
 
 
#googUrl = 'http://cse.google.com:443/cse/publicurl?cx=007419050581642401712:cnepvkurzja'
#BASIC_URL_GOOG = 'https://www.google.com/complete/search?'
#https://www.googleapis.com/customsearch/v1?parameters
 
#http://www.google.com/cse/manage/all
#https://www.google.com/complete/search?client=psy-ab&hl=en&gs_rn=64&gs_ri=psy-ab&tok=KoDX0dh4Y-4J4X8kpYU46w&pq=high&cp=5&gs_id=8&q=highs&xhr=t       
 
 
#urllib.parse.urlencode(queryParameters)
#https://www.google.com/complete/search?client=hp&hl=en&sugexp=msedr&gs_rn=62&gs_ri=hp&cp=1&gs_id=9c&q=a&xhr=t
#finalURL = 'https://www.google.com/complete/search?client=psy-ab&hl=en&gs_rn=64&gs_ri=psy-ab&tok=FSWp5p7c_g8ifdeQMa3WWg&pq=hello&cp=2&gs_id=u&q=he&xhr=t'

#def buildUrl(queryString):
#    return API_URL_GOOG + 'key=' + API_KEY_GOOG + '&cx=' + CUSTOM_SEARCH_KEY_GOOG + '&prettyPrint=true'+ '&q=' + queryString;

#urllib.parse.urlencode(queryParameters)
  