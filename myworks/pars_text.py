from cgitb import html
import re
from lxml import etree
import lxml.html
import csv
import requests
dish = input('').replace(' ', '-')
url = f'https://tvoirecepty.ru/recept/{dish}'
print(url)
api = requests.get(url)
tree = lxml.html.document_fromstring(api.text)
text = tree.xpath(
    '//*[@class="ingredients-block recipe-list col-xs-12 col-sm-6 col-md-height col-full-height"]/div//*[@class="ingredient col-xs-12 nopadding margin-bottom-10 collapsed"]/text()')
# str_text = str_text.replace('\\n', '<br>')
print(text)
# final_output = final_output.replace(
#     '                                        ', '')
# final_output = final_output.replace(
#     'Вопросы, предложения и пожелания - пишите в комментариях, я с радостью всем отвечу.', '')

# print(final_output)
