# ADD the following to BLOCK 1
from datetime import datetime

'''
In BLOCK 3 replace the line 
text_tag.attrib["date"] = metadata_file["upload_date"]
with the following ones
'''
date = datetime.strptime(metadata_file["upload_date"], "%Y%m%d")
text_tag.attrib["date_d"] = str(date.day)
text_tag.attrib["date_m"] = str(date.month)
text_tag.attrib["date_y"] = str(date.year)
text_tag.attrib["date_ts"] = str(int(date.timestamp()))