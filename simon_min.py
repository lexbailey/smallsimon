from time import*
s=''
def e(u):print(u or"\x1B[H\x1B[J");sleep(1)
while 1:
	s+='rgby'[int(time())%4];e(0)
	for c in s:e(e(c))
	for c in s:c!=input()<quit()
