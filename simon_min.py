from time import*
s=''
def e(u=0):print(u or"\x1B[H\x1B[J");sleep(1)
while 1:
	s+='rgby'[int(time())%4];e()
	for c in s:e(c);e()
	for c in s:c==input()or quit()
