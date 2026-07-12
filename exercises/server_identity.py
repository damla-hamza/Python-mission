server1 = {"name": "web-01"}
server2 = server1
server3 = {"name": "web-01"}

print(server1 == server2)
print(server1 is server2)

print(server1 == server3)
print(server1 is server3)