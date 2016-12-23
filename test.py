#this is a test
from custom import custom_route
from save_route import r_path1,r_path2,r_path3

def citylist(choice,citylist=''):
 	
 	if choice == '1':
		return r_path1()
 	elif choice == '2':
		return r_path2()
	elif choice == '3':
		return r_path3() 
	elif choice == '4':
		return custom_route(citylist)

