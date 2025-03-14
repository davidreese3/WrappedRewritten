import pandas as pd

def load_spotify_data():
    file_location_prefix = "my_spotify_data/Spotify Extended Streaming History/Streaming_History_Audio_"
    files = ["2018-2019_0","2019-2020_1","2020_2","2020_3","2020_4","2020-2021_5","2021_6","2021-2022_7",
             "2022_8","2022_9","2022-2023_10","2023_11","2023-2024_12","2024_13","2024-2025_14"]
    dataframes = []
    for file in files:
        df = pd.read_json(file_location_prefix + file + ".json")
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df