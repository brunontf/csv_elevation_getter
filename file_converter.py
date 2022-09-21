import pandas as pd
import json

def csv_limit_size_check(input,chunks):
    df= pd.read_csv(input)
    n_rows= df.shape[0]
    limit= 1000
    total_int_parts= int (n_rows/limit)

    if n_rows>limit:
        for i in range(total_int_parts +2):
            chunks.append( limit*i)
        
        #changing the last value
        if ((n_rows%limit)==0):
            chunks.pop()
        chunks.pop()
        chunks.append(n_rows)
    
    else:
        chunks.append(0)
        chunks.append(n_rows)

    # print(chunks)
        
    return chunks

def convert_csv_to_json(csv_data_file,json_file_converted,lat,long,inf_lmt,sup_lmt):
    df = pd.read_csv(csv_data_file)
    df = df.iloc[inf_lmt:sup_lmt,[lat,long]]
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

def saving_in_csv(results_list,csv_file_name,header):
    df = pd.DataFrame(results_list)
    if header>0:
        df.to_csv (csv_file_name, mode='a', index = None, header=False)
    else:
        df.to_csv (csv_file_name, mode='a', index = None, header=["latitude", "longitude", "elevation"])

def saving_in_json(output_csv_filename,json_file_name):
    df=pd.read_csv(output_csv_filename)
    df.to_json(json_file_name,indent=4, orient="records")
        # with open(json_file_name, 'w', newline="") as fp:
        #     json.dump(results_list, fp, indent=4)


