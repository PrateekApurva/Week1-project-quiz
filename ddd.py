print("Welcome to today's Quiz on GK for 7th class students")
print("Instructions:"
      "1.You have to write your chosen option's alphabet(in capital) just after the question.For example if your choice is'A' option then write A then press the enter key.\n"
      "2.Once you enter your response than next question will appear and you will have no chance to go back to previous question, so enter your answer only when you become sure of it.\n"
      "3.This quiz consists of 10 questions ,total marks=40; 4 for correct; -1 for incorrect;0 for not attempted ones.\n"
      "4.If you do not wish to attemp the question ,then enter 'E' and you will then move to next question\n.",
      "5.Note:If you enter any other character other than 'A','B','C','D','E' then that answer will not be evaluated and considered as UNATTEMPTED." )
print("Enter your name to start the Quiz")
name=input()
print("Q.1. Which orgon performs blood purification in the human body?\n",
     " A.Heart        B.Lungs       C.Kidney      D.Liver")
ans1=input()
print("Q.2. The preserved remains of one's lived organisms are called as:\n"
      "A.Diamond      B.Fossils     C.Coal        D.Sediments")
ans2=input()
print("Q.3. The food or chemical energy source made by plants during photosynthesis is called:\n"
      "A.Glucose      B.Vitamin     C.Magnesium   D.Fatty acids")
ans3=input()
print("Q.4. What is the capital city of France?\n"
      "A.Newyork      B.Paris       C.London      D.Amsterdan")
ans4=input()
print("Q.5. Char Minar is located in which city?\n"
      "A.Hyderabad    B.New Delhi   C.Jodhpur     D.Bengaluru")
ans5=input()
print("Q.6. Which continent has highest population density?\n"
      "A.Africa       B.Asia        C.North America  D.Europe")
ans6=input()
print("Q.7. Which state of India has the longest coastline?\n"
      "A.Andhra Pradesh B.Tamilnadu  C.West Bengal  D.Gujarat")
ans7=input()
print("Q.8. Who was the first Indian to climb Mt. Everet?\n"
      "A.Rakesh Sharma  B.Bachendri Pal  C.Sonam Wangchuk  D.Deoli Shah")
ans8=input()
print("Q.9. Whhat is the longest river of the world?\n"
      "A.Amazon      B.Tsangpo       C.Mekong    D.Nile")
ans9=input()
print("Q.10. What is the main cause of Goitre?\n"
      "A.Iron deficiency  B.Fugal infection  C.Bacterial infection  D.Alergic reaction")
ans10=input()
ans1a=ans1.endswith("C")
ans2a=ans2.endswith("B")
ans3a=ans3.endswith("A")
ans4a=ans4.endswith("B")
ans5a=ans5.endswith("A")
ans6a=ans6.endswith("B")
ans7a=ans7.endswith("D")
ans8a=ans8.endswith("B")
ans9a=ans9.endswith("D")
ans10a=ans10.endswith("A")
corr=ans1a,ans2a,ans3a,ans4a,ans5a,ans6a,ans7a,ans8a,ans9a,ans10a
corr1a=str(corr)
corr1=4*corr1a.count("True")
ans1b=ans1.endswith("A")
ans2b=ans2.endswith("A")
ans3b=ans3.endswith("B")
ans4b=ans4.endswith("A")
ans5b=ans5.endswith("B")
ans6b=ans6.endswith("A")
ans7b=ans7.endswith("A")
ans8b=ans8.endswith("A")
ans9b=ans9.endswith("A")
ans10b=ans10.endswith("B")
incorr=ans1b,ans2b,ans3b,ans4b,ans5b,ans6b,ans7b,ans8b,ans9b,ans10b
incorra1=str(incorr)
incorra=incorra1.count("True")
ans1c=ans1.endswith("B")
ans2c=ans2.endswith("C")
ans3c=ans3.endswith("C")
ans4c=ans4.endswith("C")
ans5c=ans5.endswith("C")
ans6c=ans6.endswith("C")
ans7c=ans7.endswith("B")
ans8c=ans8.endswith("C")
ans9c=ans9.endswith("B")
ans10c=ans10.endswith("C")
incorr1=ans1c,ans2c,ans3c,ans4c,ans5c,ans6c,ans7c,ans8c,ans9c,ans10c
incorrb1=str(incorr1)
incorrb=incorrb1.count("True")
ans1d=ans1.endswith("D")
ans2d=ans2.endswith("D")
ans3d=ans3.endswith("D")
ans4d=ans4.endswith("D")
ans5d=ans5.endswith("D")
ans6d=ans6.endswith("D")
ans7d=ans7.endswith("C")
ans8d=ans8.endswith("D")
ans9d=ans9.endswith("C")
ans10d=ans10.endswith("D")
incorr2=ans1d,ans2d,ans3d,ans4d,ans5d,ans6d,ans7d,ans8d,ans9d,ans10d
incorrc1=str(incorr2)
incorrc=incorrc1.count("True")
marks=corr1-incorra-incorrb-incorrc
print(name,end="'s ")
print("SCORE IS ",end=" ")
print(marks)
print("OUT OF 40.")
print("Thank you for giving Quiz to all by PRATEEK APURVA")
"""print(corr1,incorra,incorrb,incorrc)
print(corr)
corr2=str(corr)
print(corr2.count("True"))
#print(corr)"""