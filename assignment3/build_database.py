import os
from config import db
from models import Avocado, Avoregion, AvoType

# Data to initialize database with
# AVOCADO = [
#     {'date': '18-12-2011', 'avgprice': 30000, 'totalvol': 30,
#         'avo_a': 40, 'avo_b': 50, 'avo_c': 70, 'type': 1, 'regionid': 2}
# ]

AVOTYPE = [
    {'typeid': 1, 'type': 'matang'}
]

AVOREG = [
    {'regionid': 1, 'region': 'malang'},
    {'regionid': 2, 'region': 'asdasd'},
]
# Delete database file if it exists currently
if os.path.exists('avocado.db'):
    os.remove('avocado.db')

# Create the database
db.create_all()

for avotype in AVOTYPE:
    p = AvoType(typeid=avotype['typeid'], type=avotype['type'])
    db.session.add(p)

for avoreg in AVOREG:
    p = Avoregion(regionid=avoreg['regionid'], region=avoreg['region'])
    db.session.add(p)


# for avocado in AVOCADO:
#     p = Avocado(date=avocado['date'], avgprice=avocado['avgprice'], totalvol=avocado['totalvol'],
#                 avo_a=avocado['avo_a'], avo_b=avocado['avo_b'], avo_c=avocado['avo_c'],
#                 type=avocado['type'], regionid=avocado['regionid'])
#     db.session.add(p)

db.session.commit()
