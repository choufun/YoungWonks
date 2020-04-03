'''

1. Install MongoDB Enterprise Server 4.2.5
   https://www.mongodb.com/download-center/enterprise

   MongoDB Compass installed as well
   
2. pip3 install pymongo

3. Add MongoDB server to PATH
   Control Panel\System and Security\System
   Advance system settings
   Environment Variables
   User variables: Path
   Add C:\Program Files\MongoDB\Server\4.2\bin

4. MongoDB Server should be running

5. Enter MongoDB with mongo command

'''

import pymongo
from pprint import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

pprint(dir(client), indent=4)
print(client.server_info)
