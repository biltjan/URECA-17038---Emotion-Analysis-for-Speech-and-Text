import json
import os

#load a json file and return a dictionary
def get_template(templateParam):
    #templateParam(str) is the name (EXCLUDING file extension) of the template
    #use os.path.join to accomodate more OS (due to \ or / issue)
    directory = os.path.join("Data", "Template", templateParam)
    json_file = open(directory, "r")
    json_file = json_file.read()
    return json.loads(json_file)


#take a dictionary as argument, return 2 lists containing
#all sentences, and all emotion.
#list will be emptied first to prevent multiple template
#number = index + 1
#note: list in python is immutable
#might require python 3.6 (for ordered dict)
def separate_template(templateDict, senList, emoList):
    for i in range(0, templateDict['NumberofSentences']):
        senList.append(templateDict['Sentences'][i]['sentence'])
        emoList.append(templateDict['Sentences'][i]['emotion'])
        
