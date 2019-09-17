class Student:
    count=0;
    def input_Data(self):
        self.rno=input("ENTER ROLL NO");
        self.name=input("ENTER NAME:");
        self.c_marks=int(input("ENTER C MARKS"));
        self.cpp_marks=int(input("ENTER CPP MARKS"));
        self.python_marks=int(input("ENTER PYTHON MARKS"));
        Student.count=Student.count+1;
    def cal_total(self):
        self.total=self.c_marks+self.cpp_marks+self.python_marks;
    def cal_per(self):
        self.per=(self.total*100)/300;
    def cal_greade(self):
        if(self.per<99 and self.per>=70):
            self.greade='A';
        elif(self.per<70 and self.per>=60):
            self.greade='B';
        elif(self.per<60 and self.per>=50):
            self.greade='C';
        elif(self.per<50):
            self.greade='D';
    def show(self):
        print("ROLL NUMBER IS:",self.rno);
        print("NAME IS:",self.name);
        print("NAME IS:",self.c_marks);
        print("NAME IS:",self.cpp_marks);
        print("NAME IS:",self.python_marks);
        print("NAME IS:",self.total);
        print("NAME IS:",self.per);
        print("NAME IS:",self.greade);
    @staticmethod
    def showcount():
        print("NUMBER OF OBJECT CREATE:",Student.count);
s1=Student();
s1.input_Data();
s1.cal_total();
s1.cal_per();
s1.cal_greade();
s1.show();


s2=Student();
s2.input_Data();
s2.cal_total();
s2.cal_per();
s2.cal_greade();
s2.show();

s3=Student();
s3.input_Data();
s3.cal_total();
s3.cal_per();
s3.cal_greade();
s3.show();

Student.showcount();

