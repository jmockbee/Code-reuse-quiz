def format_name(first_name, last_name):
	if first_name=='' and last_name != '':
        return "Name: "+last_name
    elif last_name =='' and first_name !='':
        return "Name: "+first_name
    elif first_name=='' and last_name == '':
        return ''
    else:
        return 'Name: '+ last_name+', '+ first_name    
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string