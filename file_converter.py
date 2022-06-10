import pandas as pd
import json

def convert_csv_to_json(csv_data_file,json_file_converted,lat,long):
    df = pd.read_csv (csv_data_file)
    df = df.iloc[:,[lat,long]]
    df.columns=["latitude", "longitude"]
    df.to_json (json_file_converted,indent=4,orient="records")

#adapting the json file converted into a OpenElevation API json input format
def adapting_json(json_file_converted):
    file= open(json_file_converted)
    new_dict= json.load(file)
    new_dict= {"locations": new_dict}
    return(new_dict) 
    
def saving_formated_json(new_dict,final_json):
    with open(final_json, "w") as fp:
        json.dump(new_dict,fp,indent=4)

def saving_in_csv(results_list,csv_file_name):
    df = pd.DataFrame(results_list)
    df.to_csv (csv_file_name, index = None, header=["latitude", "longitude", "elevation"])

def saving_in_json(results_list,json_file_name):
        with open(json_file_name, 'w', newline="") as fp:
            json.dump(results_list, fp, indent=4)


