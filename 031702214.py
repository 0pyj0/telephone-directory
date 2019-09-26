# -*- coding: 'utf-8' -*-

import re
import json
import requests

#pro = ["北京","天津","上海","重庆","河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","内蒙古","广西","西藏","宁夏","新疆维吾尔自治区","香港","澳门","台湾"];
#city = {'北京':["东城区","西城区","崇文区","宣武区","朝阳区","海淀区","丰台区","石景山区","房山区","通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","门头沟区","密云县","延庆县"],'天津':["和平区","河东区","河西区","南开区","河北区","红桥区","东丽区","西青区","北辰区","津南区","武清区","宝坻区","滨海新区","静海县","宁河县","蓟县"],'上海':["黄浦区","卢湾区","徐汇区","长宁区","静安区","普陀区","闸北区","虹口区","杨浦区","闵行区","宝山区","嘉定区","浦东新区","金山区","松江区","青浦区","奉贤区","崇明县"],'重庆':["渝中区","大渡口区","江北区","南岸区","北碚区","渝北区","巴南区","长寿区","双桥区","沙坪坝区","万盛区","万州区","涪陵区","黔江区","永川区","合川区","江津区","九龙坡区","南川区","綦江县","潼南县","荣昌县","璧山县","大足县","铜梁县","梁平县","开县","忠县","城口县","垫江县","武隆县","丰都县","奉节县","云阳县","巫溪县","巫山县","石柱土家族自治县","秀山土家族苗族自治县","酉阳土家族苗族自治县","彭水苗族土家族自治县"],'河北':["石家庄","唐山","秦皇岛","邯郸","邢台","保定","张家口","承德","沧州","廊坊","衡水"],'山西':["太原","大同","阳泉","长治","晋城","朔州","晋中","运城","忻州","临汾","吕梁"],'辽宁':["沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛"],'吉林':["长春","吉林","四平","辽源","通化","白山","松原","白城","延边朝鲜族自治州"],'黑龙江':["哈尔滨","齐齐哈尔","鹤岗","双鸭山","鸡西","大庆","伊春","牡丹江","佳木斯","七台河","黑河","绥化","大兴安岭"],'江苏':["南京","苏州","无锡","常州","镇江","南通","泰州","扬州","盐城","连云港","徐州","淮安","宿迁"],'浙江':["杭州","宁波","温州","嘉兴","湖州","绍兴","金华","衢州","舟山","台州","丽水"],'安徽':["合肥","芜湖","蚌埠","淮南","马鞍山","淮北","铜陵","安庆","黄山","滁州","阜阳","宿州","巢湖","六安","亳州","池州","宣城"],'福建':["福州","厦门","莆田","三明","泉州","漳州","南平","龙岩","宁德"],'江西':["南昌","景德镇","萍乡","九江","新余","鹰潭","赣州","吉安","宜春","抚州","上饶"],'山东':["济南","青岛","淄博","枣庄","东营","烟台","潍坊","济宁","泰安","威海","日照","莱芜","临沂","德州","聊城","滨州","菏泽"],'河南':["郑州","开封","洛阳","平顶山","安阳","鹤壁","新乡","焦作","濮阳","许昌","漯河","三门峡","南阳","商丘","信阳","周口","驻马店"],'湖北':["武汉","黄石","十堰","荆州","宜昌","襄樊","鄂州","荆门","孝感","黄冈","咸宁","随州","恩施"],'湖南':["长沙","株洲","湘潭","衡阳","邵阳","岳阳","常德","张家界","益阳","郴州","永州","怀化","娄底","湘西"],'广东':["广州","深圳","珠海","汕头","韶关","佛山","江门","湛江","茂名","肇庆","惠州","梅州","汕尾","河源","阳江","清远","东莞","中山","潮州","揭阳","云浮"],'海南':["海口","三亚"],'四川':["成都","自贡","攀枝花","泸州","德阳","绵阳","广元","遂宁","内江","乐山","南充","眉山","宜宾","广安","达州","雅安","巴中","资阳","阿坝","甘孜","凉山"],'贵州':["贵阳","六盘水","遵义","安顺","铜仁","毕节","黔西南","黔东南","黔南"],'云南':["昆明","曲靖","玉溪","保山","昭通","丽江","普洱","临沧","德宏","怒江","迪庆","大理","楚雄","红河","文山","西双版纳"],'陕西':["西安","铜川","宝鸡","咸阳","渭南","延安","汉中","榆林","安康","商洛"],'甘肃':["兰州","嘉峪关","金昌","白银","天水","武威","酒泉","张掖","庆阳","平凉","定西","陇南","临夏","甘南"],'青海':["西宁","海东","海北","海南","黄南","果洛","玉树","海西"],'内蒙古':["呼和浩特","包头","乌海","赤峰","通辽","鄂尔多斯","呼伦贝尔","巴彦淖尔","乌兰察布","锡林郭勒盟","兴安盟","阿拉善盟"],'广西':["南宁","柳州","桂林","梧州","北海","防城港","钦州","贵港","玉林","百色","贺州","河池","来宾","崇左"],'西藏':["拉萨","那曲","昌都","林芝","山南","日喀则","阿里"],'宁夏':["银川","石嘴山","吴忠","固原","中卫"],'新疆维吾尔自治区':["乌鲁木齐","克拉玛依","吐鲁番","哈密","和田","阿克苏","喀什","克孜勒苏","巴音郭楞","昌吉","博尔塔拉","伊犁","塔城","阿勒泰"],'香港':["香港岛","九龙东","九龙西","新界东","新界西"],'澳门':["澳门半岛","离岛"],'台湾':["台北","高雄","基隆","新竹","台中","嘉义","台南市"]};
def fname():
    global name
    global mlist
    name=mlist.split(",")[0]
    mlist=re.sub(name,'',mlist,1)#去掉姓名

def fphonenum():
    global mlist
    global phonenum
    phonenum=re.findall('\d{11}',mlist)
    phonenum=''.join(phonenum)       #print(type(phonenum))
    mlist=re.sub(phonenum,'',mlist,1)#去掉电话
    mlist=''.join(mlist)  #将list转为string

def fprovince():
    global mlist
    global pro
    province=content["geocodes"][0]["province"]
    if province=='':#直辖市
        province=content["geocodes"][0]["province"]#直辖市即省份
    pro=province
    flist=mlist
    if province:
        flist=re.sub(province,'',mlist,1)#去掉province,  这里flist,mlist[i]用str形式的
        if flist==mlist:
            mlist=list(mlist)
            flist=list(flist)
            province=list(province)
            while province[0]==mlist[0]:
                mlist.pop(0)
                province.pop(0)
            mlist=''.join(mlist)
            flist=''.join(flist)
        else:
            mlist=flist  #有“省”字的，可以直接用函数去掉的情况
    else:
        pro=''#province没有的情况,为了不输出[]

def fcity():
    global mlist
    global ci
    global pro
    city = content["geocodes"][0]["city"]  #geocodes为地理编码信息列表
    ci=city
    if city=='':#直辖市
        city=content["geocodes"][0]["province"]#直辖市即城市
    if city:         
        flist=re.sub(city,'',mlist,1)#去掉city
        if flist==mlist:
            mlist=list(mlist)
            flist=list(flist)
            city=list(city)
            while city[0]==mlist[0]:
                mlist.pop(0)
                city.pop(0)
            mlist=''.join(mlist)
        else:
            mlist=flist  #有“市”字的，可以直接用函数去掉的情况
    else:
        ci=''#city没有的情况,为了不输出[]

def fdistrict():
    global mlist
    global dis
    district=content["geocodes"][0]["district"]#geocodes为地理编码信息列表，district为地址所在的区
    dis=district
    if district:
        mlist=re.sub(district,'',mlist,1)#去掉district    
    else:
        dis=''#district没有的情况,为了不输出[]
  
def ftown():
    global mlist
    global tow
    town = respond["regeocode"]["addressComponent"]["township"] #regeocode为逆地理编码，addressComponent为地址元素列表，town坐标点所在乡镇/街道
    tow=town
    rt = re.search( town, mlist) #匹配地址
    if town!=None:
        mlist=re.sub(town,'',mlist,1)#去掉town
    else:
        tow=''#town没有的情况,为了不输出[]

def froad():
    global mlist
    global ro
    road = re.findall('(.*?[路街巷道])', mlist)
    ro=road
    if road:
        mlist=list(mlist)
        while 100:
            if mlist[0]=='路'or mlist[0]=='街'or mlist[0]=='巷'or mlist[0]=='道':
                mlist.pop(0)
                break
            mlist.pop(0)
        mlist=''.join(mlist)#去掉road
    else:
        ro=''#road没有的情况,为了不输出[]
    ro=''.join(ro)

    
def fdoornum():
    global mlist
    global door
    doornum= re.findall('(.*?[号])', mlist)
    door=doornum
    if doornum:
        mlist=list(mlist)
        while mlist[0]:
            if mlist[0]=='号':
                mlist.pop(0)
                break
            mlist.pop(0)
        mlist=''.join(mlist)#去掉doornum
    else:
        door=''#doornum没有的情况,为了不输出[]
    door=''.join(door)



def ffive():
    global mlist
    global final
    global pro
    string=mlist
    final={}
    final["姓名"]=name
    final["手机"]=phonenum
    finallist=[]
    if pro=="上海市":
        pro="上海"
    if pro=="北京市":
        pro="北京"
    if pro=="天津市":
        pro="天津"
    if pro=="重庆市":
        pro="重庆"
    finallist.append(pro)
    finallist.append(ci)
    finallist.append(dis)
    finallist.append(tow)
    finallist.append(string)
    final["地址"]=finallist

def fseven():
    global mlist
    global final
    global pro
    string=mlist
    final={}
    final["姓名"]=name
    final["手机"]=phonenum
    finallist=[]
    if pro=="上海市":
        pro="上海"
    if pro=="北京市":
        pro="北京"
    if pro=="天津市":
        pro="天津"
    if pro=="重庆市":
        pro="重庆"
    finallist.append(pro)
    finallist.append(ci)
    finallist.append(dis)
    finallist.append(tow)
    finallist.append(ro)
    finallist.append(door)
    finallist.append(string)
    final["地址"]=finallist

    
mlist=input()

mlist.split('\\n')
#from ast import literal_eval
#mlist=literal_eval(ll)#将文件中的内容转换为list

url = "https://restapi.amap.com/v3/geocode/geo?key=6a6615350026e24aa1c159785e70a709" #使用高德API


kind=int(mlist[0])
mlist=list(mlist)
mlist.pop(0)#去掉难度等级
mlist.pop(0)#去掉!
mlist=''.join(mlist)

fname();
fphonenum();
    
urlweb = url + "&address=" + mlist  #urlweb为完整API请求链接
alldata = requests.get(urlweb).text  #webdata为网站返回数据包
content = json.loads(alldata)  #将json转换为字典
  
positon = content["geocodes"][0]["location"] #geocodes为地理编码信息列表，location为坐标点，两者用于逆地理编码
rurl = "https://restapi.amap.com/v3/geocode/regeo?output=JSON&key=6a6615350026e24aa1c159785e70a709&radius=100&extensions=base"
rurlweb = rurl + "&location=" + positon #逆地理编码API
respond = requests.get(rurlweb).text #返回详细地理信息
respond = json.loads(respond) #格式转化

mlist=re.sub(',','',mlist,1)   #去掉,
string=''.join(mlist[0:-1])
mlist=string   #这两步是去掉.的

fprovince();#划分省份
fcity();#划分城市
fdistrict();#划分城区/县城
ftown();#划分乡镇


if kind==1:
    ffive();
else:
    froad();
    fdoornum();
    fseven();
#print(final)
print(json.dumps(final))
