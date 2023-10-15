#słownik

countryLeaders = {'PL':'Duda', 'US':'Trump'}

print(countryLeaders['US'])

countryLeaders['DE'] = 'Merkel'
print(countryLeaders)

print(countryLeaders.keys())
print(countryLeaders.values())
print(countryLeaders.items())
#print(countryLeaders.pop('PL'))

print(countryLeaders.get('RU'))

newLeaders = {'RU':'Putin', 'DE':'Schultz'}
print(newLeaders)

countryLeaders.update(newLeaders)
print(countryLeaders)

#ZAD1

channels = {'Google':1480,'Email':300,'Natural Traffic':440,'TV Spot':700}
print(channels['Email'])

channelsUpdate = {'Natural Traffic':500,'News':600}

channels.update(channelsUpdate)
print(channels)

print(channels.keys())
channels.pop('Email')
print(channels)
