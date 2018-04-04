#!/usr/bin/python3

import utils


ret = utils.getPlaceDetails('ChIJmdGMo6p0Z0gRG8wj-rEOUbo', 'AIzaSyBa9A13FXwxEaRVTQWru0_Q0vLxZUFNx2U')

for x in ret:
    print(x)