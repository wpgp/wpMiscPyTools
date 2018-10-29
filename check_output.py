import os
import pandas as pd
import numpy as np
"""
Script to check output from WPRF. Checks presence of outfiles in all countries in all specified years

Variables to specify:
years = list of years' outputs to check
rootpath = Location of folders of output per country (A list will be made of folders in this directory).

Will print ISO's with missing files (HTML and csv) and log problem iso's in not_done_<year>.txt.

Will also print ISO's that have zonal stats difference max values greater than 0.4

Created by: David Kerr 29/10/2018 (email: dk2n16@soton.ac.uk)

"""
years = ['2000', '2012', '2014'] #Specify years to check
for year in years:
	rootpath = 'Y:/Projects/WP515640_Global/Working/RF_Output/ppp_prj_{0}_redone_12August'.format(year) #specify folders where output is held

	files_done = []
	files_not_done = []
	tables_not_matching = []

	folders = os.listdir(rootpath) 
	prj_folders = [] #Keep only wanted folders starting with "prj"
	for folder in folders:
		if folder.startswith('prj'):
			prj_folders.append(folder)

	for i in prj_folders:
		files_present = []
		if os.path.exists(os.path.join(rootpath, i, 'check_result_prj_prj_{0}_{1}.csv'.format(year, i[-3:]))):
			files_present.append('CSV present')
			df = pd.read_csv(os.path.join(rootpath, 'prj_{0}_{1}'.format(year, i[-3:]), 'check_result_prj_prj_{0}_{1}.csv'.format(year, i[-3:])))
			if df["DIFFERENCE"].max() > 0.4:
				print "Check {0} csv".format(i[-3:])
				tables_not_matching.append(i[-3:])
		else:
			print("{0} {1}: No csv".format(i[-3:], year))

		if os.path.exists(os.path.join(rootpath, i, 'report_prj_{0}_{1}.html'.format(year, i[-3:]))):
			files_present.append('HTML present')
		else:
			print("{0} {1}: No HTML".format(i[-3:], year))

		if len(files_present) == 2:
			files_done.append(i[-3:])
		else:
			print("REDO: {0} {1}".format(i[-3:], year))
			files_not_done.append(i[-3:])

	print("{0} countries completed for {1}".format(len(files_done), year))
	print("{0} countries not completed for {1}".format(len(files_not_done), year))
	file_name  = 'Not_done_{0}.txt'.format(year)
	f =	open(file_name, 'w')
	for file in files_not_done:
		f.write(file)
		f.write('\n')
	f.close()

	print("TABLES NOT MATCHING: {0}".format(tables_not_matching))
	tables_not_matching_filename = 'TABLES_{0}.txt'.format(year)
	f = open(tables_not_matching_filename, 'w')
	for file in tables_not_matching:
		f.write(file)
		f.write('\n')
	f.close()









