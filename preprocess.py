import math as m
def preprocess(ans1):

    #print(ans1.strip().split(" "))
    special_character=['X',"+","-","div","="]
    variable=["y","z","e"]
    numbers=[str(i) for i in range(0,10)]
    math=["log","sin","cos","tan"]
    ans=ans1.strip().split(" ")
    result=""
    i=0
    k=0
    num=""
    while i < len(ans):
        #print(ans[i])
        if ans[i] in special_character:
            result=result+ans[i]
            i=i+1
    
        elif ans[i] in variable:
            if (i+1)<len(ans):
                if ans[i+1] in numbers:
                        #print(ans[i]+"^"+ans[i+1])
                        result=result+ans[i]+"**"+ans[i+1]
                        i=i+2
                else:
                        result=result+ans[i]
                        i=i+1
            else:
                result=result+ans[i]
                i=i+1
            
        elif ans[i] in numbers:
            if (i+1)<len(ans):
                if ans[i+1] in variable:
                    result=result+ans[i]+"*"
                    i=i+1
                else:
                    result=result+ans[i]
                    i=i+1
            else:
                result=result+ans[i]
                i=i+1
   
        elif ans[i] in math:
            num=""
            print(ans[i])
            k=0
            for j in ans[i+1:]:
                k=k+1
                if j in numbers:
                    num=num+j
                else:
                    break
            print(num)
            if ans[i]=="log":
                result=result+str(m.log10(int(num)))
            elif ans[i]=="sin":
                result=result+str(m.sin(int(num)))
            elif ans[i]=="cos":
                result=result+str(m.cos(int(num)))
            elif ans[i]=="tan":
                result=result+str(m.tan(int(num)))
            i=i+k
    print(result)
    return(result)

