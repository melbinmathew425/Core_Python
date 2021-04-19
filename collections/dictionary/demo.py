#dictionary
#values store in dictionary as a key value pairs

student={"rollno":1001,"name":"melbin","age":25}
print(student)

#its support hetrogenious values

student={"rollno":1001,"name":"melbin","age":25,"age":30,"mark":30}
print(student)
#its support only duplicate valuse not in case of key


print(student["age"])#print a value using corresponding key

student["name"]="ambi"#dictionary is muttable,it we can update the valuse
student['mark']+=10
del student["mark"]#deletion of a key
print(student)
