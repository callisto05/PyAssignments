import json
import re
from typing import Pattern

pattern_major = re.compile("[0-9]+\.[0-9]+\.[0-9]+")
pattern_minor = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
# match = pattern1.finditer()

# using context manager
with open('C:/Users/prathamesh.bhosale/Desktop/Py/Packages.json') as packages_json:
# returns dictionary with objects
  package_dict = json.load(packages_json)

# print("URL: " +data[0]["artifact_url"]["full"]+" | "+data[0]["package_case"] )
  dictLen = len(package_dict)

  for x in range(dictLen):
      url = package_dict[x]["artifact_url"]["full"]
      pack_ver = package_dict[x]["package_case"]
      major_version = re.findall(pattern_major, url)
      minor_version = re.findall(pattern_minor, url)

      if(pack_ver != ""):
          print("URL: " +url+" | "+pack_ver +" | "+ major_version[0]+" | "+ minor_version[0][-3:])
      else:
          print("URL: " +url+" | "+ "   NA    " +" | "+ major_version[0]+" | "+ minor_version[0][-3:])    
      