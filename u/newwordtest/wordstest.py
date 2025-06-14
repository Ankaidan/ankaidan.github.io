#!/usr/bin/python3

import csv
import random

RANGE_MIN=1
RANGE_MAX=900

JtoE=5
EtoJ=20
EW=5

Q_NUM=JtoE + EtoJ+EW

with open('./data/kamitango.tsv') as f:
  reader = csv.reader(f, delimiter='\t')
  data = [row for row  in reader] #素のデータ
  f.close()

with open('./data/kamitango.history') as f:
  reader = csv.reader(f)
  sum_base = [row for row in reader]
  sum_base = sum(sum_base, [])# 二次元 -> 一次元
  sum_base = [int(s) for s in sum_base]# 整数に #過去に出した番号
  f.close()

NO = int(len(sum_base)/30+1)

sum=[] #今回の出題番号

for i in range(Q_NUM):
  IfFound = False
  while IfFound == False:
    num = random.randint(RANGE_MIN,RANGE_MAX)
    C = num in sum_base
    if C == False:
      IfFound=True
  sum.append(num) 
  sum_base.append(num)

with open('./data/System_words.history','a') as f:
  for i in range(Q_NUM):
    f.write(str(sum[i]))
    f.write("\n")
  f.close()

result_index=[0]*(Q_NUM) 
for j in range(Q_NUM):
  for k in data:
    if str(sum[j]) in k:
      result_index[j] = data.index(k) #今回の出題番号の素データ上での位置
      break

output="\\section{\\blank に当てはまる適切な単語または表現を選択肢の中から一つ選びなさい。}\n" #編集放棄
for i in range(JtoE):
  pos=random.randint(0,3)
  answer=["{}","{}","{}","{}"]
  answer[pos]="{"+data[result_index[i]][1]+"}"
  output = output + "\\JtoE{}{ " + data[result_index[i]][2] + " }" + "".join([str(m) for m in answer]) + "{" + str(pos+1) + "}{}{" + str(sum[i]) + "}\n"

output+="\n\\section{下線部の単語または表現を和訳しなさい。}\n" #ここから編集再開 2025/6/4/17:54
for i in range(JtoE,JtoE+EtoJ):
  output = output + "\\EtoJ{  " + data[result_index[i]][1] + "  }{  " + data[result_index[i]][2] + "  }{" + str(sum[i]) + "}\n"

output+="\n\\section{次の各文の\\blank に最もよく当てはまる語または表現を答えなさい。}\n"
for i in range(JtoE+EtoJ,Q_NUM):
  output = output + "\\EW{}{  " + data[result_index[i]][2] + "  }{" + data[result_index[i]][1] + "}{" + str(sum[i]) + "}\n"

filename = "./wordstest" +str(NO)+ ".tex"


file_q = "\\documentclass[a4paper]{ltjsarticle}\n\\usepackage{./files/mywordstest}\n\\usepackage[margin=15mm]{geometry}\n\\usepackage{luatexja-ruby}\n% \\renewcommand{\\anscolor}{red}\n\\pagestyle{empty}\n\\begin{document}\n\\leftskip=1em\n\\TitleHead{"
file_q += str(NO)
file_q += "}\n\n" + output +"\n{\\color{\\anscolor} 大問2の和訳がほしい方は気軽にお申し付けください}\n\\addtocounter{correct}{-1}\n\\refstepcounter{correct}{\\label{count:score}}\n\\end{document}"

with open (filename,"w") as f:
  f.write(file_q)
  f.close()