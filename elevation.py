import requests
import file_converter
import validation as val
import index_searcher as ind_search



# input vars

input_csv_filename =  "input.csv"
output_csv_filename = "output.csv"
output_json_filename= output_csv_filename.replace('csv','json')
latitude_column_number= ind_search.lat_col_ind(input_csv_filename)
longitude_column_number= ind_search.long_col_ind(input_csv_filename)
CSV_save= True
JSON_save= False

json_file_converted = 'temp_json.json' #temp file created

# Inputs Validation

input_csv_filename = val.validate_file(input_csv_filename,'csv','input')
output_csv_filename = val.validate_file(output_csv_filename,'csv','output')
output_json_filename = val.validate_file(output_json_filename,'json','output')

if latitude_column_number == False:
    latitude_column_number= int(input("It was not possible to detect the latitude column :(  \nCould you inform the column number manually?\nremember that the first column is \"0\"\n")) 
if longitude_column_number == False:
    longitude_column_number= int(input("It was not possible to detect the longitude column :(  \nCould you inform the column number manually?\nremember that the first column is \"0\"\n"))

# checks if the lat column comes first than long column
if latitude_column_number > longitude_column_number:
    temp= longitude_column_number
    longitude_column_number= latitude_column_number
    latitude_column_number= temp


# Altitude Program_______________________________________________________________________

# POST method limit checker
chunks=[]
file_converter.csv_limit_size_check(input_csv_filename,chunks)

for i in range((len(chunks))-1):
    inf_lmt,sup_lmt= chunks[i],chunks[i+1]

    # Converting the CSV file into a JSON file
    file_converter.convert_csv_to_json(input_csv_filename,json_file_converted,latitude_column_number,longitude_column_number,inf_lmt,sup_lmt)
    
    #Using OpenElevation API
    data= file_converter.adapting_json(json_file_converted)
    elevation_list = requests.post('https://api.open-elevation.com/api/v1/lookup', json=data)
    elevation_list = elevation_list.json()['results']

    #saving the data as CSV format
    if CSV_save == True:
        file_converter.saving_in_csv(elevation_list, output_csv_filename,i)

#saving the data as JSON array format
if JSON_save == True:
    file_converter.saving_in_json(output_csv_filename, output_json_filename)

# Do you wanna save the OpenElevation API formated json???
# file_converter.saving_formated_json(data,json_file_converted)

print("\n DONE!")
