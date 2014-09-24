import time
from PyAppLock import *

def checklock():
	if Lock().isPresent():
		print "is running"
	else:
		print "Not running, Starting"
		main()


def main():
	print "Before"
	time.sleep( 15 )
	print "After"

if __name__ == '__main__':
	#checklock()
	if Lock().isPresent():exit(1)
	else:main()
		
