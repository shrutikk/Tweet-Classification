from preprocess import get_text,english,parse,valid,Tokenizer
import re

politics =[]
sports =[]
technology =[]
finance =[]
entertainment = []


dataset = []
target = []


f = open('politicsnews', 'rU')
for line in f:
    line = re.sub(r'https?:\/\/[^\t ]*', '', line)
    politics.append(line)      

f = open('sportsnews', 'rU')
for line in f:
    line = re.sub(r'https?:\/\/[^\t ]*', '', line)
    sports.append(line)       

f = open('technologynews', 'rU')
for line in f:
    line = re.sub(r'https?:\/\/[^\t ]*', '', line)
    technology.append(line)       

f = open('entertainmentnews', 'rU')
for line in f:
    line = re.sub(r'https?:\/\/[^\t ]*', '', line)
    entertainment.append(line)       

f = open('financenews', 'rU')
for line in f:
    line = re.sub(r'https?:\/\/[^\t ]*', '', line)
    finance.append(line)       


for tweet in politics:
    target.append(0)

for tweet in sports:
    target.append(1)

for tweet in technology:
    target.append(2)

for tweet in entertainment:
    target.append(3)

for tweet in finance:
    target.append(4)


dataset = politics + sports +technology + entertainment + finance
