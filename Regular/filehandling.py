import datetime
import linecache

def refreshfile(x,a):
    f=open("myfile.txt","r")
    line=f.readlines()
    f.close()
    #print(line,type(line))
    f=open("myfile.txt","w")
    for i in range(a):
        if i!=int(x):
            f.writelines(line[i])
    f.close()
def filecheck(x):
    f=open("myfile.txt","r")
    a=0
    for n in f:
        a+=1
    print("Total : ",a)
    for i in range(1,a):
        line = list((linecache.getline("myfile.txt", i)).split())
        #print(line)
        if line[0]==x:
            new=linecache.getline("myfile.txt", i)
            o=open("final.txt","a")
            t=str(datetime.datetime.now())
            new = new.strip() +" - "+ t
            o.write('{}\n'.format(new))
            o.close()
            print(new)
            refreshfile(i,a)
            return 1
        elif i==99:
            return 0
    f.close()

def firstentry(x):
    f=open("myfile.txt","a")
    t = " @ " + str(datetime.datetime.now())
    t = x + t
    f.write('{}\n'.format(t))
    f.close()


for i in range(50):
    reg=input("Enter your Reg no : ")
    if i==49:
        print("Maximum login limit exceed")
        exit(0)
    if filecheck(reg) :
        print("Logged out succefully")
    else :
        firstentry(reg)
        print("Logged in succefull")
