# script for generating plots of stars
# Corey Mutnik 3/16/16

import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os



dir_path = u'/Users/cmutnik/work/classes/astr301/rrtest_outputs/rrtest.98.99.0.1/allstars.98.99.0.1'

# first test with single fits file

globpath = os.path.join(dir_path, 'grp.*')
filelist = glob(globpath)
filelist.sort() # so we are know which file we are working with


for m in range(len(filelist)):
	stardat = filelist[m]
	plot_title = 'Star ' + str(m+1) + ': 98 < RA < 97 , -1 < Dec < 0'
	plot_name = 'star' + str(m+1) + '.97.98.-1.0.png'
	dfile = np.genfromtxt(stardat)
	date = dfile[:,2]
	filt = dfile[:,5] #g=0, r=1, i=2
	mag = dfile[:,8]
	mag_err = dfile[:,9]
	plt.clf()
	plt.title(plot_title)
	plt.xlabel('Time [MJD]')
	plt.ylabel('m')
	#plt.xlim(57452,57460)
	for n in range(len(filt)):
		if filt[n] == 0:
			plt.errorbar(date[n], mag[n], yerr=mag_err[n], fmt='g.')
		elif filt[n] == 1:
			plt.errorbar(date[n], mag[n], yerr=mag_err[n], fmt='r.')
		else:
			plt.errorbar(date[n], mag[n], yerr=mag_err[n], fmt='b.')
	#plt.show()
	plt.savefig(plot_name)