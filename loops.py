#list - data structure which can hold multiple values of multiple types.
#array - data structure which can hold multiple values of same types.

list_of_team_members = ["Abhishek","Ankit","Ankita","Anamika"]

#print the list
print(list_of_team_members)

#add a new team_members (append is use to add in last of the list)
list_of_team_members.append("Anjali")

#print the list
print(list_of_team_members)

#if we want to add anything at specific number then we need to use insert , number start with 0,1,2.
list_of_team_members.insert(1,"Anil")

print(list_of_team_members)

#how to print length of list
print(len(list_of_team_members))

#iteration of list
for team_members in list_of_team_members:
    print(team_members)