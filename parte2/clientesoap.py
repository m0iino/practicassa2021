from suds.client import Client

client = Client("http://www.dneonline.com/calculator.asmx?WSDL")

#metodo suma
print("Add(1,2)")
response = client.service.Add(1,2)
print("suma: ",response)
# metodo division 
print("Divide(6,2)")
response = client.service.Divide(6,2)
print("division: ",response)

# metodo multiplicasion
print("Multiply(4,2)")
response = client.service.Multiply(4,2)
print("multiplicasion: ",response)

# metodo resta
print("Subtract(8,2)")
response = client.service.Subtract(8,2)
print("resta: ",response)
