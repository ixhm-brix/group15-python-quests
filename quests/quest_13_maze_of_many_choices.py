def grade_score():
      user_score=int(input('Enter your score(0-100): '))
      if user_score >=90:
          print('A')
      elif user_score >=80 and user_score <=89:
          print('B')
      elif user_score >=70 and user_score <=79:
          print('C')
      else:
          print('Needs improvement!')
grade_score()
 
    
