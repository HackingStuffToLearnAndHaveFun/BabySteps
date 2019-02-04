file=open("details.txt","r")
content=file.readlines()
id=input("what's your id?")
if content[0].strip()==id:
    print ("user's id:", content[0], "name: ", content[1],"surname: " , content[2],"email:",content[3],"phone number:", content[4])
else:
    print("wrong user's id")