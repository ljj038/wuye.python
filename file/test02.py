#!/usr/bin/python
#coding=utf-8
#json encode
import json;
p = {220000:{220400:[220421],220800:[220821,220882,220881]}};
#json.dumps可以输出一个json串
j = json.dumps(p);
print "json encode : " , j;
#json.dump(f,json) 可以将json输出到文件
json.dump(j, open('write4.txt', 'w'));

#json decode
proPreFix = "├──";
citPreFix = "│   └──";
araPreFix = "│   │   └──";

#json.loads 可以从一个加密的json串中解密
print json.loads(j);
print;

#json.load 可以从一个文件读取json数据,并decode
f = open('province.json');
#一下为格式化打印 json.load 解密之后的数据
provinceDict = json.load(f);
for provinceId,value in dict.iteritems(provinceDict):
    cityCount = len(value);
    if(cityCount > 0):
        print ("{proPreFix}provinceId {provinceId},{cityCount} cities").format(proPreFix=proPreFix, provinceId=provinceId, cityCount=cityCount);
        for cityId,val in dict.iteritems(value):
            areaCount = len(val);
            if(areaCount > 0):
                print ("{citPreFix}cityId {cityId},{areaCount} areas").format(citPreFix = citPreFix, cityId = cityId, areaCount = areaCount);
                strArea = "";
                for area in val:
                    strArea += area + ",";
                print araPreFix , strArea[0:-1];
            else:
                print ("{citPreFix}cityId {cityId},all areas").format(citPreFix = citPreFix, cityId = cityId, areaCount = areaCount);
    else:
        print ("{proPreFix}provinceId {provinceId},all cities or areas").format(proPreFix = proPreFix, provinceId = provinceId);

#结果
console = '''
├──provinceId 220000,9 cities
│   └──cityId 220400,1 areas
│   │   └── 220421
│   └──cityId 220800,3 areas
│   │   └── 220821,220882,220881
│   └──cityId 220100,1 areas
│   │   └── 220112
│   └──cityId 220500,2 areas
│   │   └── 220521,220523
│   └──cityId 220200,2 areas
│   │   └── 220281,220211
│   └──cityId 220600,2 areas
│   │   └── 220681,220622
│   └──cityId 222400,2 areas
│   │   └── 222404,222403
│   └──cityId 220300,3 areas
│   │   └── 220303,220302,220323
│   └──cityId 220700,3 areas
│   │   └── 220721,220723,220722
├──provinceId 140000,1 cities
│   └──cityId 140300,all areas
├──provinceId 420000,1 cities
│   └──cityId 429000,1 areas
│   │   └── 429004
├──provinceId 350000,2 cities
│   └──cityId 350800,all areas
│   └──cityId 350700,all areas
├──provinceId 370000,5 cities
│   └──cityId 371700,2 areas
│   │   └── 371725,371702
│   └──cityId 370100,1 areas
│   │   └── 370126
│   └──cityId 371400,12 areas
│   │   └── 371402,371481,371424,371421,371422,371426,371425,371423,371401,371428,371427,371482
│   └──cityId 371300,1 areas
│   │   └── 371323
│   └──cityId 370500,1 areas
│   │   └── 370523
├──provinceId 230000,1 cities
│   └──cityId 230200,all areas
├──provinceId 620000,2 cities
│   └──cityId 621100,1 areas
│   │   └── 621126
│   └──cityId 620100,1 areas
│   │   └── 620122
├──provinceId 430000,1 cities
│   └──cityId 431300,all areas
├──provinceId 410000,2 cities
│   └──cityId 411600,1 areas
│   │   └── 411627
│   └──cityId 410500,all areas
├──provinceId 820000,all cities or areas
├──provinceId 210000,1 cities
│   └──cityId 210200,1 areas
│   │   └── 210213
''';
