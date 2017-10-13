# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from query.models import SystemCommonSensitiveWords as csw
from query.models import SystemOtherSensitiveWords as osw
from query.models import SystemClause as sc
from query.models import SystemDistrict as sd
from query.models import SystemCategory
from query.models import SystemImage as si
from query.tools import Tool, PicTool
from query.models import SystemUserSimple as sus
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import base64

def querying(request,params,content):
    item_list=[]
    ctx ={}
    list=[]
    category_id=params['category_id']
    district_id=params['district_id']
    text=params['text']
    rawText=params['text']

    # print(rawText)
    #普通关键词总数
    num=csw.objects.count();
    #查找到的词数
    count=0
    #两套循环
    for i in range(num):
        item=csw.objects.get(id=i+1)
        pos=text.find(item.word)
        while pos!=-1:
            #能够找到这个单词
            show_item={}
            show_item['word']=item.word
            show_item['risk_level']=item.advice_id
            clause=sc.objects.get(id=item.advice_id)
            show_item['principle']=clause.clause
            show_item['range']=0
            tp=[pos,item.word,item.advice_id,show_item]
            list.append(tp)
            pos=text.find(item.word,pos+1)

    keynum=len(list)
    
    #排序
    list.sort()
    list2=[]

    text=text.replace(r'%','百分号')

    #循环，逐个替换单词
    for i in range(keynum):
        keyword=list[i][1]
        #print keyword
        word="<span class=\"jinzhi\">"+keyword+"</span>"
        word+='<sup class="jinzhi2">['+str(i+1)+']</sup>'
        show_item=list[i][3]
        show_item['count']=i
        item_list.append(show_item)
        list2.append(word)
        text=text.replace(keyword,'%s')
        pass

    #计算分数
    if keynum==0:
        score=100
        score_text='棒棒哒！看好你呦！'
        score_class='score_ok'
    elif keynum>0:
        score=88-29*keynum
        score_text='成绩好糟糕！快来看看有那些地方违规了！'
        score_class='score_bad'

    if score<0:
        score=0
    
    print(len(list2))
    # text=text % tuple(list2)
    try:
        text=text % tuple(list2)
    except:
        print(text.count('%s'))
        pass
    text=text.replace('百分号',r'%')

    item=SystemCategory.objects.get(id=category_id)
    category=item.category
    item=sd.objects.get(id=district_id)
    district=item.district

    text="<h4>"+text+"</h4>"
    content['upbar_text']=rawText 
    content['rawText']=rawText
    content['text']=text
    content['list']=item_list
    content['score']=score
    content['score_text']=score_text
    content['score_class']=score_class
    content['category']=category
    content['district']=district

    fengxian=0
    weigui=keynum
    zhicheng=0
    tishi=0

    content['fengxian']=fengxian
    content['weigui']=weigui
    content['zhicheng']=zhicheng
    content['tishi']=tishi

    print('过来了吗')
    return content

def query_result(request,content):
    return render(request, 'query/index/query.html', content)

def query_text(request,params,content):
    content['text']=params['text']
    content= querying(request,params,content)
    return query_result(request,content)

def query_link(request,params,content):
    tool=Tool()
    text=tool.get_text(params['link'])
    params['text']=text
    content['text']=params['text']
    content= querying(request,params,content)
    return query_result(request,content)

def query_image(request,params,content):        
    print("this is image")
    pic_tool=PicTool(params['image'])
    text=pic_tool.get_text()
    params['text']=text
    content['text']=params['text']
    content= querying(request,params,content)
    return query_result(request,content)


# Create your views here.
@csrf_exempt
def hello(request):
    mode='none'
    content= {}
    params={}
    request.encoding='utf-8'
    # 获取范畴id
    if 'category_id' in request.POST:
        category_id=request.POST['category']
    else:
        category_id='19'
    params['category_id']=category_id

    # 获取地区id
    if 'district_id' in request.POST:
        district_id=request.POST['district']
    else:
        district_id='1'    
    params['district_id']=district_id

    # 获得查询文字
    if 'upbar_text' in request.POST:
        #从本页面上面
        text= request.POST['upbar_text']
        params['text']=text
        # mode='text'
    elif 'text' in request.POST:
        #从入口页面上面输入
        text= request.POST['text']
        params['text']=text
        # mode='text'
    else:
        text=''


    # 获取链接地址
    if 'link_text' in request.POST:
        link=request.POST['link_text']
        params['link']=link
        # mode='link'
    else:
        link=''


    if 'image' in request.POST and request.POST['image']!='':
        pic=request.POST['image']
        #new_image=si(image=request.FILES.get('image'))
        #new_image.save()
        params['image']=pic
        # mode='image'
    else:
        pic=''

    a=request.FILES.dict()
    if 'image_file' in a:
        image_file=a['image_file']
        pic=base64.b64encode(image_file.read())
        pic=str(pic)
        params['image']=pic[2:-1]
        # mode='image_file'
    else:
        pic=''

    print(request.POST)
    if 'mode' in request.POST:
        mode_num=int(request.POST['mode'])
        print(mode_num)
    else:
        mode_num=-1

    # print(request.FILES)
    # print(request.FILES.dict())
    # a=request.FILES.dict()
    # print(a['image_file'])

    if mode_num==1:
        return query_text(request,params,content)
    elif mode_num==3:
        return query_link(request,params,content)
    elif mode_num==2:
        return query_image(request,params,content)
    else:
        return HttpResponse('<p>错误</p>')


def index(request):
    content={}
    # 获取范畴id
    if 'category_id' in request.POST:
        category_id=request.POST['category']
    else:
        category_id='19'

    # 获取地区id
    if 'district_id' in request.POST:
        district_id=request.POST['district']
    else:
        district_id='1'

    # 获得查询文字
    if 'upbar_text' in request.POST:
        #从本页面上面
        text= request.POST['upbar_text']
    elif 'text' in request.POST:
        #从入口页面上面输入
        text= request.POST['text']
    else:
        text=''
    content['text']=text
    return render(request,'query/index/index.html',content)

def cost(request):
    content={}
    cost_list=[]
    for i in range(1,5):
        cost_item={}
        cost_item['num']=str(i*20)
        cost_list.append(cost_item)
    cost_list[0]['class']='success'
    cost_list[1]['class']='primary'
    cost_list[2]['class']='warning'
    cost_list[3]['class']='danger'
    cost_list[0]['command_class']='success'
    cost_list[1]['command_class']='primary'
    cost_list[2]['command_class']='warning'
    cost_list[3]['command_class']='danger'
    cost_list[0]['command']='违反'
    cost_list[1]['command']='合规'
    cost_list[2]['command']='法律咨询'
    cost_list[3]['command']='一键输出'
    content['cost_list']=cost_list
    return render(request,'query/index/cost.html',content)

def black(request):
    content={}
    return render(request,'query/index/black.html',content)

def insertWords(request):
    commonStr="国家级、世界级、最佳、最大、唯一、首个、"+\
    "首选、最好、精确、最高、最低、最具、最便宜、"+\
    "填补国内空白、绝对、独家、首家、最新、金牌、名牌、"+\
    "优秀、最先、全球首发、"+\
    "全网首发、世界领先、"+\
    "最时尚、极品、顶级、顶尖、"+\
    "终极、最受欢迎、王牌、销量冠军、第一、NO.1、"+\
    "Top1、极致、永久、掌门人、领袖品牌、"+\
    "独一无二、绝无仅有、前无古人、史无前例、万能、100％"
    makeupStr ="防止过敏、防晒、预防皮肤癌、抗菌、消炎、祛痘、最高医疗价值、天然药物、快速止痒、消肿、促进愈合"
    healthStr="调节血脂、脑血栓、中风、老年痴呆症、动脉硬化、末梢血管阻塞"
    foodStr="抗癌、腰腿痛、关节炎、肩周炎"
    medicalStr="包治百病、药到病除、100%治愈、治愈率高"
    estateStr="学区、重点小学、学区房"

    commonAdviceStr='''中华人民共和国广告法（2015修订）
第九条  广告不得有下列情形：
（一）使用或者变相使用中华人民共和国的国旗、国歌、国徽，军旗、军歌、军徽；
（二）使用或者变相使用国家机关、国家机关工作人员的名义或者形象；
（三）使用“国家级”、“最高级”、“最佳”等用语；
（四）损害国家的尊严或者利益，泄露国家秘密；
（五）妨碍社会安定，损害社会公共利益；
（六）危害人身、财产安全，泄露个人隐私；
（七）妨碍社会公共秩序或者违背社会良好风尚；
（八）含有淫秽、色情、赌博、迷信、恐怖、暴力的内容；
（九）含有民族、种族、宗教、性别歧视的内容；
（十）妨碍环境、自然资源或者文化遗产保护；
（十一）法律、行政法规规定禁止的其他情形。
'''    
    healthAdviceStr='''中华人民共和国广告法（2015修订）
第十八条    保健食品广告不得含有下列内容：
（一）表示功效、安全性的断言或者保证；
（二）涉及疾病预防、治疗功能；
（三）声称或者暗示广告商品为保障健康所必需；
（四）与药品、其他保健食品进行比较；
（五）利用广告代言人作推荐、证明；
（六）法律、行政法规规定禁止的其他内容。
保健食品广告应当显著标明“本品不能代替药物”。
'''
    
    medicalAdviceStr='''医疗广告管理办法（2006修订）
第七条    医疗广告的表现形式不得含有以下情形：
（一）涉及医疗技术、诊疗方法、疾病名称、药物的；
（二）保证治愈或者隐含保证治愈的；
（三）宣传治愈率、有效率等诊疗效果的；
（四）淫秽、迷信、荒诞的；
（五）贬低他人的；
（六）利用患者、卫生技术人员、医学教育科研机构及人员以及其他社会社团、组织的名义、形象作证明的；
（七）使用解放军和武警部队名义的；
（八）法律、行政法规规定禁止的其他情形。
    '''

    estateAdviceStr='''中华人民共和国广告法（2015修订）
第二十六条    房地产广告，房源信息应当真实，面积应当表明为建筑面积或者套内建筑面积，并不得含有下列内容：
（一）升值或者投资回报的承诺；
（二）以项目到达某一具体参照物的所需时间表示项目位置；
（三）违反国家有关价格管理的规定；
（四）对规划或者建设中的交通、商业、文化教育设施以及其他市政条件作误导宣传。
'''
    educateAdviceStr='''中华人民共和国广告法（2015修订）
第二十四条    教育、培训广告不得含有下列内容：
（一）对升学、通过考试、获得学位学历或者合格证书，或者对教育、培训的效果作出明示或者暗示的保证性承诺；
（二）明示或者暗示有相关考试机构或者其工作人员、考试命题人员参与教育、培训；
（三）利用科研单位、学术机构、教育机构、行业协会、专业人士、受益者的名义或者形象作推荐、证明。
'''
    
    investAdviceStr='''中华人民共和国广告法（2015修订）
第二十五条    招商等有投资回报预期的商品或者服务广告，应当对可能存在的风险以及风险责任承担有合理提示或者警示，并不得含有下列内容：
（一）对未来效果、收益或者与其相关的情况作出保证性承诺，明示或者暗示保本、无风险或者保收益等，国家另有规定的除外；
（二）利用学术机构、行业协会、专业人士、受益者的名义或者形象作推荐、证明。
'''

    #清空三个表
    csw.objects.all().delete()
    osw.objects.all().delete()
    sc.objects.all().delete()
    SystemCategory.objects.all().delete()
    sd.objects.all().delete()

    #普通词汇
    common=commonStr.split('、')
    for i in range(len(common)):
        item=csw(id=i+1,word=common[i],advice_id=1)
        item.save()

    #化妆品词汇
    #化妆品代号为10
    makeup=makeupStr.split('、')
    other_count=0
    for i in range(len(makeup)):
        other_count=other_count+1
        item=osw(id=other_count,word=makeup[i],advice_id=2,
            district_id=-1,category_id=10)
        item.save()

    #保健品词汇
    #保健品代号为7
    health=healthStr.split('、')
    for i in range(len(health)):
        other_count=other_count+1
        item=osw(id=other_count,word=health[i],advice_id=2,
            district_id=-1,category_id=7)
        item.save()

    #食品词汇
    #食品代号为6
    food=foodStr.split('、')
    for i in range(len(food)):
        other_count=other_count+1
        item=osw(id=other_count,word=food[i],advice_id=2,
            district_id=-1,category_id=6)
        item.save()

    #医疗词汇
    #医疗为8,9
    medical=medicalStr.split('、')
    for i in range(len(medical)):
        other_count=other_count+1
        item=osw(id=other_count,word=medical[i],advice_id=3,
            district_id=-1,category_id=8)
        item.save()

    #医疗词汇
    #医疗为8,9
    medical=medicalStr.split('、')
    for i in range(len(medical)):
        other_count=other_count+1
        item=osw(id=other_count,word=medical[i],advice_id=3,
            district_id=-1,category_id=9)
        item.save()

    #房地产词汇
    #房地产为13
    estate=estateStr.split('、')
    for i in range(len(estate)):
        other_count=other_count+1
        item=osw(id=other_count,word=estate[i],advice_id=4,
            district_id=-1,category_id=13)
        item.save()

    #插入地区
    district_list=['全国','北京','上海','广东',
    '江苏','浙江','河北','四川','福建','安徽',
    '湖南','其他']
    for i in range(len(district_list)):
        item=sd(id=i+1,district=district_list[i])
        item.save()

    #插入范畴
    category_list=[r'服装/鞋帽/视频','电子电器(非医疗)','家居家装',
    '母婴玩具',r'影视/文化/娱乐','食品(非保健食品)',
    '保健食品',r'药品/医疗器械','医疗机构/医疗服务',
    '化妆品（个人护理）','汽车','旅游',
    '房地产','r教育/培训','投资',
    r'法律/财税/咨询','信息服务','其他','不限']
    for i in range(len(category_list)):
        item=SystemCategory(id=i+1,category=category_list[i])
        item.save()

    #插入提示
    hint_list=[commonAdviceStr,healthAdviceStr,
        medicalAdviceStr,estateAdviceStr,educateAdviceStr,
        investAdviceStr]
    for i in range(len(hint_list)):
        item=sc(id=i+1,clause=hint_list[i])
        item.save()

    return HttpResponse('<p>插入成功</p>')

def upload(request):
    if request.method=='POST':
        print(request.FILES)
        new_image=si(image=request.FILES.get('image'))
        new_image.save()
    return render(request,'query/index/upload.html')

def show(request):
    images=si.objects.all()
    content={
        'images':images,
    }
    return render(request,'query/index/show.html',content)


def register(request):
    content={}

    # 获得用户名
    if 'register_username' in request.POST and len(request.POST['register_username'])>0:
        r_username= request.POST['register_username']
    else:
        content['error']='请输入用户名'
        return render(request,'query/index/error.html',content)

    # 获得密码
    if 'register_password' in request.POST and len(request.POST['register_password'])>0:
        #从本页面上面
        r_password= request.POST['register_password']
    else:
        content['error']='请输入密码'
        return render(request,'query/index/error.html',content)

    # 获得密码2
    if 'register_password2' in request.POST and len(request.POST['register_password2'])>0:
        #从本页面上面
        r_password2= request.POST['register_password2']
    else:
        content['error']='请再次输入密码'
        return render(request,'query/index/error.html',content)

    # 获得电话号码
    if 'register_phone' in request.POST and len(request.POST['register_phone'])>0:
        r_phone=request.POST['register_phone']
    else:
        content['error']='请输入手机号码'
        return render(request,'query/index/error.html',content)

    # 获得email
    if 'register_email' in request.POST:
        r_email=request.POST['register_email']
    else:
        content['error']='请输入邮箱'
        return render(request,'query/index/error.html',content)

    # 真正的业务
    # 首先检查验证码(暂时不弄)
    # 然后检查两次密码是否一致
    if r_password!=r_password2:
        content['error']='两次密码输出不一致'
        return render(request,'query/index/error.html',content)

    # 然后插入，捕获数据库错误
    item=sus(username=r_username,password=make_password(r_password,None,'pbkdf2_sha256'),
        email=r_email,phone=r_phone)
    try:
        item.save()
    except Exception as e:
        arg=e.args
        if arg[0]==1062:
            content['error']='已经有了同名的用户，请再选择一个用户名'
        else:
            content['error']='插入数据库失败'
        return render(request,'query/index/error.html',content)

    # 没啥错就返会成功
    content['success']='注册成功'
    return render(request,'query/index/success.html',content)

def error(request):
    pass

def success(request):
    pass

def login(request):
    content={}
    user = sus.objects.get(username=request.POST['login_username'])
    password=request.POST['login_password']
    if check_password(password,user.password):
        request.session['user_id'] = user.id
        content['success']='登录成功'
        return render(request,'query/index/success.html',content)
    else:
        content['error']='登录失败，原因是：用户名和密码不匹配'
        return render(request,'query/index/error.html',content)
         
         
def logout(request):
    content={}
    try:
        del request.session['user_id']
    except KeyError:
        content['error']='注销失败，原因是：您还未登录'
        return render(request,'query/index/error.html',content)

    content['success']='注销成功'
    return render(request,'query/index/success.html',content)
