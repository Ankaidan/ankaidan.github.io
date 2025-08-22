#!/usr/bin/env python3

import csv
import random

RANGE_MIN=401
RANGE_MAX=600

JtoE=5
EtoJ=20
EW=5

Q_NUM=JtoE + EtoJ + EW

with open('./files/kamitango.tsv') as f:
  reader = csv.reader(f, delimiter='\t')
  data = [row for row  in reader] #素のデータ
  f.close()

with open('./files/kamitango.history') as f:
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

with open('./files/kamitango.history','a') as f:
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

output="\\section{\\blank に当てはまる適切な単語または表現を選択肢の中から一つ選びなさい。}\n"
for i in range(JtoE):
  pos=random.randint(0,3)
  answer=["{}","{}","{}","{}"]
  answer[pos]="{"+data[result_index[i]][1]+"}"
  output = output + "\\nJtoE{" + str(sum[i]) + "}{}" + "".join([str(m) for m in answer]) + "{" + str(pos+1) + "}\n"
  #\nJtoE{<番号>}{<受験者の解答>}{単語(rand)}{単語(rand)}{単語(rand)}{単語(rand)}{<正答>}
output+="\n\\section{下線部の単語または表現を和訳しなさい。}\n"
for i in range(JtoE,JtoE+EtoJ):
  output = output + "\\nEtoJ{" + str(sum[i]) + "}{}{}{}% " + data[result_index[i]][2] + "\n"
  #\nEtoJ{<番号>}{<受験者の解答>}{<T/F>}{<コメント>}% 正答

output+="\n\\section{次の各文の\\blank に最もよく当てはまる語または表現を答えなさい。}\n"
for i in range(JtoE+EtoJ,Q_NUM):
  output = output + "\\nEW{" + str(sum[i]) + "}{}{}{}% " + data[result_index[i]][1] + "\n"
  #\nEtoJ{<番号>}{<受験者の解答>}{<正誤>}{<コメント>}% 正答

filename = "./kamiwordtest" +str(NO)+ ".tex"


file_q = "\\documentclass[a4paper]{ltjsarticle}\n\\usepackage{./files/newwordtest}\n\\usepackage[margin=15mm]{geometry}\n\\usepackage{luatexja-ruby}\n% \\renewcommand{\\anscolor}{red}\n\\pagestyle{empty}\n\\begin{document}\n\\leftskip=1em\n\\TitleHead{"
file_q += str(NO)
file_q += "}\n\n" + output +"\\addtocounter{correct}{-1}\n\\refstepcounter{correct}{\\label{count:score}}\n\\end{document}"

with open (filename,"w") as f:
  f.write(file_q)
  f.close()