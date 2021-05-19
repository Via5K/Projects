#Removing the duplicate files from 2 folder.
import os
Copy1Path = r".\Copy1"
Copy2Path = r".\Copy2"
Path2, Path1 = [] , []
Path1 = os.listdir(Copy1Path)
Path2 = os.listdir(Copy2Path)
print(Path1,Path2)
for item1 in Path1:
	for item2 in Path2:
		if item1==item2:
			removalName = os.path.join(Copy1Path,item1)
			os.remove(removalName)
			
print("Work Done\nThe Files With Same Name has been Removed..."	)