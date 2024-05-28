# #!/usr/bin/env python
filepath = "/home/garvika40/Desktop/aws.txt"
with open(filepath, 'r') as f:
    content = f.read()

print(content)


infile = open(filepath,'r')
data = infile.read()
infile.close()
print(data)

#Date and Time Python
import time
timenow=time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(day)+'/'+str(month)+'/'+str(year)+'/'+str(hour)+'/'+str(minute))
a=time.time()
for i in range(3):
    time.sleep(2)
    print(2)
b=time.time()
print(b-a)


#Try and Except
filepath = "/home/garvika40/Desktop/aws1.txt"
try:
    with open(filepath) as f:
        df=f.read()
    print(f)
except FileNotFoundError:
#except Exception:
#-----handle exception(we can have multiple exceptions)
    print("See if the file exists")
#Benifit of using try and except is that - without it the programe would never implement whats in the later part of the script before the error was raised.
print("even with an error we could implement later part of script")

#try finally
#finally clause is always executed
#else part is printed only when no exception is raised 
#raise - we can force an exception to occur even if it doesnt occur
filepath = "/home/garvika40/Desktop/aws.txt"
try:
    with open(filepath) as f:
        df=f.read()
    print(df)
except FileNotFoundError:
    print("No such file exists in the given path")
else:
    print("No exception occured")
finally:
    f.close()
    print("File closed")
raise ValueError("Wrong value")


#User defined exceptions
class LunchError(Exception):
    pass


avail=input('Is programmer available? ', )
print(avail)
if avail == 'Yes':
    print('ok')
else:
    raise LunchError("Programmer went to lunch")

#---DONE---