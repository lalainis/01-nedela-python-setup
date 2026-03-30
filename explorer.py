# virkņu savienošana
print ("5"+"3")
# print ("5"+3)
print (int("5")+3)
#Robežgadījumi
#print (int("abc")) - tāpēc ka "abc" nav skaitlis, un nevar tikt pārveidots par skaitli.
print (float("3.14"))
#truthy/Falsy vērtības
print (bool(""))
print (bool(" "))
print (bool("0"))
print (bool(0))
print (bool([]))
print (bool(None))
print (True + True)
#jauktā aritmētika
print (True * 10)
print (False + 5)
print (10 / True)
#skaitļu pārveidošana
print (int(3.86))
#print (int("3.14")) - tāpēc ka pēdiņas ir virkne un nevar tikt pārveidota par skaitli, un arī tāpēc ka "3.14" nav vesels skaitlis.
print (int(float("3.14")))
print (float("1e3"))
#citi interesanti gadījumi
print (0.1 + 0.2 == 0.3)
print (round(2.5))
print (round(3.5))  