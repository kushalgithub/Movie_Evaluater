fo=open("test.txt","a")


go=open("reduced_guardians of the galaxy vol. 2.txt","r")
golines=go.readlines()
temp=[]
for i in range(len(golines)):
    fo.write(golines[i].strip()[11:-2] + " ")
go.close()
fo.write("\n")

go=open("reduced_Baywatch.txt","r")
golines=go.readlines()
temp=[]
for i in range(len(golines)):
    fo.write(golines[i].strip()[11:-2] + " ")
go.close()
fo.write("\n")

go=open("reduced_the boss baby.txt","r")
golines=go.readlines()
temp=[]
for i in range(len(golines)):
    fo.write(golines[i].strip()[11:-2] + " ")
go.close()
fo.write("\n")

go=open("reduced_Bahubali2.txt","r")
golines=go.readlines()
temp=[]
for i in range(len(golines)):
    fo.write(golines[i].strip()[11:-2] + " ")
go.close()
fo.write("\n")

go=open("reduced_King Arthur.txt","r")
golines=go.readlines()
temp=[]
for i in range(len(golines)):
    fo.write(golines[i].strip()[11:-2] + " ")
go.close()
fo.write("\n")
