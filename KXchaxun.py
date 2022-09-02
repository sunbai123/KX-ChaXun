import execjs
import requests
import time
import sys

url = {
    "0":"http://mhub.hust.edu.cn/kxjsController/selectFreeRoom",
    "1":"http://mhub.hust.edu.cn/kxjsController/queryFreeRoomDetail",
    "2":"http://mhub.hust.edu.cn/kxjsController/selectFreeRoom"
}
    
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'cookie': ""

}

fanghao = {
    '东九楼A':'D091',
    '东九楼B':'D092',
    '东九楼C':'D093',
    '东九楼D':'D094',
}

fanghao1 = {
    'A':'D091',
    'B':'D092',
    'C':'D093',
    'D':'D094',
}

'''timetable = {
    '第一节':'08:45',
    '第二节':'09:40',
    '第三节':'10:55',
    '第四节':'11:50',
    '第五节':'15:15',
    '第六节':'16:05',
    '第七节':'17:10',
    '第八节':'18:00',
    '第九节':'19:45',
    '第十节':'20:35',
    '第十一节':'21:30',
    '第十二节':'22:20',
}'''

timetable = {
    '第一节':'08:45',
    '第二节':'09:40',
    '第三节':'10:55',
    '第四节':'11:50',
    '第五节':'14:45',
    '第六节':'15:35',
    '第七节':'16:40',
    '第八节':'17:30',
    '第九节':'19:15',
    '第十节':'20:05',
    '第十一节':'21:00',
    '第十二节':'21:50',
}

if sys.argv[1]=="0":
    temp2 = url[sys.argv[1]]

    temp1 = fanghao[sys.argv[3]]

    temp = timetable[sys.argv[4]]

    #print ('参数列表:', str(sys.argv))

    data  = {
        'sj': sys.argv[2],
        'jxlbh': temp1
    }

    headers["cookie"] = sys.argv[5]

    response = requests.post(url=temp2, headers=headers, data=data).json()


    for item in response['dataList']:
        if item['JSSJ'] == temp:
            print(item['JSMC'])

elif sys.argv[1]=="1":
    temp2 = url[sys.argv[1]]

    temp = fanghao1[sys.argv[3][0]]

    temp1 = temp + '0' + sys.argv[3][1:2] + '0' + sys.argv[3][2:4]

    data  = {
        'sj': sys.argv[2],
        'jxlbh': temp,
        'jsbh': temp1
    }


    headers["cookie"] = sys.argv[4]

    response = requests.post(url=temp2, headers=headers, data=data).json()

    for item in response['dataList']:
        print("第" + str(item["JC"]) +"节："+item["state"])

else:
    temp2 = url[sys.argv[1]]

    temp1 = fanghao[sys.argv[3]]

    data  = {
        'sj': sys.argv[2],
        'jxlbh': temp1
    }

    headers["cookie"] = sys.argv[6]

    response = requests.post(url=temp2, headers=headers, data=data).json()

    CArr = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

    for item in response['dataList']:
        if item['JSSJ'] == '08:45':
            CArr[0].add(item['JSMC'])
        if item['JSSJ'] == '09:40':
            CArr[1].add(item['JSMC'])
        if item['JSSJ'] == '10:55':
            CArr[2].add(item['JSMC'])
        if item['JSSJ'] == '11:50':
            CArr[3].add(item['JSMC'])
        if item['JSSJ'] == '14:45':
            CArr[4].add(item['JSMC'])
        if item['JSSJ'] == '15:35':
            CArr[5].add(item['JSMC'])
        if item['JSSJ'] == '16:40':
            CArr[6].add(item['JSMC'])
        if item['JSSJ'] == '17:30':
            CArr[7].add(item['JSMC'])
        if item['JSSJ'] == '19:15':
            CArr[8].add(item['JSMC'])
        if item['JSSJ'] == '20:05':
            CArr[9].add(item['JSMC'])
        if item['JSSJ'] == '21:00':
            CArr[10].add(item['JSMC'])
        if item['JSSJ'] == '21:50':
            CArr[11].add(item['JSMC'])

    for i in range(int(sys.argv[4]),int(sys.argv[5])):
        CArr[i] = CArr[i-1] & CArr[i]

    for item in CArr[int(sys.argv[5])-1]:
        print(item)
    


        