

# parsing

n = int(input())

photos = list()

for i in range(n):
    line = input().split(" ")
    position = line[0]
    features = line[2:]
    photo = {
        'position': position,
        'features': features,
        'id': i
    }
    photos.append(photo)

res = []
picked = [False] * len(photos)

slide = [photos[0]]

verticals = [x for x in photos if x['position'] == 'V']
horizontals = [x for x in photos if x['position'] == 'H']

# group verticals
v = []
tmp = []
for i in range(0, len(verticals), 2):
    tmp.append([verticals[i], verticals[i + 1]])
verticals = tmp

res = []

picked_h = [False] * len(horizontals)
picked_v = [False] * len(verticals)

if len(horizontals):
    res.append([horizontals[0]])
    features = horizontals[0]['features']
    picked_h[0] = True
else:
    res.append(verticals[0])
    picked_v[0] = True
    features = verticals[0][0]['features'] + verticals[0][1]['features']

while len(res) != len(verticals) + len(horizontals):
    found = False
    for feature in features:
        if found:
            break
        for i, horizontal in enumerate(horizontals):
            if picked_h[i]:
                continue
            if feature in horizontal['features']:
                print(horizontal['id'])
                found = True
                picked_h[i] = True
                res.append([horizontal])
                features = horizontal['features']
                break
    if found:
        continue
    for feature in features:
        if found:
            break
        for i, vertical in enumerate(verticals):
            if picked_v[i]:
                continue
            for v in vertical:
                if feature in v['features']:
                    print(str(vertical[0]['id']) + " " + str(vertical[1]['id']))
                    found = True
                    picked_v[i] = True
                    res.append(vertical)
                    features = vertical[0]['features'] + vertical[1]['features']
                    break
            if found:
                break
    if found:
        continue
    for feature in features:
        if found:
            break
        for i, vertical in enumerate(verticals):
            if picked_v[i]:
                continue
            else:
                print(str(vertical[0]['id']) + " " + str(vertical[1]['id']))
                found = True
                res.append(vertical)
                picked_v[i] = True
                features = vertical[0]['features'] + vertical[1]['features']
        if found:
            break
        for i, horizontal in enumerate(horizontals):
            if picked_h[i]:
                continue
            else:
                print(horizontal['id'])
                found = True
                res.append([horizontal])
                picked_h[i] = True
                features = horizontal['features']
    if not found:
        break
"""
print(len(res))
for photo in res:
    if len(photo) == 1:
        print(photo[0]['id'])
    else:
        print(str(photo[0]['id']) + " " + str(photo[1]['id']))
"""
