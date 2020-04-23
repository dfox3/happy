import os
import argparse
import glob
import csv
import pandas as pd
import seaborn as sns
import matplotlib as plt
sns.set_style("darkgrid")
#sns.set_context("talk")
#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Plot Social Mutations')

parser.add_argument('-i',
                    metavar='-input',
                    type=str,
                    required=True,
                    help="Input directory, contains log .csvs from social_interactions.py")

def main():
	options = parser.parse_args()

	log = str(options.i).split("/")[1]
	if not os.path.exists(str(options.i) + "/figures"):
		os.makedirs(str(options.i) + "/figures")
	header = []
	data_list = []
	for file_name in glob.glob(str(options.i) + "*.csv"):
		print(file_name)
		temp_lists = []
		with open(file_name, 'r') as f:
			reader = csv.reader(f)
			temp_lists = list(reader)
		header = ["iteration"] + temp_lists[0] + ["npc"]
		temp_lists = [ [ int(y) for y in x ] for x in temp_lists[1:] ]
		temp_lists = [ [i] + x + [file_name.split("_")[0].split("/")[-1]] for i, x in enumerate(temp_lists) ]
		data_list = data_list + temp_lists
	df = pd.DataFrame.from_records(data_list, columns=header)
	print(df)

	df.sort_values("npc")

	y_vals = ["happiness", "social", "open_mindedness", "giving", "funnybone"]
	
	for y in y_vals:
		sns_plot = sns.relplot(x="iteration", y=y, hue="npc", kind="line", data=df, linewidth=.5, alpha=.9)
		sns_plot.fig.suptitle(str(log) + " " + str(y) + " mutations comboplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(y) + "_comboplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(y) + "_comboplot.png", dpi=420)
		sns_plot = sns.relplot(x="iteration", y=y, hue="npc", kind="line", data=df, linewidth=2, alpha=1, col="npc", col_wrap=4)
		sns_plot.fig.suptitle(str(log) + " " + str(y) + " mutations facetplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(y) + "_facetplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(y) + "_facetplot.png", dpi=311)


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()