
import sys

dataFile = open('WBC.data','r').read()
dataDic = {i.split(',')[0]: i.split(',')[1:]  for i in dataFile.split('\n')} 

def funDataClean():

      bening = []
      malignant = []

      for i in dataDic:
            myline = dataDic[i]
            line10 = myline[9]
            if line10=="benign":
                  bening.append(myline)
            elif line10=="malignant":
                  malignant.append(myline)

      bening_summed = [0,0,0,0,0,0,0,0,0]
      bening_missed = [0,0,0,0,0,0,0,0,0]
      malignant_summed = [0,0,0,0,0,0,0,0,0]
      malignant_missed = [0,0,0,0,0,0,0,0,0]


      for say in range(9):
            for i in bening:
                  x = i[say]
                  if x=="?":
                        al = bening_missed[say]
                        al+=1
                        bening_missed[say]=al
                  else:
                        al = bening_summed[say]
                        integer_i = int(i[say])
                        al+=integer_i
                        bening_summed[say]=al

      for say in range(9):
            for i in malignant:
                  x = i[say]
                  if x=="?":
                        al = malignant_missed[say]
                        al+=1
                        malignant_missed[say]=al
                  else:
                        al = malignant_summed[say]
                        integer_i = int(i[say])
                        al+=integer_i
                        malignant_summed[say]=al

      count_malignant = len(malignant)
      count_bening = len(bening)
      missed_sum = 0
      missed_count = 0

      for i in range(9):
            for j in dataDic:
                  if dataDic[j][9] == "benign":
                        missed_value = round(bening_summed[i]/(count_bening-bening_missed[i]))
                        if (dataDic[j])[i]=="?":
                              myvalue = dataDic[j]
                              myvalue[i]=missed_value
                              dataDic[j]=myvalue
                              missed_count+=1
                              missed_sum = missed_sum + missed_value
                  elif dataDic[j][9] == "malignant":
                        missed_value = round(malignant_summed[i]/(count_malignant-malignant_missed[i]))
                        if (dataDic[j])[i]=="?":
                              myvalue = dataDic[j]
                              myvalue[i]=missed_value
                              dataDic[j]=myvalue
                              missed_count+=1
                              missed_sum = missed_sum + missed_value
      last_calculate = missed_sum/missed_count
      print("The average of all missing values is :",round(last_calculate,4))

def performStepWiseSearch():

      al  = sys.argv[1]
      bol = al.split(",")

      real_count_benign = 0
      real_count_malignant = 0

      for i in dataDic:
            val = dataDic[i]
            count_now = 0
            for j in range(9):

                  operator = bol[j]
                  if operator=="?":
                        count_now+=1

                  else:
                        real_val = (dataDic[i])[j]
                        real_val = int(real_val)
                        bol2 = operator.split(":")
                        part1 = bol2[0]
                        part2 = bol2[1]
                        part2 = int(part2)

                        if part1 == "<":
                              if real_val < part2:
                                    count_now+=1
                        elif part1 == "<=":
                              if real_val <= part2:
                                    count_now+=1
                        elif part1 == ">":
                              if real_val > part2:
                                    count_now+=1
                        elif part1 == ">=":
                              if real_val >= part2:
                                    count_now+=1
                        elif part1 == "!=":
                              if real_val != part2:
                                    count_now+=1
                        elif part1 == "=":
                              if real_val == part2:
                                    count_now+=1
            if(count_now==9 and val[9]== "benign"):
                  real_count_benign+=1
            elif(count_now==9 and val[9]=="malignant"):
                  real_count_malignant+=1

      if((real_count_benign+real_count_malignant)==0):
            rate=0
      else:
            rate = real_count_malignant/(real_count_malignant+real_count_benign)

      print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str(real_count_malignant) +
      '\nNegative (benign) cases               : ' + str(real_count_benign) +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format(rate) +
      '\n----------------------------------------------')

funDataClean()
performStepWiseSearch()
