import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns

def plotMostPlayedAlbums(df):
    df["album_artist"] = df["album"] + " (" + df["artist"] + ")"
    plt.plot(df["album_artist"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Album")
    plt.ylabel("Hours Played")
    plt.title("Top Albums by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotMostPlayedSongs(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    plt.plot(df["song_artist"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Song")
    plt.ylabel("Hours Played")
    plt.title("Top Songs by Hours Played")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotListeningTimeByYear(df):
    plt.plot(df["year"], df["hours_played"], marker="o", linestyle="-")
    plt.xlabel("Year")
    plt.ylabel("Hours Played")
    plt.title("Hours Played Per Year")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotMostSkippedTracks(df):
    df["song_artist"] = df["song"] + " (" + df["artist"] + ")"
    plt.plot(df["song_artist"], df["times_skipped"], marker="o", linestyle="-")
    plt.xlabel("Song")
    plt.ylabel("Times Skipped")
    plt.title("Times Skipped Per Song")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotListeningByHour(df):
    plt.plot(df["ts"], df["percent"], marker="o", linestyle="-")
    plt.xlabel("Time of Day")
    plt.ylabel("Percentage of listening")
    plt.title("Percentage of Listening at Time of Day")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotListeningByWeekday(df):
    plt.plot(df["weekday"], df["percent"], marker="o", linestyle="-")
    plt.xlabel("Day of Week")
    plt.ylabel("Percentage of listening")
    plt.title("Percentage of Listening at Day of Week")
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()
    plt.show()

def plotListeningHeatmap(df):
    sns.heatmap(df, cmap="viridis")
    plt.xlabel("Day of Week")
    plt.ylabel("Time of Day")
    plt.title("Heatmap of Streaming")
    plt.xticks(rotation=0)  
    plt.tight_layout()
    plt.show()


def plotTop10SongsByMonth(df):    
    plt.figure(figsize=(20, 30)) 
    sns.heatmap(df, cmap="viridis")
    plt.xlabel("Month")
    plt.ylabel("Song")
    plt.title("Heatmap of Top 10 Song")
    plt.xticks(rotation=0)  
    plt.tight_layout()
    plt.show()