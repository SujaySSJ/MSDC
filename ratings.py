import threading
import time


def entry_to_list(line):
	triplet_list=[]
	triplet_list=line.split('\t')
	triplet_list[2]=triplet_list[2].split('\n')[0]
	return triplet_list


# class mythread(threading.Thread):
# 	def __init__(self,id,name):
# 		threading.Thread.__init__(self)
# 		self.id=id
# 		self.name=name

# 	def run(self):
# 		count=100000
# 		while(True):
# 			# if(count%100==0):
# 			# 	time.sleep(2)
# 			print(self.name,count)
# 			count-=1


# thread1=mythread(1,"thread1")
# thread1.start()


# # thread2=mythread(2,"thread2")

# count =1000000
# while(count>0):
# 	print("main thread",count)
# 	count-=1

min_dict={}
max_dict={}

db_path="/home/makky/Desktop/Million-song-Dataset-challenge/project_data/db_150_indexed.txt"
new_db_path="/home/makky/Desktop/Million-song-Dataset-challenge/project_data/db_150_indexed_with_rating.txt"

class compute_thread(threading.Thread):
	def __init__(self,id,name):
		threading.Thread.__init__(self)
		self.id=id
		self.name=name
		

	def run(self):
		t_main=open(db_path,"r")
		t_new_main=open(new_db_path,"w+")
		count=12120030
		while(count>0):
			triplet=entry_to_list(t_main.readline())
			while(True):
				try:
					min_val=(int)(min_dict[triplet[0]])
					max_val=(int)(max_dict[triplet[0]])
					break
				except:
					continue
			rating=(5)/(max_val-min_val)*((int)(triplet[2])-max_val)+5
			t_new_main.write("{}\t{}\t{}\t{}\t\n".format(triplet[0],triplet[1],triplet[2],rating))
			print("Computer thread upto",count)
			count-=1

computer=compute_thread(1,"computer_thread")
computer.start()


main=open(db_path,"r")
count=12120030
def max(a,b):
	if(a>b):
		return a
	return b

def min(a,b):
	if(a<b):
		return a
	return b

triplet=entry_to_list(main.readline())
current_user=triplet[0]
min_playcount=1000000000000
max_playcount=-100000000000

while(count>0):
	triplet=entry_to_list(main.readline())
	if(triplet[0]!=current_user):
		min_dict[current_user]=min_playcount
		max_dict[current_user]=max_playcount
		min_playcount=1000000000000
		max_playcount=-100000000000
	current_user=triplet[0]
	min_playcount=min((int)(min_playcount),(int)(triplet[2]))	
	max_playcount=max((int)(max_playcount),(int)(triplet[2]))	
	print("main_thread upto",count)
	count-=1



# print(triplet)

# print(min_dict)
# print(max_dict)
# thread1.join()
computer.join()
print("main thread exit!")