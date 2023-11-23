#OpenFile --> Operation -->CloseFile



file=open("Example.txt","w")

# file.write("Hello, world! \n")
# file.write("iProgrammer Solution Private Limited")

file.writelines(["Hello, world!" ,"\n"," Next line"])
# file.writelines("iProgrammer Solution Private Limited")



file.close()

