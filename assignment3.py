#read text file (a question)
f = open("question.txt","r+")
question = f.read()
#print(question)
#use text question as the prompt for input function
answer = input(question + "\n")
#print(answer)
#write the user's answer back to the text file
f.write("\n" + answer)
f.close()
