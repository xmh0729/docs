import requests,json,sys,random,time,os,re,openpyxl,urllib.parse,urllib3,glob
urllib3.disable_warnings()
 
def User_gent():
    agent=[
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    ]
    fackender={}
    fackender['Cache-Control'] = "max-age=0"
    fackender['sec-ch-ua-platform'] = "Windows"
    fackender['Upgrade-Insecure-Requests'] = "1"
    fackender['user-agent']=agent[random.randint(0,len(agent)-1)]
    fackender['Sec-Fetch-Site'] = "same-origin"
    fackender['Sec-Fetch-Mode'] = "navigate"
    fackender['Accept-Encoding'] = "gzip, deflate"
    fackender['Accept-Language'] = "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    fackender['Connection'] = "close"
    return (fackender)
 
#针对无中文
def Secone(fileName,FilePath,Fpath):
    with open(file=fileName, mode="r", encoding='utf-8') as f1:
        # 用来计数
        sus_count = 0
        lines = f1.readlines()
        for i in range(0, len(lines)):
            #针对其他md内的图片文件，一般只需要修改此处即可
            pattern = re.compile(r"[(](https://cdn.nlark.com/.*?)[)]")
            urls = re.findall(pattern, lines[i])
            num = 0
            for url in urls:
                try:
                    if len(url)!=0:
                        #从URL中提取文件名
                        url = url.replace("(", "").replace(")", "")
                        #从URL中提取文件名，如果没有文件名则使用时间戳
                        parsed_url = urllib.parse.urlparse(url)
                        path = parsed_url.path
                        filename = os.path.basename(path)
                        if filename and '.' in filename:
                            #如果URL中有文件名，使用它
                            image_name = filename
                        else:
                            #如果没有文件名，使用时间戳
                            timestamp = int(time.time())
                            image_name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(timestamp+num)))+str(i)+".png"
                        #请求图片
                        img = requests.get(url,headers=User_gent(),verify=False,timeout = 2)
                        #判断是否成功获取图片
                        if img.status_code != 200:
                           print('第', i, '行：', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',img.status_code)
                           continue
                        #存储网络图片到本地
                        print(Fpath)
                        target = open(image_name,'ab')
                        target.write(img.content)
                        target.close()
                        lines[i] = lines[i].replace(url, FilePath + '\\' + image_name)
                        print('第',sus_count,'个''第',i,'行：',url+'成功转为'+ FilePath + '\\' + image_name)
                        sus_count += 1
                        num += 1
                except:
                    print("图片路径错误")
    #重新保存md文件
    # with open(file=fileName, mode='w', encoding='utf-8') as f2:
    #     print(fileName)
    #     f2.writelines(lines)
 
#针对有中文的文件名
def ChineseSecone_test(fileName,FilePath,Fpath):
    with open(file=fileName, mode="r", encoding='utf-8') as f1:
        # 用来计数
        sus_count = 0
        lines = f1.readlines()
        for i in range(0, len(lines)):
            num = 0
            #针对其他md内的图片文件，一般只需要修改此处即可
            pattern = re.compile(r"[(](https://cdn.nlark.com/.*?)[)]")
            urls = re.findall(pattern, lines[i])
            for url in urls:
                try:
                    if len(url)!=0:
                        #从URL中提取文件名
                        url = url.replace("(", "").replace(")", "")
                        #从URL中提取文件名，如果没有文件名则使用时间戳
                        parsed_url = urllib.parse.urlparse(url)
                        path = parsed_url.path
                        filename = os.path.basename(path)
                        if filename and '.' in filename:
                            #如果URL中有文件名，使用它
                            image_name = filename
                        else:
                            #如果没有文件名，使用时间戳
                            timestamp = int(time.time())
                            image_name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(timestamp+num)))+str(i)+".png"
                        #请求图片
                        img = requests.get(url,headers=User_gent(),verify=False,timeout = 2)
                        #判断是否成功获取图片
                        if img.status_code != 200:
                           print('第', i, '行：', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',img.status_code)
                           continue
                        #存储网络图片到本地
                        target = open(Fpath + image_name,'ab')
                        target.write(img.content)
                        target.close()
                        lines[i] = lines[i].replace(url, FilePath + '\\' + image_name)
                        print('第',sus_count,'个''第',i,'行：',url+'成功转为'+ FilePath + '\\' + image_name)
                        sus_count += 1
                        num += 1
                except:
                    print("图片路径错误")
    #重新保存md文件
    with open(file=fileName, mode='w', encoding='utf-8') as f2:
        print(fileName)
        f2.writelines(lines)
 
#判断是否有中文字符
def Chinese_char(chars):
    return bool(re.search(r'[\u4e00-\u9fff]', chars))
 
if __name__=='__main__':
    ImgDirectory = 'Image'              #存放图片的目录
    query = input("单文件请按1，全目录按2：")
    if query == "1":
        file_suffix = '.md'
        fileName = input("输入md文件：")
        # 获取上一级目录路径
        current_path = fileName
        parent_path = os.path.abspath(os.path.join(current_path, '..'))
        # 新建存放所有图片目录 image
        pickure = parent_path + '\\' + ImgDirectory
 
        if not os.path.exists(pickure):
            os.makedirs(pickure)
        try:
            #以.切割出后缀md
            fileNames = fileName.split(".")
            #以\切割出文件名名称
            Fname = fileNames[0].split("\\")
            for file in Fname:
                FilePath = file      # 得到最后一个为文件目录
            #创建文件夹，如果不存在则新建
            if not os.path.exists(ImgDirectory + '\\' + FilePath):
                #判断文件名中是否有中文
                if (Chinese_char(FilePath) == True):
                    #在文件名中去掉中文括号
                    Fstring = re.sub(r'[\u4e00-\u9fff（）（）（）]+', '', FilePath)
                    #去除空格
                    Fstring = re.sub(r' ', '', Fstring)
                    # 给后续文件夹命名
                    FilePath = ImgDirectory + '\\' +  Fstring + '-' + 'Chinese'
                    # 得到完整目录地址
                    Fpath = pickure + '\\'+Fstring + '-' + 'Chinese'+'\\'
                    # 新建文件夹
                    if not os.path.exists(Fpath):
                        os.makedirs(Fpath)
                    ChineseSecone_test(fileName, FilePath, Fpath)
                else:
                    Fpath = fileNames[0] + '\\'
                    Fpath = pickure + '\\' + FilePath  # FilePath此时是文件名称
                    FilePath = ImgDirectory + '\\' + FilePath  # Image/111
                    print('Fpath',Fpath)
                    print('FilePath',FilePath)
                    if not os.path.exists(Fpath):
                        os.makedirs(Fpath)  # D:\test\Image\111
                    Secone(fileName, FilePath, Fpath)
        except:
            print("单个md文件获取失败")
    elif query == "2":
        Path = input("输入md文件目录所在路径（D:\test)：")
        md_files = glob.glob(os.path.join(Path, '*.md'))
        num = 1
        # 获取上一级目录路径
        current_path = md_files[0]
        parent_path = os.path.abspath(os.path.join(current_path, '..'))
        # 新建存放所有图片目录 image
        pickure = parent_path + '\\' + ImgDirectory
        if not os.path.exists(pickure):
            os.makedirs(pickure)
        for fileName in md_files:
            if os.path.exists(pickure):
                #以. 切割出后缀md
                fileNames = fileName.split(".")
                #以\切割出文件名名称
                Fname = fileNames[0].split("\\")
                for file in Fname:
                    # 得到最后一个为文件名名称，将其进行判断是否有中文
                    FilePath = file
                # 创建文件夹，如果不存在则新建
                if not os.path.exists(ImgDirectory + '\\' + FilePath):
                    # 判断文件名中是否有中文
                    if (Chinese_char(FilePath) == True):
                        # 在文件名中去掉中文括号
                        Fstring = re.sub(r'[\u4e00-\u9fff（）（）（）]+', '', FilePath)
                        # 去除空格
                        Fstring = re.sub(r' ', '', Fstring)
                        # 给后续新建文件夹命名
                        FilePath = ImgDirectory + '\\' + Fstring + str(num) + '-' + 'Chinese'
                        # 得到一个完整的目录地址
                        Fpath = pickure + '\\' + Fstring + str(num) + '-' + 'Chinese' + '\\'
                        # 新建一个文件夹
                        if not os.path.exists(Fpath):
                            os.makedirs(Fpath)
                        ChineseSecone_test(fileName, FilePath, Fpath)
                    else:
                        Fpath = fileNames[0] + '\\'     #d:\test\111
                        # 得到一个完整的目录地址,后续准备新建文件夹
                        Fpath = pickure + '\\' + FilePath       #FilePath此时是文件名称
                        FilePath = ImgDirectory + '\\' + FilePath   #Image/111
                        if not os.path.exists(Fpath):
                            os.makedirs(Fpath)                  #D:\test\Image\111
                        Secone(fileName, FilePath,Fpath)
            else:
                pass
            num = num + 1
    else:
        print("未输入")