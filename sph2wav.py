import glob
import subprocess
import sox
import os

for filename in glob.glob('*.sph'):
       result = os.path.splitext(filename)[0]
       #print(result)
       new_filename =  result + ".wav"
       #print(new_filename)
       subprocess.run(["sox", filename, new_filename])


