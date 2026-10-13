import csv
import json
import os

acces="files/acces.csv"
logs="files/logs.csv" #incase of misuse/inapropriate useage
togglefiles="files/toggle.csv"# form of serverid,on/off
configfiles="files/config.csv" # serverid,modelname,apikey


def embedhelp():
    json_path = os.path.join(os.path.dirname(__file__),'helpembed.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def lacces():
    data={}
    try:
        with open(acces,newline="") as f:
            for gid, uid in csv.reader(f):
                gid ,uid= int(gid) ,int(uid)
                if gid not in data: data[gid] = set()

                data[gid].add(uid)
        
    except: pass
    return data





def ltoggle():
    try:
        with open(togglefiles) as f:
            return {int(line.strip()) for line in f if line.strip()}
    except: return set()
    
    
    
    
def stoggle(c):
    with open(togglefiles,"w") as f:
        for gid in c:
            f.write(f"{gid}\n")
            
            
            
            
def lconfig():
    d={}
    try:
        with open(configfiles,newline="") as f:
            for gid,model,key,prompt in csv.reader(f):
                d[int(gid)]={"model":model,"apikey":key,"prompt":prompt}
    except: pass
    return d



def sconfig(gid,model,key,prompt):
    d=lconfig()
    d[gid]={"model":model,"apikey":key,"prompt":prompt}
    
    try:
        with open(configfiles,"w",newline="") as f:
            writer=csv.writer(f)
            for gid,config in d.items():
                writer.writerow([gid,config["model"],config["apikey"],config["prompt"]])
    except: print("error at scofnig")
                
      