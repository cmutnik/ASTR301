# Python Script to convert our galactic coordinates to RA and Dec
# Corey Mutnik 3/3/16

from astropy.coordinates import SkyCoord
from astropy import units as u

# lists of l and b (galactic coors) to convert
l_list = [165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195]
bp5 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


trans = SkyCoord(l=l_list, b=bp5, unit=(u.degree, u.degree), frame='galactic')

# prints out the coordinates in RA & Dec [deg]
trans.icrs