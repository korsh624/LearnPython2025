def accuracy_solution(real, predicted):
  count_true=0
  for i in range(len(real)):
    if real[i]==predicted[i]:
      count_true+=1
  res=count_true/len(real)
#   print(res)
  return round(res, 2)
real=[0,1,1,1,1,1,1,0,0,0,1,0,1,0]
predicted=[0,1,0,1,0,1,0,0,0,0,1,0,1,0]
print(accuracy_solution(real, predicted))