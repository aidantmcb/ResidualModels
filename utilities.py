def get_aspcap_path(telescope = None, field = None, sourceid = None, row = None):
    if row is not None:
        telescope, field, sourceid = (np.array(row['TELESCOPE'], dtype = str), np.array(row['FIELD'], dtype = str), 
                                      np.array(row['APOGEE_ID'], dtype = str))
    specdir = '/uufs/chpc.utah.edu/common/home/sdss/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/{TELESCOPE}/{FIELD}/'
    specname = 'aspcapStar-dr17-{SOURCEID}.fits'
    path = (specdir + specname).format(TELESCOPE = telescope, FIELD = field, SOURCEID = sourceid)
    return path

def get_apstar_path(telescope = None, field = None, fname = None, hdul = None):
    if hdul is not None:
        telescope, field, fname = (str(hdulist[4].data['TELESCOPE'][0]),str(hdulist[4].data['FIELD'][0]),str(hdulist[4].data['FILE'][0]))
    specdir = '/uufs/chpc.utah.edu/common/home/sdss/dr17/apogee/spectro/redux/dr17/stars/{TELESCOPE}/{FIELD}/'
    path = (specdir + fname).format(TELESCOPE = telescope, FIELD = field)
    return path