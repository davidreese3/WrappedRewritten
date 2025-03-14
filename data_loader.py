import pandas as pd
import os

def load_spotify_data(file_location):
    dataframes = []
    files = getListOfFiles(file_location)
    for file in files:
        df = pd.read_json(file_location + "/" + file)
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

def getListOfFiles(file_location):
        listOfFiles = [file for file in os.listdir(file_location) if os.path.isfile(os.path.join(file_location, file))]
        listOfFilesToRemove = [file for file in listOfFiles if not("Streaming_History_Audio_" in file)]
        for file in listOfFilesToRemove:
             listOfFiles.remove(file)
        return listOfFiles