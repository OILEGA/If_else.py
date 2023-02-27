print("Kindly enter your monthly scores in ALX: \n")

month0 = int(input("Your score for month 0 is: \n"))
month1 = int(input("Your score for month 1 is: \n"))
month2 = int(input("Your score for month 2 is: \n"))

sum =(month0 + month1 +month2)
avg = ((month0 + month1 + month2)/3)
print("Your total sum is: \n", sum)
print("Your average score is: \n", avg)

if avg >= 1 and avg <= 50:
  print("\033[35m" "Very Poor, Go back home and learn how to cook\n")
elif avg >= 51 and avg <= 79:
  print("\033[38m" "You are a failure, You can never make it in ALX")
elif avg >= 80 and avg <= 120:
  print("\033[32m" "You are doing well. Keep it up")
elif avg >= 121 and avg <= 175:
  print("\033[33m" "I hope you are not copying from someone's github?")
  feedback = input("feedback: \n")
  if feedback == 'Yes':
    print("\033[039m""Repent and Learn")
  elif feedback == 'No':
    print("\033[32m" "You are doing very well")
elif avg >= 176 and avg <= 200:
  print("\033[34m" "ALX is coming to investigate you")
elif avg < 1 and avg > 200:
   print("\033[32m" "wrong input\n")
  


