# creating a variable and storing the text
# that we want to search
search_text = "replaced"

# creating a variable and storing the text
# that we want to add
replace_text = "https://www.thiraisix.com/v/vijay/0211uns1635904977/720/fileSequence"

# Opening our text file in read only
# mode using the open() function
with open(r'video_name.m3u8', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text, replace_text)

# Opening our text file in write only
# mode to write the replaced content
with open(r'video_name.m3u8','w') as file:
	file.write(data)
print(" psText replaced")
