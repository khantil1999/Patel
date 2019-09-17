def palindrom_number(data):
    data1=data[::-1];
    if(data==data1):
        print("PALINDROM");
    else:
        print("NOT PALINDROM");
def join_string(data1,data2):
    print("STRING IS:",data1+data2);
def compare_string(data1,data2):
    if(data1==data2):
        print("BOTH ARE SAME");
    else:
        print("NOT SAME");
def getInput():
    data=(input("ENTER DATA:"));
    return data;
def check_sentence(data,val):
    if data in val:
        print("FIND VALUE:",val);
    else:
        print("SORRY NO MATCH FOUND");
def menuFunction():
    while(1):
        print("1.length");
        print("2.join string");
        print("3.compare string");
        print("4.reverse");
        print("5.palindrom or not");
        print("6.check sentance");
        print("ENTER YOUR CHOICE");
        
        ch=int(input("ENTER CHOICE:"));
        if(ch==1):
            lst=getInput();
            print(len(lst));
        elif(ch==2):
            lst=getInput();
            lst1=getInput();
            join_string(lst,lst1);
        elif(ch==3):
            lst=getInput();
            lst1=getInput();
            compare_string(lst,lst1);
        elif(ch==4):
            lst=getInput();
            print(lst[::-1]);
        elif(ch==5):
            lst=getInput();
            palindrom_number(lst);
        elif(ch==6):
            lst=getInput();
            val=input("ENTER STRING:");
            check_sentence(lst);
            
        else:
            break;

menuFunction();            
        
        
