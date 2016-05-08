# Python script to isolate items with same RA & Dec but different magnitudes
# Corey Mutnik 3/2/16
'''
Basically what you want to do is read in everything, sort on Dec
(otherwise you get annoyances from the RA wrap around 360-0), and then
go through the list trying to match each star with others that are
closer than some tolerance, say 0.001 deg.  This is fast because a
quicksort is fast and because you don't have to go very far down the
list before the (sorted) Dec exceeds your tolerance.
'''
import numpy as np
from astropy.io import ascii
from glob import glob
import os

dir_path = u'/Users/cmutnik/work/classes/astr301/variable_proposal/gri_data/57396_dph'
globpath = os.path.join(dir_path, '*.dph')
filelist = glob(globpath)
filelist.sort()

#problem_file= ascii.read(filelist[201]) # 01p57396o0194g1.dph

cat = ascii.read(filelist[0])
cat.colnames
#>>['RA', 'Dec', 'm', 'idx', 'Type', 'xtsk', 'ytsk', 'fitmag', 'dfitmag', 'sky', 'major', 'minor', 'phi', 'probgal', 'apmag', 'dapmag', 'apsky', 'ap-fit']
# allow leeway to account for not perfectly absolute positions of stars

'''
# SEARCHES THROUGH ONE FILE
for i in range(len(cat['RA'])):
	for j in range(i+1, len(cat['RA'])):
		if cat['RA'][j] >= (cat['RA'][i]-0.00005) and cat['RA'][j] <= (cat['RA'][i]+0.00005):
			if cat['Dec'][j] >= (cat['Dec'][i]-0.00005) and cat['Dec'][j] <= (cat['Dec'][i]+0.00005):
				if cat['m'][i] != cat['m'][j]:
					print 'RA_1: ', cat['RA'][i], '\tDec_1: ' , cat['Dec'][i], '\tm_1: ', cat['m'][i], '\n', 'RA_2: ', cat['RA'][j], '\tDec_2: ' , cat['Dec'][j], '\tm_2: ', cat['m'][j], '\n\n'
'''

# NEEDS TO BE SORTED BY Dec
for k in range(len(filelist)):
	cat1 = ascii.read(filelist[k])
	for l in range(k+1, len(filelist)):
		cat2 = ascii.read(filelist[l])
		for i in range(len(cat1['RA'])):
			for j in range(i+1, len(cat1['RA'])):
				if cat2['RA'][j] >= (cat1['RA'][i]-0.00005) and cat2['RA'][j] <= (cat1['RA'][i]+0.00005):
					if cat2['Dec'][j] >= (cat1['Dec'][i]-0.00005) and cat2['Dec'][j] <= (cat1['Dec'][i]+0.00005):
						if cat1['m'][i] != cat2['m'][j]:
							print 'RA_1: ', cat1['RA'][i], '\tDec_1: ' , cat1['Dec'][i], '\tm_1: ', cat1['m'][i], '\n', 'RA_2: ', cat2['RA'][j], '\tDec_2: ' , cat2['Dec'][j], '\tm_2: ', cat2['m'][j], '\n\n'





