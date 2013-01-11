
import re
duty_file = open("/Users/wheat/work/001_GL.TXT", 'r') # open the data
duty_file_lines = duty_file.readlines() #read the data
print type(duty_file_lines)
#print duty_file_lines[0:2]

testline = duty_file_lines[1]
print type(testline)
#print duty_file_lines
duty_file.close()
#print duty_file.closed
print testline
#print duty_file_lines[2]
print testline.decode('gbk').encode('utf-8')
#duty_file_lines
#print testline.findall