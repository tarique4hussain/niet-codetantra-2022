import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def getProductSign(a, b):
	if a>0 and b>0: return 'positive'
	if a<=0<=b:
		return 'zero'
	negatives = a-b+1
	if negatives%2==0:
		return'positive'
	return 'negative'

print(getProductSign(a, b))
