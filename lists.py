schools = ["SDSB", "SSE","SAHSOL","HSS"]
print (schools)
#print index
print (schools[1])
print (schools[1:3]) #from 1 to 3
schools[1]= "SBASSE"
print (schools[1])
schools.insert (4, "SOE")
soe="After SOE"
print (soe)
print (schools)
schools.remove ( "SOE") #for remove dont need the index number
#can also use schools.pop() to remove last one
print("SOE removed")
print (schools)
schools.clear() #clears list
print(schools)
schools2= schools.copy()
#schools.index(school) for school
#schools.sort()
#schools.count(school)
