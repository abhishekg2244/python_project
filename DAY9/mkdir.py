import os


try:
    file_paath=os.path.exists(" D:/2026D/Python/2026oython/DAY9/nya_folder")
    if file_paath == False:
        os.mkdir("nya_folder")
        print("file created successfully")

except:
    print("file pahle se hi bahi, coming from except")

else:
    print("file exist bro , coming for else")

finally:
    print("program shi hai  bha")




