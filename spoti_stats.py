import pandas as pd
import os
import matplotlib.pyplot as plt

def main():
    file_location_prefix = "my_spotify_data/Spotify Extended Streaming History/Streaming_History_Audio_"
    files = ["2018-2019_0","2019-2020_1","2020_2","2020_3","2020_4","2020-2021_5","2021_6","2021-2022_7",
             "2022_8","2022_9","2022-2023_10","2023_11","2023-2024_12","2024_13","2024-2025_14"]
    dataframes = []
    for file in files:
        df = pd.read_json(file_location_prefix + file + ".json")
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    topAlbumsPlot(topAlbums(combined_df))

#sum of playtime of songs from each album
def topAlbums(df):
    albums = df["master_metadata_album_album_name"].unique()
    album_counts = {album: 0 for album in albums}  

    for index, row in df.iterrows():
        album_name = row["master_metadata_album_album_name"]
        if album_name in album_counts:
            album_counts[album_name] += (row["ms_played"]/60000)


    album_df = pd.DataFrame(album_counts.items(), columns=["album", "minutes_played"])
    album_df = album_df.sort_values(by="minutes_played", ascending=False)
    album_df = album_df.head(10)
    return album_df

def topAlbumsPlot(df):
    plt.plot(df["album"], df["minutes_played"], marker="o", linestyle="-")
    plt.xlabel("Album")
    plt.ylabel("Minutes Played")
    plt.title("Top Albums by Minutes Played")
    plt.xticks(rotation=45, ha="right")  
    plt.show()

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       