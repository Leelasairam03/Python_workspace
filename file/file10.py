#dumps,loads
import json
with open("file/serialise.txt","w+") as f:
    l=["akash","bhoomi","agni","vayu","neera"]
    jstr=json.dumps(l)
    print(jstr)
    f.write(jstr)
    f.seek(0)

    #deserialization
    f.seek(0)
    data=f.read()
    l=json.loads(data)
    print(l)
    print(type(l))

