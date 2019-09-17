class Account:
    interest_rate=7.6;
    def set(self):
        self.ac_no=input("ENTER ACCOUNT NUMBER:");
        self.ac_name=input("ENTER NAME:");
        self.ac_balance=int(input("ENTER BALANCE:"));
    
    def deposit(self):
        self.amount=int(input("ENTER AMOUNT:"));
        self.ac_balance=self.ac_balance+self.amount;
        print("AFTER DEPOSIT:",self.ac_balance);
    def withdraw(self):
        self.amount=int(input("ENTER AMOUNT:"));
        self.ac_balance=self.ac_balance-self.amount;
        print("AFTER DEPOSIT:",self.ac_balance);        
    def cal_interest(self):
        self.years=int(input("ENTER YEARS:"));
        self.interest=(self.ac_balance*Account.interest_rate*self.years)/100
        print("INTEREST IS:",self.interest)
    def show(self):
        print("ACCOUNT NUMBER IS:",self.ac_no);
        print("NAME IS:",self.ac_name);
        print("BALANCE:",self.ac_balance);

    def menu(self):
         while(1):
            print("1.ENTER DATA");
            print("2.DEPOSIT");
            print("3.WITHDRAW");
            print("4.CALCULATE INTEREST");
            print("5.SHOW DATA");
            print("ENTER YOUR CHOICE");
            ch=int(input("ENTER CHOICE:"));
            if(ch==1):
                self.set();
            elif(ch==2):
                self.deposit();
            elif(ch==3):
                self.withdraw();
            elif(ch==4):
                self.cal_interest();
            elif(ch==5):
                self.show();
            else:
                break;
                
        
a1=Account();

a1.menu();
