import MySQLdb
import numpy
from math import radians, cos, sin, asin, sqrt 
from dijkstra import dijkstra
from salesman import run

db = MySQLdb.connect("localhost","root","123","BIGPJ" )
cursor = db.cursor()
sql = "SELECT * FROM distance"
sql2= "SELECT * FROM connect"
def haversine(lat1,lon1,lat2,lon2): 

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  

    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 
    return c * r 

cursor.execute(sql)
result = cursor.fetchall()
cursor.execute(sql2)
connect = cursor.fetchall()
di=int(sqrt(len(result)))
g={}

f2 = open('./city_list/international_city.txt', 'w')
for i in range(0,di):
	f2.write("\"")
	f2.write(str(result[i][2]))
	f2.write("\"")
	f2.write(",")
f2.close()

f3 = open('./city_list/distance.txt', 'w')
f3.write(str(result))
f3.close()
f4 = open('./city_list/connect.txt', 'w')
f4.write(str(connect))
f4.close()

for i in range(0,di):
    g[i]={}
    for j in range(0,di):
        row=result[i*di+j]
        if i!=j and (connect[i*di+j][4]!=None):
            g[i][j]=haversine(row[4],row[5],row[6],row[7])

D=numpy.zeros((di,di))
B={}
for i in range(0,di):
	A,B[i]=dijkstra(g,i)
	for j in range(0,di):
		D[i][j]=A[j]


route=run(Din=D)
def true_path(A,B):
	for i in (range(len(A))[::-1]):
		while (B[A[i-1]][A[i]] != A[i-1]):
			A.insert(i,B[A[i-1]][A[i]])
	return A
route=true_path(route,B)

f = open('route.txt', 'w')
for i in route:
	f.write("(")
	f.write(str(result[i][6]))
	f.write(",")
	f.write(str(result[i][7]))
	#f.write(",")
	#f.write("\"")
	#f.write(str(result[i][2]))
	#f.write("\"")
	f.write(")")
	f.write(",")
	
f.close()

#f2 = open('international_city.txt', 'w')
#	for i in route:
#		f2.write(str(result[i][2]))
#		f2.write("\n")
db.close()


