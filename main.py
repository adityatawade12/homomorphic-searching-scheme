from pymongo import MongoClient
from funcs import BytesIntEncoder,encodeNencrypt,dencodeNdencrypt,sameChecking
from bson.binary import Binary
from bson.objectid import ObjectId
import pickle




connection = MongoClient('localhost', 27017)
my_database = connection.newDb
data = my_database.coll1
data1 = my_database.textData

key=data.find_one({'_id': ObjectId('607e734b4f247f2ae4b789b0')})
pubK=pickle.loads(key["publicKey"])
privK=pickle.loads(key["privateKey"])

def encObjCreate(s):
    return  encodeNencrypt(BytesIntEncoder.encode(s.encode()),pubK)


foundObj=0
choice=0
while choice!=3:
    print("\n1.Create record\n2.Search\n3.Exit")
    choice=int(input())
    if choice==1:
        inputText=input("Enter input text: ")
        encObj=encObjCreate(inputText)
        inputText1=input("Enter input text1: ")
        encObj1=encObjCreate(inputText1)
        entry_data = {
            'text': pickle.dumps(encObj),
            'field2':pickle.dumps(encObj1)
        }
        result = data1.insert_one(entry_data)
        
    elif choice==2:
        searchText=input("Enter search text: ")
        encObj=encObjCreate(searchText)
        
        for doc in data1.find():
            
            retObj=sameChecking(pickle.loads(doc["text"]),encObj)
            try:
                if len(BytesIntEncoder.decode(dencodeNdencrypt(retObj,privK)).decode())==0:
                    keyList=list(doc.keys())
                    keyList.remove("_id")
                    print("")
                    for f in keyList :
                        print(f,":",BytesIntEncoder.decode(dencodeNdencrypt(pickle.loads(doc[f]),privK)).decode()," ",end=" ")
                        print("")
                    foundObj=1
                 
            except:
                pass
                
        if foundObj==1:
            foundObj=0
            
        else:
            print("Not Found")

    

        



connection.close()