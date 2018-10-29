import os
import shutil

years = ['2005', '2009', '2010', '2011']
for year in years:
	rootpath = 'Y:/Projects/WP515640_Global/Working/RF_Output/ppp_prj_{0}'.format(year)
	iso_list_all = os.listdir(rootpath)
	iso_list = []

	for iso in iso_list_all:
		if not iso.startswith('prj_'):
			iso_list.append(iso)
	#iso_list.remove('ADDED_LATER')


	countries_done = []
	for iso in iso_list:
		zonal_stats = os.path.join(rootpath, iso, 'zonal_stats')
		dst = os.path.join(rootpath, 'prj_{0}_{1}'.format(year, iso), 'zonal_stats')
		shutil.move(zonal_stats, dst)
		countries_done.append(iso)
		print(iso)

	print('Countries done for {0}: {1}'.format(year, len(countries_done)))



