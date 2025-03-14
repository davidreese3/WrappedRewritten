import pandas as pd
import os

def load_spotify_data(file_location, year="", artist=""):
    dataframes = []
    files = getListOfFiles(file_location, year)
    for file in files:
        df = pd.read_json(file_location + "/" + file)
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    if year != "":
        combined_df["year"] = combined_df["ts"].str.split("-").str[0]
        combined_df = combined_df[combined_df["year"] == year]
    if artist != "":
        combined_df["artist"] = combined_df["master_metadata_album_artist_name"]
        combined_df = combined_df[combined_df["artist"] == artist]
    return combined_df

def getListOfFiles(file_location, year=""):
        listOfFiles = [file for file in os.listdir(file_location) if os.path.isfile(os.path.join(file_location, file))]
        listOfFilesToRemove = [file for file in listOfFiles if not("Streaming_History_Audio_" in file)]
        if year != "":
            for file in listOfFiles:
                if year not in file and file not in listOfFilesToRemove:
                    listOfFilesToRemove.append(file)
        
        for file in listOfFilesToRemove:
             listOfFiles.remove(file)
        return listOfFiles