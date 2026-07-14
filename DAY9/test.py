# Folder Name = Logs

# Agar Logs folder nahi hai:
#     create karo
#     print "Logs folder created"

# Agar Logs folder hai:
#     print "Logs folder already exists"

import os

path="D:/2026D/Python/2026oython/DAY9"

if not os.path.exists(f"{path}/logs"):
        print("creating logs folder")
        try:
            os.mkdir(f"{path}/logs")
            print("file created successfully")
        except:

            print("folder exist already")
else:
     print("folder exist already") 