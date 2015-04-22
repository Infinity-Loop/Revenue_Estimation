class TestDataGenerator:
    def __init__(self):
        print "initing....."
        self.city_dic={}
        self.city_group_dic={}
        self.type_dic={}

        self.city_count=0
        self.city_group_count=0
        self.type_count=0

        self.pre_scane("../data/Origin/train.csv")
        self.pre_scane("../data/Origin/test.csv")

        
    def pre_scane(self,path):#scan both train and test to build a dictionary
        file=open(path)
        for count,line in enumerate(file):
            sp_line=line.split(',')
            if count==0:
                continue    #remove the title
            
            city_name=sp_line[2].decode("utf-8").encode('ascii','ignore')
            city_group=sp_line[3]
            Type=sp_line[4]

            if city_name not in self.city_dic:
                self.city_dic[city_name]=self.city_count
                self.city_count+=1
            if city_group not in self.city_group_dic:
                self.city_group_dic[city_group]=self.city_group_count
                self.city_group_count+=1
            if Type not in self.type_dic:
                self.type_dic[Type]=self.type_count
                self.type_count+=1
    
    def generate_train(self):
        file=open("../data/Origin/train.csv")
        output=open("../data/v0.2/v0.2_train.csv",'w+')
        for count,line in enumerate(file):
            if count==0:
                output.write(line)
                continue
            sp_line=line.split(',')
            time=self.format_time_to_month(sp_line[1])
            city_name=sp_line[2].decode("utf-8").encode('ascii','ignore')
            city_group=sp_line[3]
            Type=sp_line[4]

            city_code=self.city_dic[city_name]
            city_group_code=self.city_group_dic[city_group]
            Type_code=self.type_dic[Type]

            
            output.write(sp_line[0]+',')
            output.write(str(time)+',')
            output.write(str(city_code)+',')
            output.write(str(city_group_code)+',')
            output.write(str(Type_code))
            for item in sp_line[5:]:
                output.write(','+str(item))
    def format_time_to_month(self,time):#compare with 1/1/1995
        if '-' in time:
            cp_time=time.split('-')
            year=cp_time[0]
            month=cp_time[1]
        else:
            cp_time=time.split('/')
            year=cp_time[2]
            month=cp_time[1]
        return (12*(int(year)-1995))+int(month)

    def generate_test(self):
        file=open("../data/Origin/test.csv")
        output=open("../data/v0.2/v0.2_test.csv",'w+')
        for count,line in enumerate(file):
            if count==0:
                output.write(line.rstrip()+",revenue\n")
                continue
            sp_line=line.rstrip().split(',')
            time=self.format_time_to_month(sp_line[1])
            city_name=sp_line[2].decode("utf-8").encode('ascii','ignore')
            city_group=sp_line[3]
            Type=sp_line[4]

            city_code=self.city_dic[city_name]
            city_group_code=self.city_group_dic[city_group]
            Type_code=self.type_dic[Type]
            
            output.write(sp_line[0]+',')
            output.write(str(time)+',')

            output.write(str(city_code)+',')
            output.write(str(city_group_code)+',')
            output.write(str(Type_code))

            for item in sp_line[5:]:
                output.write(','+str(item))
            output.write(",0")
            output.write('\n')




        
    def print_dic(self,dic):
        for item in dic.items():
            print item


if __name__=="__main__":
    tdg=TestDataGenerator()
    tdg.generate_train()
    tdg.generate_test()
