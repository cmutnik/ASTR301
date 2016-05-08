# Python Script to convert our galactic coordinates to RA and Dec
# Corey Mutnik 3/3/16

from astropy.coordinates import SkyCoord
from astropy import units as u

l_list = [202, 205, 208, 211, 214, 217, 220, 223, 226, 229, 232, 232, 229, 226, 223, 220, 217, 214, 211, 208, 205, 202]
b_list = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
len(l_list) == len(b_list)

trans = SkyCoord(l=l_list, b=b_list, unit=(u.degree, u.degree), frame='galactic')
trans.icrs