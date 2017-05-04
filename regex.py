import re
text = 'hi,I am Shirley Hilton.I am his wife.'
m = re.findall(r'\bhi\b',text)
if m:
	print m
else:
	print 'not match'
