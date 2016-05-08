# Py script to determine max and min of RA and Dec
# Corey Mutnik 3/25/16
# mod of 'RADec.maxmin.py'

from astropy.io import ascii
import numpy as np

no_offset = ascii.read('observation_list_RR_Lyrae_160322.txt')
offset = ascii.read('observation_list_RR_Lyrae_160323.txt')

# make empty lists
b_of_0_no_offset, b_of_0_offset, b_of_1_no_offset, b_of_1_offset = [], [], [], []
# sort by b=+5 and b=-5
for m in range(len(no_offset['Obs_ID'])):
	b_value = no_offset['Obs_ID'][m][3:-5]
	#print b_value
	if b_value == '0':
		b_of_0_no_offset.append([no_offset['RA[deg]'][m], no_offset['Dec[deg]'][m]])
		b_of_0_offset.append([offset['RA[deg]'][m], offset['Dec[deg]'][m]])
	else:
		b_of_1_no_offset.append([no_offset['RA[deg]'][m], no_offset['Dec[deg]'][m]])
		b_of_1_offset.append([offset['RA[deg]'][m], offset['Dec[deg]'][m]])


# cast lists as arrays
b_of_0_no_offset, b_of_0_offset, b_of_1_no_offset, b_of_1_offset = np.array(b_of_0_no_offset), np.array(b_of_0_offset), np.array(b_of_1_no_offset), np.array(b_of_1_offset)


# max and min values [deg] with no offset at b=0 
b_0_nooff_RA_max = max(b_of_0_no_offset[:,0]) 
#>> 107.16172785000001
b_0_nooff_Dec_max = max(b_of_0_no_offset[:,1])
#>> 7.3768987800000003
b_0_nooff_RA_min = min(b_of_0_no_offset[:,0])
#>> 93.357665409999996
b_0_nooff_Dec_min = min(b_of_0_no_offset[:,1])
#>> -19.231548220000001

# max and min values [deg] with offset at b=0 
b_0_off_RA_max = max(b_of_0_offset[:,0]) 
#>> 107.26763815930001
b_0_off_Dec_max = max(b_of_0_offset[:,1])
#>> 7.3768987800000003
b_0_off_RA_min = min(b_of_0_offset[:,0])
#>> 93.458500016900004
b_0_off_Dec_min = min(b_of_0_offset[:,1])
#>> -19.231548220000001

# max and min values [deg] with no offset at b=1
b_1_nooff_RA_max = max(b_of_1_no_offset[:,0]) 
#>> 116.35511714
b_1_nooff_Dec_max = max(b_of_1_no_offset[:,1])
#>> 11.998083230000001
b_1_nooff_RA_min = min(b_of_1_no_offset[:,0])
#>> 102.35705234
b_1_nooff_Dec_min = min(b_of_1_no_offset[:,1])
#>> -14.47179442

# max and min values [deg] with offset at b=1
b_1_off_RA_max = max(b_of_1_offset[:,0]) 
#>> 116.4583940353
b_1_off_Dec_max = max(b_of_1_offset[:,1])
#>> 11.998083230000001
b_1_off_RA_min = min(b_of_1_offset[:,0])
#>> 102.4592856726
b_1_off_Dec_min = min(b_of_1_offset[:,1])
#>> -14.47179442




