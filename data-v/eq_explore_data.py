from fileinput import filename
import json

#explore the structure of data
filename = 'data/eq_data_1_day_m1.json'
with open (filename) as f :
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file , W) as f :
    # json.dump(all_eq_data,f,indent=4)

mags ,lons , lats = [],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])