ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# All routes without A-A and without duplicates (A-B and B-A)
routes = [(a, b) for a in ports for b in ports if a < b]
print(routes)
print(len(routes))