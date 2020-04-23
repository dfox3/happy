import os
import argparse
import glob
import csv
import pandas as pd
import seaborn as sns
import matplotlib as plt
sns.set_style("darkgrid")
sns.set_context("talk")
#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Plot Social Interactions')

parser.add_argument('-i',
                    metavar='-input',
                    type=str,
                    required=True,
                    help="Input directory, contains log .csvs from social_interactions.py")

def main():
	options = parser.parse_args()

	if not os.path.exists(str(options.i) + "/figures"):
		os.makedirs(str(options.i) + "/figures")
	header = []
	data_list = []
	log = str(options.i).split("/")[1]
	for file_name in glob.glob(str(options.i) + "*.csv"):
		print(file_name)
		temp_lists = []
		with open(file_name, 'r') as f:
			reader = csv.reader(f)
			temp_lists = list(reader)
		header = temp_lists[0] + ["npc", "count"]
		temp_lists = [ [ int(y) if i == 2 else y for i, y in enumerate(x) ] for x in temp_lists[1:] ]
		temp_lists = [ x + [file_name.split("_")[0].split("/")[-1], 1] for i, x in enumerate(temp_lists) ]
		data_list = data_list + temp_lists
	df = pd.DataFrame.from_records(data_list, columns=header)
	print(df)

	received = "sent"
	receiver = "receiver"
	if header[3] != "receiver":
		receiver = "sender"
		received = "received"

	x_vals = ["dialog", "order", receiver]

	influence = "feedback"
	if header[2] == "influence":
		influence = "influence"

	df.sort_values("npc")

	for x in x_vals:
		plt.pyplot.subplots_adjust(top=0.85)
		sns_plot = sns.catplot(x, col="npc", col_wrap=4,data=df,kind="count")
		sns_plot.set_xticklabels(rotation=90)
		sns_plot.fig.suptitle(str(log) + " " + str(x) + " total " + str(received) + " catfacetplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(x) + "_total_catfacetplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(x) + "_total_catfacetplot.png", dpi=311)

		#sns_plot = sns.barplot(x=x, y=influence, data=df, col="npc", col_wrap=4, kind="count")
		#sns_plot.set_xticklabels(rotation=90)
		#print("Printing " + str(options.i) + "/figures/" + str(x) + "_sum_influence_catfacetplot.png")
		#sns_plot.savefig(str(options.i) + "/figures/" + str(x) + "_sum_influence_catfacetplot.png", dpi=360)

		sns_plot = sns.catplot(x=x, y=influence, data=df, col="npc", col_wrap=4, kind="bar")
		sns_plot.set_xticklabels(rotation=90)
		sns_plot.fig.suptitle(str(log) + " " + str(x) + " mean influence " + str(received) + " catfacetplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(x) + "_mean_influence_catfacetplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(x) + "_mean_influence_catfacetplot.png", dpi=311)

		sns_plot = sns.catplot(x=x, y=influence, data=df, col="npc", col_wrap=4, kind="box")
		sns_plot.set_xticklabels(rotation=90)
		sns_plot.fig.suptitle(str(log) + " " + str(x) + " mean influence " + str(received) + " boxfacetplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(x) + "_mean_influence_boxfacetplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(x) + "_mean_influence_boxfacetplot.png", dpi=311)


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()