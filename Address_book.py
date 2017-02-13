from builtins import str
import operator

#check if it works without object label
class contatto(object):
   
    def __init__(self, *args):
        if len(args) == 0: 
            self.name =         None
            self.surname =      None
            self.phoneNumber =  None
            
        elif len(args) == 1:
            self.name =         args[0]
            self.surname =      None
            self.phoneNumber =  None 
            
        elif len(args) == 2: 
            self.name =         args[0]
            self.surname =      args[1]
            self.phoneNumber =  None
            
        elif len(args) == 3: 
            self.name =         args[0]
            self.surname =      args[1]
            self.phoneNumber =  args[2]   
             
    def toString(self):
        #formatting
        arg = "{0:<20} {3:<8}\n{1:<20} {4:<8}\n{2:<20} {5:<8}\n"
        return arg.format("nome","cognome:","numero telefono:",self.name,self.surname,self.phoneNumber)
    
    #it clears a contact info
    def clear(self):
        self.name =         None
        self.surname =      None
        self.phoneNumber =  None
    
    def createList(self):
        self.lst = []
    
    def addElement(self, name, surname, phoneNumber):
        foo = contatto(name, surname, phoneNumber)
        self.lst.append(foo)
    
    def setElement(self, indx, obj):
        self.lst[indx] = obj
    
    def delElement(self,indx):
        del self.lst[indx-1]

    def printList(self):
        for idx, item in enumerate(self.lst):
            print("contatto n." + str(idx+1))
            print(item.toString())
    
    def getList(self):
        foo = ""
        tmplt = "{}#{}#{}\n"
        
        for item in self.lst:
            foo += tmplt.format(item.name, item.surname, item.phoneNumber)
             
        return foo
    
    def sort(self):
        #sort the list by the "name" attribute
        self.lst.sort(key=operator.attrgetter("name"), reverse=False)
        
    
class main():
    
    IndexErrorMessage = "index out of range or invalid, no contact has been deleted\n"
    #declaring the list
    lst = contatto()
    lst.createList()
    #menu loop
    menu = {}
    menu[1] = "\nAdd a Contact" 
    menu[2] = "Delete a Contact"
    menu[3] = "Show contacts"
    menu[4] = "Sort"
    menu[5] = "Save contacts"
    menu[6] = "Add saved contacts"
    
    while True: 
        options = menu.keys()
        for entry in options: 
            #prints menu option
            print (entry, menu[entry])
    
        selection = input("Please Select:\n>")
         
        #Add Contact
        if selection =='1': 
            name        =   input("Insert the name:\n>")
            surname     =   input("Insert the surname:\n>")
            phoneNumber =   input("Insert the phone number:\n>")
            lst.addElement(name, surname, phoneNumber)
            
        #Delete contact
        elif selection == '2':
            try: 
                idx = input("wich contact to delete?\n>")
                lst.delElement(int(idx))
            except IndexError: print(IndexErrorMessage)                       
            except ValueError: print(IndexErrorMessage)              
            
        #Sort contacts
        elif selection == '3':
            print("printing contacts...\n")
            lst.printList()
            
        #Exit
        elif selection == '4': 
            print("sorting...\n")
            lst.sort()
        
        #saving contacts
        elif selection == '5':
            out_file = open('saved_contacts.txt', 'w')
            out_file.write(lst.getList())
            out_file.close()
         
        elif selection == '6':
            with open('saved_contacts.txt') as fin:
                for line in fin: 
                    items = line.split('#')
                    #add all the elements on the file to the list
                    for idx,item in enumerate(items):
                        if      idx == 0:name        = item                            
                        elif    idx == 1:surname     = item
                        elif    idx == 2:phoenNumber = item
                    lst.addElement(name, surname, phoenNumber)
                
        else: 
            print('Unknown Option Selected!')     
    
#calling main class
if __name__ == '__main__':
    main()
