#dump,load
import json
with open("file/serialise.txt","w+") as f:
    l=["sita","ram","lakshman","bharat","hanuman"]
    json.dump(l,f)

    f.seek(0)
    l=json.load(f)
    print(l)
    print(type(l))
