file_read = open("README.md")

file_write = open("README_copy.md", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
