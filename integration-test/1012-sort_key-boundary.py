# Adds tests for OSM features (but not NE features)

# country boundary of USA
#https://www.openstreetmap.org/relation/148838
assert_has_feature(
    8, 39, 95, "boundaries",
    {"kind": "country", "id": -148838,
     "sort_key": 262})

# region boundary between Nevada - California
#https://www.openstreetmap.org/relation/165473
#https://www.openstreetmap.org/relation/165475
assert_has_feature(
    8, 42, 96, "boundaries",
    {"kind": "region", "id": -165473,
     "sort_key": 256})

# county boundary between Mendocino County - Humboldt County
#https://www.openstreetmap.org/relation/396458
#https://www.openstreetmap.org/relation/396489
assert_has_feature(
    10, 159, 387, "boundaries",
    {"kind": "county", "id": -165473,
     "sort_key": 254})

# locality boundary between San Francisco - Daly City
#https://www.openstreetmap.org/relation/111968
#https://www.openstreetmap.org/relation/112271
assert_has_feature(
    10, 163, 396, "boundaries",
    {"kind": "locality", "id": -111968,
     "sort_key": 252})
