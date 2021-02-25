import json

file = open("dictionary.txt", "r")
y = file.read()

diction = json.loads(y)
file.close()

sec_dict = {}
def GetKeys(diction):
    for keys, value in diction.items():
        if type(value) is dict:
            GetKeys(value)
            if (keys in sec_dict):
                sec_dict[keys] += 1
            else:
                sec_dict[keys]=1
        elif (keys in sec_dict):
            sec_dict[keys] += 1
        else:
            sec_dict[keys]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    GetKeys(value[i])

GetKeys(diction)

KeyVals = max(sec_dict.items(), key=lambda x: x[1])
KeyList = list()
for key, value in sec_dict.items():
    if value == KeyVals[1]:
        KeyList.append(key)
print("All keys with the max value: ", KeyList)
