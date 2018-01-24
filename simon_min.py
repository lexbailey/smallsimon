from time import*
l=sleep;s=''
def e():print("\x1B[H\x1B[J")
while 1:
	s+="rgby"[int(time()*9)%4];e()
	for c in s:print(c);l(1);e();l(1)
	for c in s:c==input()or quit()
