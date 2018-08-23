# encoding:

# BeautifulSoup4库
# 和lxml一样，解析和提取HTML/XML数据，lxml只会局部提取，BeautifulSoup是基于HTNL DOM的，性能要低于lxml，
# 但是它的API非常人性化，使用简单，支持CSS选择器、Python标准库中的HTML解析器、也支持lxml的XML解析器。


# 1、find_all方法的使用
from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html, 'lxml')  # 第一个参数是解析的文本，第二个参数是lxml解析器
# print(soup.prettify())
# 获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print("==================")
#     print(type(tr))  # <class 'bs4.element.Tag'>

# 获取第二个tr标签
# tr = soup.find_all('tr', limit=2)[1]  # limit最多获取几个元素
# print(tr)

# 获取所有class等于even的tr标签
# trs = soup.find_all('tr', class_='even')
# trs = soup.find_all('tr', attrs={'class': 'even'})
# for tr in trs:
#     print(tr)
#     print("=================")

# 将所有id等于test，class也等于test的a标签提取出来
# aList = soup.find_all('a', attrs={'id': 'test', 'class': 'test'})
# aList = soup.find_all('a', id='test', class_='test')
# for a in aList:
#     print(a)

# 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
    # 通过下标操作的方式
    # href = a['href']
    # print(href)
    # 通过attrs属性的方式
    # href = a.attrs['href']
    # print(href)

# 获取所有职位信息(纯文本)
# 第一种方式
# trs = soup.find_all('tr')[1:]  # 获取tr标签
# infos = []
# for tr in trs:
#     info = {}  # 存放职位信息
#     tds = tr.find_all('td')  # 获取tr标签下的td标签
#     title = tds[0].string  # 标题
#     category = tds[1].string  # 职位类别
#     nums = tds[2].string  # 招聘人数
#     city = tds[3].string  # 坐标
#     pubtime = tds[4].string  # 职位发布时间
#
#     info['title'] = title
#     info['category'] = category
#     info['nums'] = nums
#     info['city'] = city
#     info['pubtime'] = pubtime
#     infos.append(info)
#
# print(infos)

# 第二种方式
# trs = soup.find_all('tr')
# positions = []
# for tr in trs:
#     position = {}
#     infos = list(tr.stripped_strings)  # 获取tr标签下的所有非空白文本信息
#
#     position['title'] = infos[0]
#     position['category'] = infos[1]
#     position['nums'] = infos[2]
#     position['city'] = infos[3]
#     position['pubtime'] = infos[4]
#     positions.append(position)
#
# print(positions)

# 获取第一个tr标签的所有文本信息
# tr = soup.find('tr')
# print(type(tr.get_text()))
# print(tr.get_text())
