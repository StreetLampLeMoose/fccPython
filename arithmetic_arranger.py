def arithmetic_arranger1(problems):
    if errorHandling(problems) != 0:
      print(errorHandling(problems))
      quit()
    problemList = dataCleaner(problems)
    answerList = answers(problemList)
    lineList = arranger(problemList,answerList)
    return lineList

def dataCleaner (problems):
  cleanedData = []
  i=0
  for x in problems:
    cleanedData.append(x.split())
    i +=1
  return cleanedData

def answers(problems):
  i=0
  answerList = []
  for x in problems: 
    firstNumber =  float(problems[i][0])
    secondNumber = float(problems[i][2])
    if problems[i][1] =='+':
      answer = firstNumber + secondNumber
    elif problems[i][1] == '-':
      answer = firstNumber - secondNumber
    answerList.append(answer)
    i+=1
  return answerList

def arranger(problems,answers):
  line1 = []
  line2 = []
  line3 = []
  line4 = []
  i = 0
  for x in problems :
    line1String = ""
    line2StringHead = ""
    line2StringTail = ""
    line2String = ""
    line3String = ""
    line4String = ""
    answerString = str(answers[i])
    gridSize = max(len(x[0]), len(x[2]) +2 , len(answerString))
    line1String = line1String+ x[0] 
    line2StringHead = line2StringHead + x[1]
    line2StringTail = line2StringTail+ x[2]
    line4String = line4String + answerString
    while len(line1String) < gridSize :
      line1String = " " + line1String
    while len(line2StringHead) + len(line2StringTail) < gridSize :
      line2StringHead = line2StringHead + " "
    line2String = line2StringHead + line2StringTail
    while len(line3String) < gridSize : 
      line3String = line3String+ "-"
    while len(line4String) < gridSize :
      line4String = " " + line4String
    line1.append(line1String)
    line2.append(line2String)
    line3.append(line3String)
    line4.append(line4String)
    i+= 1
  return [line1, line2, line3,line4]

def errorHandling(problems):
    if len(problems) > 5 :
      return("Error: Too many problems")
    cleanedData = dataCleaner(problems)
    for x in cleanedData : 
      if len(x[0]) > 4 or len(x[2]) > 4:
        return("Error: numbers cannot be greater than 4 digits")
        
      if x[1] != "+" and x[1] != "-":
        return ("Error: Operator must be '+' or '-'")
      if x[0].isdigit() == True and x[2].isdigit() == True:
        continue
      else: 
        return("Error:Numbers must only contain digits")
    return 0


