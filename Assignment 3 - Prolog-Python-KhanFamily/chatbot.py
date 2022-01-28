
from flask import Flask, app, render_template, request, jsonify
import json
from pyswip import Prolog
prolog=Prolog()
prolog.consult("khan_family.pl")


# def Swi_prolog(choice='', member=''):
#     if choice != '' and member != '':
#         if(choice=='1'):
            # answer=[]
            # Y=member
            # Y=Y.lower()
            # # val=prolog.query("baap(X,"+Y+")")
            # # print(val)
            # for val in prolog.query("baap(X,"+Y+")"):
            #     print(val)
            #     print(val["X"])
            #     answer.append(val["X"])
            #     break
            # return answer



def display_khanFamily():
    print("#########################################################################################")
    print("*\n*Please Select Any choice/Alphabet Below In Order To Find Relationship!*\n")
    print("*Enter 1 for Baap", "Enter 2 for Maa",sep="________*")
    print("*Enter 3 for Beti", "Enter 4 for Beta", sep="________*")
    print("*Enter 5 for Dada", "Enter 6 for Nana", sep="________*")
    print("*Enter 7 for Dadi", "Enter 8 for Nani", sep="________*")
    print("*Enter 9 for Sala", "Enter 'a' for Bahu", sep="________*")
    print("*Enter 'b' for Pota", "Enter 'c' for Poti", sep="______*")
    print("*Enter 'd' for Nawasa", "Enter 'e' for Nawasi", sep="________*")
    print("*Enter 'f' for husband side sussar", "Enter 'g' for wife side sussar*", sep="________*")
    print("*Enter 'h' for bapdada", "Enter 'i' for khala", sep="___________*")
    print("*Enter 'j' for chachataya", "Enter 0 for Exit*\n**", sep="________*")
    print("#########################################################################################")

def khanFamilyMembers():
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("\n* Select Any Member of Khan Family: \n*")
    print("ChoteKhan,   ChotiRani,  BarreKhan,  BarriRani")
    print("Salim,       Kausar,     Nadir,      Asad")
    print("Nahid,       Sumra,      Rizwan,     Burhan")
    print("Rashid,      Akram,      Salima,     Sanam,")
    print("Rabia")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")


# 2 in 1 means two user interfaces one is terminal and the other is web interface
def main():
    print("\n***--- (: WELLCOME TO 2 in 1 Chatbot OF KHAN FAMILY :)---***\n")
    choice = None 
    found = False
    answer = []
    display_khanFamily()    
    valid_choices = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j"}
    choice=input("\n---> Enter your Choice for the Relationship that you are interested in <---\n")
    if choice in valid_choices:
        choice = str(choice)
    else:
        print("\n--->Invalid Choice :( ")

    if(choice=='1'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Baap is required : ")
        Y=Y.lower()
        for val in prolog.query("baap(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the baap of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer,Y
    
    if(choice=='2'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Maa is required : ")
        Y=Y.lower()
        for val in prolog.query("maa(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the maa of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='3'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Beti is required : ")
        Y=Y.lower()
        for val in prolog.query("beti(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the beti of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='4'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Beta is required : ")
        Y=Y.lower()
        for val in prolog.query("beta(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the beta of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='5'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Dada is required : ")
        Y=Y.lower()
        for val in prolog.query("dada(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the dada of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='6'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Nana is required : ")
        Y=Y.lower()
        for val in prolog.query("nana(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the nana of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='7'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Dadi is required : ")
        Y=Y.lower()
        for val in prolog.query("dadi(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the dadi of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='8'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Nani is required : ")
        Y=Y.lower()
        for val in prolog.query("nani(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the nani of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='9'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Sala is required : ")
        Y=Y.lower()
        for val in prolog.query("sala(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the sala of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='a'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Bahu is required : ")
        Y=Y.lower()
        for val in prolog.query("bahu(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the bahu of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='b'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Pota is required : ")
        Y=Y.lower()
        for val in prolog.query("pota(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the pota of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='c'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Poti is required : ")
        Y=Y.lower()
        for val in prolog.query("poti(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the poti of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='d'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Nawasa is required : ")
        Y=Y.lower()
        for val in prolog.query("nawasa(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the nawasa of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='e'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Nawasi is required : ")
        Y=Y.lower()
        for val in prolog.query("nawasi(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the nawasi of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='f'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Husband Sussar is required : ")
        Y=Y.lower()
        for val in prolog.query("sussar_h(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the sussar of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='g'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Wife Sussar is required : ")
        Y=Y.lower()
        for val in prolog.query("sussar_w(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the sussar of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='h'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Bapdada is required : ")
        Y=Y.lower()
        for val in prolog.query("bapdada(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the bapdada of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer

    if(choice=='i'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Khala is required : ")
        Y=Y.lower()
        for val in prolog.query("khala(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mrs.{0} is the khala of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer
    if(choice=='j'):
        khanFamilyMembers()
        Y=input("Enter name of person whose Chachataya is required : ")
        Y=Y.lower()
        for val in prolog.query("chachataya(X,"+Y+")"):
            answer.append(val["X"])
            found=True
            print("\n==========================================================")
            print("Mr.{0} is the chachataya of {1}.".format(val["X"], Y))
            print("============================================================")
        if found == False:
            print("\n============================================================")
            print("Relationship does't Found.")
            print("============================================================")
            exit()
        return answer
    if(choice=='0'):
        exit()


if __name__=="__main__":
    result, Mem=main()

# From here the Flask web interface started
print('\n','\n')
print('***************\n',"Click the below link, It will take you to Web Interface",'\n***************\n')
print('***************\n',"Please Select The Choices as Select In Terminal It Will Give You Correct Answer",'\n***************\n')
app = Flask(__name__)       
userData=[]
def receivedData(form): 
    for key in form.keys():
        data=key 
    userInfo=json.loads(data)
    userData.append(userInfo)
    return userData


# Main Page Route
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route("/processUserInfo",methods=['POST'])

def processUserInfo():
    rf=request.form
    recData=receivedData(rf)
    recData=[x.strip() for x in recData if x.strip()]
    # ans='Invalid Entry, Please Select The same member As Select In Terminal'
    # resp_dic={'sum':ans}
    # response = jsonify(resp_dic)
    if len(recData) >= 2:
        print('yes')
        relationship=recData[0]
        member=recData[1]
    # if member == Mem:
    resp_dic={'sum':result}
    response = jsonify(resp_dic)
            # return resp
        # print(Swi_prolog(recData[0],recData[1]))
    # num=['abc','eee']
    # print(response[1])
        # resp.headers['Access-Control-Allow-Origin']='*'
    return response



if __name__ == '__main__':
    app.run()

print("\n\n===================> Thank You for Coming :) <=====================\n")

