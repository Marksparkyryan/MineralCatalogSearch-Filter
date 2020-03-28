# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# import django
# from django.db import models, migrations, transaction, IntegrityError
# import os
# import json
# import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# class Migration(migrations.Migration):
#     """custom data migration from minerals.json"""

#     def populate_db(apps, schema_editor):
#         """fetches and reads minerals.json if not in testing mode. Json 
#         objects are then loaded into the database.
#         """
#         if 'test' not in sys.argv:
#             Mineral = apps.get_model('mineralsearchapp', 'Mineral')
#             with open(os.path.join(BASE_DIR, "minerals.json"),
#                         encoding="utf-8") as jsonfile:
#                 json_reader = json.load(jsonfile)
#                 json_length = len(json_reader)
#                 successful = 0
#                 skipped = 0
#                 for mineral in json_reader:
#                     mineral_copy = mineral.copy()
#                     for key, value in mineral_copy.items():
#                         if value == "":
#                             del mineral[key]
#                         else:
#                             newkey = key.replace(' ', '_')
#                             mineral[newkey] = mineral.pop(key)
#                     mineral['name'] = mineral['name'].lower()
#                     try:
#                         with transaction.atomic():
#                             Mineral.objects.create(**mineral)
#                             successful += 1
#                     except IntegrityError:
#                         skipped += 1

#             failed = json_length - (successful + skipped)
#             print("\n")
#             print("\tPopulating database with minerals.json...")
#             print("\tsuccess: ", successful)
#             print("\tskipped: ", skipped,)
#             print("\tfailed: ", failed)
#             print("\n")

#     dependencies = [
#         ('mineralsearchapp', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(populate_db),
#     ]
