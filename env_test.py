'''check what version of python used'''

'''while True:
    try:
        print "Hello World, using python 2"
    break
    except:
        print("Hello World, using python 3")
    '''

def add_did(start, finish):
	did = start - 1
	dids = []

	for i in range(start, finish + 1):
		did = did + 1
		dids.append(did)
	return dids

# test the function
setlist = add_did(100, 200)
for set in setlist:
	print set