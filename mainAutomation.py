import os,sys
import win32print
import pprint
import magic
import jinja2,pdfkit

def findAvailablePrinters():
    #availablePrinters.insert(0,"testElement")
    availablePrinters=win32print.EnumPrinters(win32print.PRINTER_ENUM_NAME, None, 5)
    return availablePrinters



def directoryListing(path,printers=""):
    documents=[]
    
    for item in os.listdir(path):
        documents.append({item:magic.from_file(item)})
    return documents
##########################################################
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f)

def createAndReadTXTfile(dirContents):
    fd = open("output.txt", "r+", encoding = "utf-8")
    for item in dirContents:
        for key in item:
            print(key,item[key])
        
            fd.write("- "+ key+ ", File Type: "+item[key] +"\n")
        
    #input_string = fd.read()
   # multi_line_string = input_string.splitlines()
   # return multi_line_string
#def deleteTXTfile(file_name):

    
#################################################
def sendDocumentToPrinter(printer_name, pdf_path):
    printer_handle = win32print.OpenPrinter(printer_name)
    
    try:
        print("1")
        
    except Exception as e:
        print("Exception occured:", e)
        
    finally:
        win32print.ClosePrinter(printer_handle)
        pdf_file.close()

if __name__=="__main__":
    selectorList=dict()
    pathToPrint=str(input("Enter directory/path of printing documents:"))
    ap=findAvailablePrinters()    
    #pprint.pp(directoryListing(pathToPrint))
    for i in range(len(ap)):
        selectorList[i] = ap[i]["pPrinterName"]

    #pprint.pp(selectorList)
    
    #printerOption=int(input("Select from the above available printers:"))
    createAndReadTXTfile(directoryListing(pathToPrint))
    
