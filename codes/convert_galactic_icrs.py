# Python Script to convert our galactic coordinates to RA and Dec
# Corey Mutnik 3/3/16

from astropy.coordinates import SkyCoord
from astropy import units as u

l_list = [220, 223, 226, 229, 232, 235, 238, 241, 244, 247, 250, 250, 247, 244, 241, 238, 235, 232, 229, 226, 223, 220]
b_list = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

trans = SkyCoord(l=l_list, b=b_list, unit=(u.degree, u.degree), frame='galactic')
trans.icrs