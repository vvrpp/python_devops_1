#name='casselyn'
#age=62
#height=6.1
#isIndian=False

#print('name:',, 'age:', age, 'height:', height, 'isIndian:', isIndian)

#input ("what is your name?=")

#print('whar is your name=',input)

#username = input("server name ")
#print ("regester successfully", username)
print("enter the server details")
server_name = str(input("server name "))
IP_address = (input("IP address "))
port_number = int(input("port number "))
print ("server name:", server_name, "IP address:", IP_address, "port number:", port_number)
if server_name == "localhost" and IP_address == 127001 and port_number == 8080:
    print("server is running");

else:
    print("server is not running");

#print("registered successfully")


