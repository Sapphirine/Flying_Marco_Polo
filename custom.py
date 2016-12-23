import MySQLdb
import numpy
from math import radians, cos, sin, asin, sqrt 
from dijkstra import dijkstra
from salesman import run


def haversine(lat1,lon1,lat2,lon2): 

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  

    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 
    return c * r 

def custom_route(city_list='Beijing,New York,Paris,Delhi'):
	capital=["Abidjan","Abu Dhabi","Abuja","Accra","Addis Ababa","Amman","Amsterdam","Antananarivo","Asmara","Asuncion","Athens","Auckland","Baghdad","Bahrain","Baku","Bamako","Bandar Seri Begawan","Bangkok","Bangui","Beijing","Beirut","Belgrade","Berlin","Bern","Bishkek","Bogota","Bratislava","Bridgetown","Brussels","Bucharest","Budapest","Buenos Aires","Bujumbura","Cairo","Caracas","Castries","Cayenne","Chisinau","Conakry","Copenhagen","Dakar","Dar Es Salaam","Delhi","Dhaka","Dili","Djibouti","Doha","Dushanbe","Freetown","Georgetown","Hanoi","Harare","Havana","Helsinki","Honiara","Islamabad","Istanbul","Jakarta","Johannesburg","Juba","Kabul","Kathmandu","Keflavik","Khartoum","Kiev","Kigali","Kingston","Kuala Lumpur","Kuwait","Libreville","Lilongwe","Lima","Lisbon","Ljubljana","Lome","London","Luanda","Lusaka","Madrid","Malabo","Male","Managua","Manila","Maputo","Mexico City","Mogadishu","Monrovia","Montevideo","Moroni","Moscow","Muscat","N'djamena","Nairobi","Nassau","New York","Niamey","Nice","Nicosia","Oslo","Ottawa","Ouagadougou","Panama City","Paris","Phnom-penh","Podgorica","Port Moresby","Port-au-prince","Prague","Quito","Rabat","Riga","Rio De Janeiro","Riyadh","Rome","San Jose","San Juan","San Salvador","Santiago","Santo Domingo","Sao Tome","Sarajevo","Seoul","Singapore","Sofia","Stockholm","Sydney","Taipei","Tashkent","Tbilisi","Tegucigalpa","Tehran","Thimphu","Tirana","Tokyo","Tripoli","Tunis","Vienna","Vientiane","Vilnius","Warsaw","Yaounde","Yerevan","Zagreb"]
	

	db = MySQLdb.connect("localhost","root","123","BIGPJ" )
	cursor = db.cursor()
	sql1 = "SELECT * FROM distance"
	sql2= "SELECT * FROM connect"
	cursor.execute(sql1)
	result = cursor.fetchall()
	cursor.execute(sql2)
	connect = cursor.fetchall()
	di=int(sqrt(len(result)))
	db.close()

	city_list=city_list.split(',')

	
	dic=len(city_list)
	city_list_index=numpy.zeros(dic)-1
	for i in range(0,dic):
		for j in range(0,di):
			if city_list[i]==capital[j]:
				city_list_index[int(i)]=int(j)
	
	for i in range(0,dic):
		if city_list_index[i]==-1:
			return [],[],"Sorry, you might input an imaginal city %s" % (city_list[i])

	g={}
	for i in city_list_index:
		g[int(i)]={}
		for j in city_list_index:
			row=result[int(i*di+j)]
			if i!=j and (connect[int(i*di+j)][4]!=None):
				g[int(i)][int(j)]=haversine(row[4],row[5],row[6],row[7])
	D={}
	B={}
	for i in city_list_index:
		A,B[int(i)]=dijkstra(g,int(i))
		D[int(i)]={}
		for j in city_list_index:
			D[int(i)][int(j)]=A[int(j)]
	
	
	route=run(Din=D)
	print("lalalal")
	def true_path(A,B):
		for i in (range(len(A))[::-1]):
			while (B[A[i-1]][A[i]] != A[i-1]):
				A.insert(i,B[A[i-1]][A[i]])
		return A
	route=true_path(route,B)
	path=[]
	pathmarker=[]
	output=[]
	for i in route:
		i_=i
	
		path.append((result[i_][6],result[i_][7]))
		pathmarker.append((result[i_][6],result[i_][7],result[i_][2]))
		output.append(result[i_][2])
	path.append((result[route[0]][6],result[route[0]][7]))
	return path,pathmarker,output
		
#path,pathmarker,output=custom_route()

		

