
file_path="project_data/train_triplets.txt"
max_song_file="project_data/max_song_file.txt"
all_details_file="project_data/all_details.txt"


def entry_to_list(line):
	triplet_list=[]
	triplet_list=line.split('\t')
	return triplet_list


def maximum(a,b):
	if(a>b):
		return a
	return b


# def make_db_short_per(thread_name,percentage,file_name):
# 	print("{} is online".format(thread_name))
# 	temp_count=48373587
# 	temp_string=""
# 	current_user=""
# 	current_song_count=0
# 	previous_user=""
# 	final_db=""
# 	triplet=[]
# 	with open(file_path,"r") as fp:
# 		line=fp.readline()
# 		triplet=entry_to_list
# 		current_song_count=1
# 		previous_user=triplet[0]
# 		current_user=triplet[0]
# 	while(temp_count > 0):
# 		with open(file_path,"r") as fp:
# 			line=fp.readline()
# 			triplet=entry_to_list(line)
# 			temp_string+=line
# 			if(previous_user==current_user)
# 				current_song_count+=1
# 			else:
# 				if(current_song_count>=((4400*percentage)/100))
# 					final_db+=temp_string
# 				else temp_string=""
# 				current_song_count=1
# 				previous_user=current_user
# 		temp_count-=1
# 	current_file_ptr=open(file_name,"w")
# 	current_file_ptr.write(final_db)
# 	current_file_ptr.close()





def max_song_count():
	count=0
	current_song_count=0
	max=-1
	max_user=""
	current_user=""
	previous_user=""
	temp_count=48373587
	all_ptr=open(all_details_file,"a")
	with open(file_path) as fp:

		line=fp.readline()
		triplet=entry_to_list(line)
		previous_user=triplet[0]
		current_user=triplet[0]
		current_song_count=1

		while(temp_count>0):
			line=fp.readline()
			triplet=entry_to_list(line)
			current_user=triplet[0]
			if(previous_user==current_user):
				current_song_count=current_song_count+1
			else:
				all_ptr.write("user:{} \t song-count:{} \n".format(previous_user,current_song_count))
				max=maximum(max,current_song_count)
				if(max==current_song_count):
					max_user=previous_user
				current_song_count=1
				previous_user=current_user
			count+=1
			print(count)
			temp_count-=1
	print("Maximum song count :{} & Corresponding User:{}".format(max,max_user))
	max_song_file_pointer=open(max_song_file,"w")
	max_song_file_pointer.write("Maximum song count :{} & Corresponding User:{}".format(max,max_user))
	max_song_file_pointer.close()

def main_function():
	max_song_count()
		

main_function()
	
