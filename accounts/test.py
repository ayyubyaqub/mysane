
def rotationAssignment(name,numofrotations):
    for i in range(numofrotations):
        temp=name[len(name)-1]+name[0:len(name)-1]
        name=temp
    return name


name=str(input('Enter the string ')) 
iterations= int(input('Enter the iterations ')) 
output=rotationAssignment(name,iterations)
print('your output is  '+str(output))


