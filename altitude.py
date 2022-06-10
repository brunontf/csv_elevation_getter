import requests
import file_converter

# input variables

input_csv_filename =  "input.csv"
output_csv_filename = "output.csv"
output_json_filename= "output.json" #You need to uncomment below
latitude_column_number= 3  #remember that the first column is "0", and that the LAT column must necessarily be before the Long column in the csv file
longitude_column_number=4

json_file_converted = 'temp_json.json' #temp file created
# _______________________________________________________________________

# Converting the CSV file into a JSON file
file_converter.convert_csv_to_json(input_csv_filename,json_file_converted,latitude_column_number,longitude_column_number)

#Using OpenElevation API
data= file_converter.adapting_json(json_file_converted)
elevation_list = requests.post('https://api.open-elevation.com/api/v1/lookup', json=data)
elevation_list = elevation_list.json()['results']

#saving the data as CSV format
file_converter.saving_in_csv(elevation_list, output_csv_filename)

#saving the data as JSON array format
# file_converter.saving_in_json(elevation_list, output_json_filename)

# Do you wanna save the OpenElevation API formated json???
# file_converter.saving_formated_json(data,json_file_converted)

print("\n DONE!")