import sys

#sys.argv[1] is the first cl argument

user_file_path=sys.argv[1]

num_users=sys.argv[2]

main_db_path="project_data/train_triplets.txt"

new_file="project_data/new_db_"+num_users+".txt"


def entry_to_list(line):
	triplet_list=[]
	triplet_list=line.split('\t')
	return triplet_list



def user_entry_to_list(line):

	triplet=[]
	triplet=line.split(',')
	triplet[1]=triplet[1].strip(" ")
	return triplet



def main_function():

	main_db_tup_count=48373587
	progress_count=0

	user_file_ptr=open(user_file_path)
	main_file_path=open(main_db_path)
	new_file_ptr=open(new_file,"w+")

	user_list=user_entry_to_list(user_file_ptr.readline())
	main_list=entry_to_list(main_file_path.readline())

	choose_next=False
	progress_count+=1
	while(main_db_tup_count>0):
		if(main_list[0]==user_list[1]):
			new_file_ptr.write("{}\t{}\t{}\r".format(main_list[0],main_list[1],main_list[2]))
			main_list=entry_to_list(main_file_path.readline())
			choose_next=True
		else:
			if(choose_next==False):
				main_list=entry_to_list(main_file_path.readline())
			else:
				user_list=user_entry_to_list(user_file_ptr.readline())
				choose_next=False
		main_db_tup_count-=1
		progress_count+=1
		print(progress_count)





main_function()	
