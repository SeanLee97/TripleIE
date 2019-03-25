from docx import Document
from docx.shared import Inches

from utils.common import getQuestions

questions = getQuestions('data/question.txt')

doc = Document()  # doc对象
for (i, question) in enumerate(questions):
    if i > 2:
        break
    string = question
    images = 'images/%s.png' % i  # 保存在本地的图片
    doc.add_paragraph(string)  # 添加文字
    doc.add_picture(images, width=Inches(10))  # 添加图, 设置宽度

doc.save('output/output.docx')  # 保存路径
