
import re
import xlwt

file = open("/Users/wheat/work/001_GL.TXT",'rU')
month_date ='2012/12'
file_month_date = []
#lines = len(file.readlines())
#print lines
for eachline in file: 
    #if month_date in eachline:
        #file_month_date=
        re.sub(r'\t',' ',eachline)
        if month_date in eachline:
           file_month_date.append(eachline)
#print file_month_date        
file.close()
def formatdata(trans_data):
    global enno,name,time,year_mon_day
    trans_data = re.sub(r'\t',' ',trans_data)
    datafinal = trans_data.split(' ')
    enno = datafinal[2]
    name = datafinal[3].decode('gbk').encode('utf-8')
    time = datafinal[-3]
    year_mon_day = datafinal[-4]
    #print enno,name,year_mon_day,time
for trans_data in file_month_date:
    formatdata(trans_data)
    
    print name

#xls = xlwt.Workbook()
#sheet = xls.add_sheet('sheet 1')
#sheet.write()

   # print name
   # print year_mon_day
   #print time
#for each_name in file_month_date:
#    if name in each_name:
#formatdata(file_month_date[1])
#print formatdata(file_month_date[1]).name
file.close()    
    
    