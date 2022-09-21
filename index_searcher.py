import csv

def index_return(word,header):
    for i in header:
        if (i == word):
            return header.index(i)
    return False

def searcher(alias,header):
    for i in range(len(alias)):
        index= index_return(alias[i],header)
        if index != False:
            return  index
    return False

def read_header(input_csv_filename):
    with open(input_csv_filename, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        #Removing white space
        for i in range(len(row1)):
            row1[i] = row1[i].replace(" ","")
    return row1
    
latitude_alias= ['Latitude','latitude','Lat','lat','LAT','LATITUDE','Lati','lati']
longitude_alias= ['Longitude','longitude','Long','long','Lon','lon','LON','LONGITUDE']


def lat_col_ind(input_csv_filename):
    return searcher(latitude_alias,read_header(input_csv_filename))

def long_col_ind(input_csv_filename):
    return searcher(longitude_alias,read_header(input_csv_filename))
