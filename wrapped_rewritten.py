import pandas as pd
import os
import matplotlib.pyplot as plt
import time
import seaborn as sns
# my files
import data_processor as dp
import data_visualizer as dv
import report_generator as rg
import data_loader as dl

def main():
    print("Select a year (leave blank for all):")
    year = input()
    print("Select an artist (leave blank for all):")
    artist = input()
    print("Please wait...")
    df = dl.load_spotify_data("my_spotify_data/Spotify Extended Streaming History", year, artist)
    start = time.time()
    rg.generate_reports(df, year, artist)
    end = time.time()
    print(f"Data processed and visualized in: {end - start}")

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
