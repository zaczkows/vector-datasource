tiles = [
    # there are TWO Target stores in this tile - and both are huge!
    ['14/2618/6338', set([152722810, 56149856]), 'department_store'],
    ['14/2620/6333', 219072560, 'supermarket'],
    ['14/2618/6338', 344057345, 'supermarket'],
    ['14/2621/6334', 259001359, 'doityourself'],
    ['15/5240/12668', 194906343, 'supermarket'],
    ['15/5236/12666', -3585039, 'supermarket'],
]

for zxy, id, kind in tiles:
    z, x, y = map(int, zxy.split('/'))
    assert_has_feature(z, x, y, 'pois', {'kind': kind, 'id': id})
