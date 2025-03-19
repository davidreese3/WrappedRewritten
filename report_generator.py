from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import data_loader as dl
import data_processor as dp
import data_visualizer as dv

def generate_figs(df, year, artist):
    df_original = df.copy()
    plots = {
        "MostPlayedAlbums": dp.mostPlayedAlbums(df_original.copy()),
        "MostPlayedSongs": dp.mostPlayedSongs(df_original.copy()),
        "MostPlayedArtist": dp.mostPlayedArtist(df_original.copy()) if artist == "" else None,
        "ListeningTimeByYear": dp.listeningTimeByYear(df_original.copy()) if year == "" else None,
        "MostSkippedTracks": dp.mostSkippedTracks(df_original.copy()),
        "ListeningByHour": dp.listeningByHour(df_original.copy()),
        "ListeningByWeekday": dp.listeningByWeekday(df_original.copy()),
        "ListeningHeatmap": dp.listeningHeatmap(df_original.copy()),
        "Top10RecurringSongsByMonth": dp.top10RecurringSongsByMonth(df_original.copy(), year) if year != "" else dp.top10RecurringSongsByMonth(df_original),
    }

    figures = []

    for name, data in plots.items():
        if data is not None and not data.empty:
            fig = getattr(dv, f"plot{name}")(data)
            figures.append(fig)

    return figures

def generate_report(df, year, artist):
    figures = generate_figs(df, year, artist)
    with PdfPages('report.pdf') as pdf:
        for fig in figures:
            pdf.savefig(fig)
            plt.close(fig)