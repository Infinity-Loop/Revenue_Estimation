
if __name__=="__main__":
    file=open("../Submission/new_submission.csv")
    output=open("../Submission/my_sub.csv",'w+')
    for counter,line in enumerate(file):
        if counter==0:
            output.write(line)
            continue
        cp_line=line.split(',')
        id=cp_line[0]
        pre=cp_line[1]
        output.write(str(int(id)-1)+','+pre)
        
