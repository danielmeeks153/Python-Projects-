import shutill
import os

source = 'C:\Users\Daniel\Desktop\SaveFile'

destination = 'C:\Users\Daniel\Desktop\DestinationFile'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)

    
