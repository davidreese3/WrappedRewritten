import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns

def main():
    start = time.time()
    df = setUp()
    #ta = topAlbums(df)
    #ts = topSongs(df)
    #tpy = timePerYear(df)
    #mss = mostSkippedSongs(df)    
    #mlttod = mostListenedToTimeOfDay(df)
    #mltdow = mostListenedToDayOfWeek(df)
    #mlthm = mostListenedToHeatMap(df)
    top10MonthToMonth(df, "2024")
    end = time.time()
    #topAlbumsPlot(ta)
    #topSongsPlot(ts)
    #timePerYearPlot(tpy)
    #mostSkippedSongsPlot(mss)
    #mostListenedToTimeOfDayPlot(mlttod)
    #mostListenedToDayOfWeekPlot(mltdow)
    #mostListenedToHeatMapPlotHeatMap(mlthm)
    print(f"Data calculated in: {end - start}")

def setUp():
    file_location_prefix = "my_spotify_data/Spotify Extended Streaming History/Streaming_History_Audio_"
    files = ["2018-2019_0","2019-2020_1","2020_2","2020_3","2020_4","2020-2021_5","2021_6","2021-2022_7",
             "2022_8","2022_9","2022-2023_10","2023_11","2023-2024_12","2024_13","2024-2025_14"]
    dataframes = []
    for file in files:
        df = pd.read_json(file_location_prefix + file + ".json")
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df

#sum of playtime of songs from each album
def topAlbums(df):
    albums = df.groupby(["master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().div(3600000)
    album_df = albums.reset_index().rename(columns={"master_metadata_album_album_name": "album", 
                                                "master_metadata_album_artist_name": "artist", 
                                                "ms_played": "hours_played"})
    album_df = album_df.sort_values(by="hours_played", ascending=False).head(10)
    return album_df

"""
sum of the most played songs, distinguishing by artist and album to account for different songs with the same name. 
however, it still differentiates between EP and LP versions.
"""
def topSongs(df):
    song = df.groupby(["master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().div(3600000)
    song_df = song.reset_index().rename(columns={"master_metadata_track_name" : "song",
                                                 "master_metadata_album_album_name" : "album",
                                                 "master_metadata_album_artist_name" : "artist",
                                                 "ms_played": "hours_played"})
    song_df = song_df.nlargest(10, "hours_played")
    return song_df

def timePerYear(df):
    df["year"] = df["ts"].str.split("-").str[0]
    time = df.groupby(["year"])["ms_played"].sum().div(3600000).reset_index(name="hours_played")
    return time

def mostSkippedSongs(df):
    skips = df.groupby(["skipped", "master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"]).size().reset_index(name="times_skipped")
    skips_df = skips.reset_index().rename(columns={"master_metadata_track_name" : "song",
                                                 "master_metadata_album_album_name" : "album",
                                                 "master_metadata_album_artist_name" : "artist"})
    skips_df = skips_df[skips_df["skipped"] != False]
    skips_df = skips_df.nlargest(10, "times_skipped")
    return skips_df

def mostListenedToTimeOfDay(df):
    df["ts"] = df["ts"].str.split("T").str[1].str.split(":").str[0]
    time_df = df.groupby(["ts"])["ms_played"].sum().reset_index(name="time")
    total_playtime = time_df["time"].sum()
    time_df["percent"] = time_df["time"]/total_playtime * 100
    return time_df

def mostListenedToDayOfWeek(df):
    df["ts"] = pd.to_datetime(df["ts"])  
    df["weekday"] = df["ts"].dt.day_name()
    day = df.groupby(["weekday"])["ms_played"].sum().reset_index(name="time")
    total_playtime = day["time"].sum()
    day["percent"] = day["time"]/total_playtime * 100
    return day

def mostListenedToHeatMap(df):
    df["ts"] = pd.to_datetime(df["ts"])    
    df["year"] = df["ts"].dt.year
    df["month"] = df["ts"].dt.month
    heatMap_df = df.groupby(["hr","weekday"])["ms_played"].sum().reset_index()
    total_playtime = heatMap_df["ms_played"].sum()
    heatMap_df["percent"] = heatMap_df["ms_played"]/total_playtime * 100
    
    weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    heatMap_df = heatMap_df.pivot(index="hr", columns="weekday", values="percent")
    heatMap_df = heatMap_df[weekdays]
    return heatMap_df

def top10MonthToMonth(df, year):
    df["year"] = df["ts"].str.split("T").str[0].str.split("-").str[0]
    df["month"] = df["ts"].str.split("T").str[0].str.split("-").str[1]
    month_year_df = df.groupby(["year","month","master_metadata_track_name", "master_metadata_album_album_name", "master_metadata_album_artist_name"])["ms_played"].sum().reset_index(name="play_time")  
    month_year_df = month_year_df.reset_index().rename(columns = { "master_metadata_track_name" : "song",
                                                  "master_metadata_album_album_name" : "album",
                                                  "master_metadata_album_artist_name" : "artist"})
    month_year_df = month_year_df[month_year_df["year"] == year] 
    print(month_year_df)   
    monthly_dfs = month_year_df.groupby("month").apply(lambda x: x.nlargest(10, "play_time")).reset_index(drop=True)
    monthly_dfs["song_artist"] = monthly_dfs["song"] + " (" + monthly_dfs["artist"] + ")"

def topAlbumsPlot(df):
    df["album_artist"] = df["album"] + " (" + df["artist"] + ")"
    plt.plot(df["album_artist"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Album")
    plt.ylabel("Hours Played")
    plt.title("Top Albums by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def topSongsPlot(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    plt.plot(df["song_artist"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Song")
    plt.ylabel("Hours Played")
    plt.title("Top Songs by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def timePerYearPlot(df):
    plt.plot(df["year"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Year")
    plt.ylabel("Hours Played")
    plt.title("Hours Played Per Year")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def mostSkippedSongsPlot(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    plt.plot(df["song_artist"], df["times_skipped"], marker="o", linestyle="-")
    plt.xlabel("Song")
    plt.ylabel("Times Skipped")
    plt.title("Times Skipped Per Song")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def mostListenedToTimeOfDayPlot(df):
    plt.plot(df["ts"], df["percent"], marker="o", linestyle="-")
    plt.xlabel("Time of Day")
    plt.ylabel("Percentage of listening")
    plt.title("Percentage of Listening at Time of Day")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def mostListenedToDayOfWeekPlot(df):
    plt.plot(df["weekday"], df["percent"], marker="o", linestyle="-")
    plt.xlabel("Day of Week")
    plt.ylabel("Percentage of listening")
    plt.title("Percentage of Listening at Day of Week")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def mostListenedToHeatMapPlotHeatMap(df):
    sns.heatmap(df, cmap="viridis")
    plt.xlabel("Day of Week")
    plt.ylabel("Time of Day")
    plt.title("Heatmap of Streaming")
    plt.xticks(rotation=0)  
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
