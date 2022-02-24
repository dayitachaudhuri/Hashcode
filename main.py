myfile=open("a_an_example.in.txt", 'r+')

outputFile=("outputLOL.txt", 'a+')

contents=myfile.readlines()

n,m=map(int,contents.pop(0).split())

contributors={}
projects={}

for i in range(n):
    name,noSkills=contents.pop(0).split()
    noSkills=int(noSkills)
    skillsList=[]
    for j in range(noSkills):
        skill,level=contents.pop(0).split()
        level=int(level)
        skillsList.append([skill,level])
    contributors[name]=skillsList

for i in range(m):
    name,days,points,bestBefore,contri=contents.pop(0).split()
    days=int(days)
    points=int(points)
    bestBefore=int(bestBefore)
    contri=int(contri)
    skillsList=[days,points,bestBefore,contri]
    for j in range(contri):
        skill,level=contents.pop(0).split()
        level=int(level)
        skillsList.append([skill,level])
    projects[name]=skillsList

print(contributors)
print(projects)
'''
print(n)
print(m)'''