def fname(i,array=[]):
    print(array[i],end="      ")
    return
def fsum(a,b,c):
    return a+b+c
def favg(x):
    return round(x/3,1)
def fgrade(x):
    if(x>=95):
        print('A+',end="     ")
    elif(x>=90):
        print('A',end="      ")
    elif(x>=85):
        print('B+',end="     ")
    elif(x>=80):
        print('B',end="      ")
    elif (x>=75):
        print('C+',end="     ")
    elif (x>=70):
        print("C",end="      ")
    elif (x>=60):
        print("D",end="      ")
    else:
        print("F",end="      ")
        return
def frank(k):
    print(k)
    return
def main():
    student_id=[0]*5
    name=[""]*5
    englishscore=[0]*5
    c_score=[0]*5
    python_score=[0]*5
    sums=[0]*5
    ranks=[]
    for i in range(0,5):
        student_id[i]=int(input("please student number: "))
        name[i]=input("please name: ")
        englishscore[i]=int(input("please english score: "))
        c_score[i]=int(input("please c score: "))
        python_score[i]=int(input("please python score: "))
    for i in range(0,5):
        sums[i]=c_score[i]+python_score[i]+englishscore[i]
    sorted_sums=sorted(sums,reverse=True)
    for i in range(0,5):
        rank=sorted_sums.index(sums[i])+1
        ranks.append(rank)
    print("          program of manage grade           ")
    print("=======================================================================================")
    print("student number       name     english   c_language   python   sum    avg   grade    rank")
    print("=======================================================================================")
    for i in range(0,5):
        print(student_id[i],end="        ")
        fname(i,name)
        print(f"{englishscore[i]}      {c_score[i]}      {python_score[i]}",end="        ")
        x=fsum(englishscore[i],c_score[i],python_score[i])
        print(x,end="      ")
        y=favg(x)
        print(y,end="       ")
        fgrade(y)
        z=frank(ranks[i])
main()

    
