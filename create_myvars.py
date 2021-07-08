from os import name
import sys
import xlrd
import jinja2
jinjaFile = jinja2.FileSystemLoader('F:\python') # 文件路径在当前文件夹
jinjaEnv = jinja2.Environment(loader=jinjaFile) # 定义jinja2环境
part1 = jinjaEnv.get_template('myvars_part1.j2')
part2 = jinjaEnv.get_template('myvars_part2.j2')


dict1={
    'folder':'VM_121_PT_docker',
    'datacenter':'DC_PRICE'
}
dict2={
       'name': '',
       'esxi_hostname': '',
       'datastore': '', 
       'd1_size_gb': '',
        'd2_size_gb': '',
        'memory_mb': '',
        'num_cpus': '',
        'ip': '',
        'gw': '',
        'vlan': '',
        'hostname': '',
        'sys_ver': ''
      }

tempout = part1.render(dict1)
workbook= xlrd.open_workbook('F:\\python\\test.xlsx')
sheet=workbook.sheet_by_index(2)
print(sheet.name,sheet.ncols,sheet.nrows)
tempout1=''
for i in range(sheet.nrows):
    rowx=sheet.row_values(i)
    dict2['name']=rowx[0]
    dict2['d1_size_gb']=int(rowx[6])
    dict2['d2_size_gb']=int(rowx[7])
    dict2['memory_mb']=int(rowx[5]*1024)
    dict2['num_cpus']=int(rowx[4])
    dict2['ip']=rowx[3]
    dict2['hostname']=rowx[0]
    #print(dict2)
    tempout1 = tempout1+part2.render(dict2)

with open('F:\\python\\myvars.yml','w') as f:
    f.write(tempout+'\n')
    f.write(tempout1)
    f.close()



