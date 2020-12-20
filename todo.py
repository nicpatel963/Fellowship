import sys,os 
from datetime import date 

cur_dir=os.getcwd()
todo_txt=open(cur_dir+"\\todo.txt","a")
done_txt=open(cur_dir+"\\done.txt","a")
usr_input=sys.argv[1:]

todo_txt.close()
done_txt.close()

def print_report():
	with open(cur_dir+"\\todo.txt","r") as todo_txt:
		todo_list = [line.strip() for line in todo_txt]

	with open(cur_dir+"\\done.txt","r") as todo_txt:
		done_list = [line.strip() for line in todo_txt]
	
	print(str(date.today())+" Pending : {0} Completed : {1}".format(len(todo_list),len(done_list)))

def print_ls():
	with open(cur_dir+"\\todo.txt","r") as todo_txt:
		todo_list = [line.strip() for line in todo_txt]

	todo_list=todo_list[::-1]
	count=len(todo_list)
	if count == 0:
		print("There are no pending todos!")
	else:		
		for i in range(count):
			print("[{0}] {1}".format(str(count),todo_list[i]))
			count-=1

def delete_todo():

	if len(usr_input) <2:
		print("Error: Missing NUMBER for deleting todo.")
	else:
		index=int(usr_input[1])
		if not index or index<=0:
			print("Error: todo #{0} does not exist. Nothing deleted.".format(index))
		else:

			with open(cur_dir+"\\todo.txt","r") as todo_txt:
				todo_list = [line.strip() for line in todo_txt]
			if index > len(todo_list):
				print("Error: todo #{0} does not exist. Nothing deleted.".format(index))
			else:
				todo_list.pop(index-1)
				print("Deleted todo #"+str(index))
			with open(cur_dir+"\\todo.txt","w") as todo_txt:
				for i in todo_list:
					todo_txt.write(i+'\n')
		
def print_usage():
	print("Usage :-")
	print("$ ./todo add \"todo item\"  # add new todo")
	print('$ ./todo ls               # show remaining todo')
	print('$ ./todo del NUMBER       # Delete a todo')
	print('$ ./todo done NUMBER      # Complete a todo')
	print('$ ./todo help             # Show usage')
	print('$ ./todo report           # Statastics')


def add_todo():
	if len(usr_input) != 2:
		print("Error: Missing todo string. Nothing added!")
	else:
		with open(cur_dir+"\\todo.txt","a") as todo_txt:
			todo_txt.write(usr_input[1].strip()+'\n')
		print('Added todo: "{0}"'.format(usr_input[1]))	

def done_todo():
	if len(usr_input)<2:
		print("Error: Missing NUMBER for marking todo as done.")
	else:
		index=int(usr_input[1])
		with open(cur_dir+"\\todo.txt","r") as todo_txt:
			todo_list = [line.strip() for line in todo_txt]
		
		if index > len(todo_list) or index ==0:
			print("Error: todo #{0} does not exist.".format(index))
		else:
			todo_to_done=todo_list.pop(index-1)
			print("Marked todo #{0} as done.".format(index))

			with open(cur_dir+"\\todo.txt","w") as todo_txt:
				for i in todo_list:
					todo_txt.write(i.strip()+'\n')
			
			with open(cur_dir+"\\done.txt","a") as done_txt:
				done_txt.write("x "+ str(date.today())+' '+todo_to_done+'\n')



if __name__=="__main__":
	if not usr_input or usr_input[0]=="help":
		print_usage()
	elif usr_input[0]=="report":
		print_report()
	elif usr_input[0]=="add":
		add_todo()
	elif usr_input[0]=="ls":
		print_ls()
	elif usr_input[0]=="del":
		delete_todo()
	elif usr_input[0]=="done":
		done_todo()
	