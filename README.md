# CSV_Elevation_Getter
A python3 script that reads a csv file with latitude and longitude coordinates and obtains the respective elevation coordinates using the Open-Elevation API and saves in CSV or JSON format.

## Required Libs
**requests** > install pasting " python -m pip install requests " in your cmd
**pandas**  > install pasting  " pip install pandas " in your cmd

# How to use
Rename the input_csv_filename in code preserving the ".csv" 

 1. Download this code in ZIP format from the green button Code above.
 2. Extract the ZIP and paste your .csv file inside the folder
 3. Rename the variable **input_csv_filename** inside the script to your csv namefile preserving the ".csv" ( or just rename your csv file to input.csv)
 4. Run the **altitude.py** from your python terminal
 5. Done! The output.csv you be created

	input_csv_filename = "input.csv"
	output_csv_filename = "output.csv"
	output_json_filename= "output.json"