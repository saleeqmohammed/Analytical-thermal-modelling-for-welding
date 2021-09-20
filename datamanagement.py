import pickle
def save_object(obj,file_name):
    try:
        with open("savedata/"+file_name+".pickle", "wb") as f:
            pickle.dump(obj,f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
        
def load_object(filename):
    try:
        with open("savedata/"+filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        
        print("Can't locate save data...\n estimating new parameters...:", ex)
        
