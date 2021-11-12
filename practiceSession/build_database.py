import os
from config import db
from models import Avocado

# Data to initialize database with
AVOCADO = [
    {'date': '18-12-2011', 'avgprice': 30000, 'totalvol': 30,
        'avo_a': 40, 'avo_b': 50, 'avo_c': 70, 'type': 1, 'regionid': 3}
]

# Delete database file if it exists currently
if os.path.exists('avocado.db'):
    os.remove('avocado.db')

# Create the database
db.create_all()


for avocado in AVOCADO:
    p = Avocado(date=avocado['date'], avgprice=avocado['avgprice'], totalvol=avocado['totalvol'],
                avo_a=avocado['avo_a'], avo_b=avocado['avo_b'], avo_c=avocado['avo_c'],
                type=avocado['type'], regionid=avocado['regionid'])
    db.session.add(p)

db.session.commit()
