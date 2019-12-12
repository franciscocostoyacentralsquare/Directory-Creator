import os

#print("WARNING: Folder creation will only work when connected to the server. \n If you are out of the office, make sure you are connected via VPN\n\n")

def repeat():
    question = input("Press ENTER key to end the program, or NEW if you need to make another jurisdiction\n")
    repeat = question.casefold
    global x
    if repeat == 'new':
        pass
    else:
        x = False

def pullJD(self):
    jd = self.inputJurisdictionName.get()
    print(f"got the name: {jd}.")
    return jd

def makeCWDirectory(self, jurisdiction, counter, title):
    x = counter
    numberation = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        #os.mkdir(f'\\\\psc-app03\\OutsourceDocuments\\JurisdictionFolders\\Lake Mary Team\\{jurisdiction}')
    try:
        os.mkdir(f'\\\\psc-app03\\OutsourceDocuments\\JurisdictionFolders\\Lake Mary Team\\{jurisdiction}\\')

        for count in range(0, counter):
            n = numberation[count]
            t = title[count]
            #os.mkdir(f'\\\\psc-app03\\OutsourceDocuments\\JurisdictionFolders\\Lake Mary Team\\{jurisdiction}\\{number} {title}')
            os.mkdir(f'\\\\psc-app03\\OutsourceDocuments\\JurisdictionFolders\\Lake Mary Team\\{jurisdiction}\\{n} {t}')
            x += 1
    except FileExistsError:
        self.result.set("Directory already exist. Files not created")
    else:
        rtt = os.path.isdir(f'\\\\psc-app03\\OutsourceDocuments\\JurisdictionFolders\\Lake Mary Team\\{jurisdiction}')

        return rtt









#x = True
#while x == True:
#    makeCWDirectory()
#    repeat()
##
#Payments
#Appeals
#Bank Reconciliations
#End Of Month Reports
#Refunds
#Collections
#Spreadsheets
#Returned Checks
#Registration Forms
#Misc
