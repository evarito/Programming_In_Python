# Program to check whether a set is a subset of another set

set_1 = {"mogadishu","marsabit","kuwait","dandora","dandora"}
set_2 = {"marsabit","kuwait","tripoli"}

is_subset = set_2 <= set_1

if is_subset:
    print("Set_2 is a subset of Set_1")
else:
    print("NO SUBSET FOUND")    

print(set_1) # demonstrates sets don't accept dupliates