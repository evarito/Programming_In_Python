# A program that merges different dictionanries to form one new dictonary 

dict_a = {'F_name': "Eve", 'L_name': "Lubanga"}
dict_b = {'School': "WoodCreek", 'Staff_No': 154889}
dict_c = {'Department': "ICT", 'Supervisor': None}
dict_d = {}

for d in (dict_a,dict_b,dict_c):
  dict_d.update(d)
print(dict_d)
