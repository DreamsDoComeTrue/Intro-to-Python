class Employee:
    def __init__(self, name="", idnum="", dept=" ", jobtitle=" "):
        self.__name = name
        self.__idnum = idnum
        self.__dept = dept
        self.__jobtitle = jobtitle


    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setIdnum(self, idnum):  # @Name.setter used instead of set method
        self.__idnum = idnum

    def getIdnum(self):
        return self.__idnum

    def setDept(self, dept):
        self.__dept = dept

    def getDept(self):
        return self.__dept

    def setJobTitle(self, jobtitle):
        self.__jobtitle = jobtitle

    def getJobTitle(self):
        return self.__jobtitle

def main():
    name = input('Enter name: ')
    idnum = input('Enter ID number: ')
    dept = input('Enter department: ')
    jobtitle = input('Enter Job Title: ')
    emp = Employee(name, idnum, dept, jobtitle)
    print('Employee Name: '+emp.getName()+'ID NUmber: '+emp.getIdnum()+'Department: '+emp.getDept()+'Job Title: '+emp.getJobTitle())
if __name__ == "__main__":
    main()