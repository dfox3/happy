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
parser = argparse.ArgumentParser(description='Plot Relationships')

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
		header = temp_lists[0]
		temp_lists = [ [ int(y) if (i == 2 or i == 3) else y for i, y in enumerate(x) ] for x in temp_lists[1:] ]
		temp_lists = [ x for x in temp_lists ]
		data_list = temp_lists
		name = file_name.split("_")[0].split("/")[-1]
		relationship = header[1]
		df = pd.DataFrame.from_records(data_list, columns=header)
		print(df)

		df.sort_values(relationship)

		plt.pyplot.subplots_adjust(top=0.85)
		sns_plot = sns.relplot(x="iteration", y="value", hue=relationship, kind="line", data=df, linewidth=.5, alpha=.9)
		sns_plot.fig.suptitle(str(log) + " " + str(name) + " " + str(relationship) + " comboplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(name) + "_" + str(relationship) + "_comboplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(name) + "_" + str(relationship) + "_comboplot.png", dpi=420)
		sns_plot = sns.relplot(x="iteration", y="value", hue=relationship, kind="line", data=df, linewidth=2, alpha=1, col=relationship, col_wrap=4)
		sns_plot.fig.suptitle(str(log) + " " + str(name) + " " + str(relationship) + " facetplot", y=1.03)
		print("Printing " + str(options.i) + "/figures/" + str(name) + "_" + str(relationship) + "_facetplot.png")
		sns_plot.savefig(str(options.i) + "/figures/" + str(name) + "_" + str(relationship) + "_facetplot.png", dpi=311)


#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()