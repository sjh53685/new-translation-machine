from PyQt5.Qt import QFileDialog, QErrorMessage
import urllib.request
import re


def input(text_put, window):
    file = QFileDialog.getOpenFileName(window, '文件打开', './', 'Table(*.txt)', 'Table(*.txt)')
    if file[0] != '':
        with open(file[0], 'r') as r:
            item = r.read()
        text_put.setPlainText(item)


def output(text_put, window):
    item = text_put.toPlainText()
    file = QFileDialog.getSaveFileName(window, '文件保存', './', 'Table(*.txt)', 'Table(*.txt)')
    if file[0] != '':
        with open(file[0], 'w') as w:
            w.write(item)


def translate(text_put, window):
    item = text_put.toPlainText()
    list_do = item.split('\n')
    while '' in list_do:
        list_do.remove('')
    result: [2, 3, 45, 2]
    list_result = []

    try:
        n = len(list_do)

        for dancicnt in range(n):
            def getHtml(url):
                page = urllib.request.urlopen(url)
                html = page.read()
                return html

            danci = list_do[dancicnt]
            print("正在查询：" + danci, end='')
            list_result.append('{}.{}'.format(dancicnt + 1, danci))
            danci = danci.replace(' ', '%20')

            wangzhi = "http://dict.youdao.com/w/" + danci
            html = getHtml(wangzhi)

            def getImg(html):
                nPos = 0
                phrase = 0

                html = html.decode('utf-8', 'ignore')
                reg = r'<li>(.*?)</li>'
                imgre = re.compile(reg)
                imglist = re.findall(imgre, html)

                if len(imglist) == 0:
                    result = "未收录"
                    return result
                for i in range(len(imglist)):
                    element = ''.join(imglist[i])
                    if element.count('. ') == 1:
                        nPos += 1
                    elif element.count('</a>') == 0 and phrase == 0:
                        nPos += 1
                        phrase += 1
                if nPos > 0:
                    result = ''
                    for c in range(nPos):
                        if c == 0:
                            s = ''
                        else:
                            s = '\n'
                        result = result + s + ''.join(imglist[c])
                    return result
                else:
                    return '查找失败'

            list_result.append(getImg(html) + '\n')

        item_result = '\n'.join(list_result)
        text_put.setPlainText(item_result)

    except:
        error = QErrorMessage(window)
        error.showMessage('查找错误')
