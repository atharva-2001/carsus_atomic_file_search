import requests
WEIGHTSCOMP_URL = "http://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl"
res = requests.get(WEIGHTSCOMP_URL, params={'ascii': 'ascii2', 'isotype': 'some'})
