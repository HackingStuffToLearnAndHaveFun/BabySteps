fn = input ("what's your first name?")
sn = input ("what's your surname?")
em = input ("what's your email?")
tn = input ("what's your telephone number?")
filename = "motherfucker's shit.txt"
file = open(filename , "w")
file.write (fn+"\n")
file.write (sn+"\n")
file.write (em+"\n")
file.write (tn+"\n")
file.close()