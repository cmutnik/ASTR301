# Py script to determine max and min of RA and Dec
# Corey Mutnik 6/23/16

from astropy.io import ascii


no_offset = ascii.read('observation_list_RR_Lyrae_160322.txt')
offset = ascii.read('observation_list_RR_Lyrae_160323.txt')


RA_no_offset = no_offset['RA[deg]']
RA_offset = offset['RA[deg]']

Dec_no_offset = no_offset['Dec[deg]']
Dec_offset = offset['Dec[deg]']


max_RA_no_offset = max(RA_no_offset)
max_RA_offset = max(RA_offset)
max_Dec_no_offset = max(Dec_no_offset)
max_Dec_offset = max(Dec_offset)

min_RA_no_offset = min(RA_no_offset)
min_RA_offset = min(RA_offset)
min_Dec_no_offset = min(Dec_no_offset)
min_Dec_offset = min(Dec_offset)


max_RA_offset 		# 116.4583940353
max_RA_no_offset 	# 116.35511714

min_RA_no_offset 	# 93.357665409999996
min_RA_offset 		# 93.458500016900004

max_Dec_no_offset 	# 11.998083230000001
max_Dec_offset 		# 11.998083230000001

min_Dec_no_offset 	# -19.231548220000001
min_Dec_offset 		# -19.231548220000001


upper_RA_limit = max_RA_offset + 3. # FOV is 5[deg], r=2.5[deg], so add 3[deg] to account for mispointings and the like
#>> 119.4583940353
lower_RA_limit = min_RA_no_offset - 3.
#>> 90.357665409999996
upper_Dec_limit = max_Dec_offset + 3.
#>> 14.998083230000001
lower_Dec_limit = min_Dec_no_offset - 3.
#>> -22.231548220000001

