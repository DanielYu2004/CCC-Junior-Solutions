#7/15 points, i keep getting runtime error on J5 questions

smallest_level = 0

class Node:
	def __init__(self, val, arr = []):
		self.val = val
		self.pages = arr
		self.level = None

	def traversal(self):
		if self.pages == []:
			global smallest_level
			if self.level < smallest_level:
				smallest_level = self.level
				#print(self.level)
			elif smallest_level == 0:
				smallest_level = self.level
		#else: 
		for i in range(len(self.pages)):
			#print(self.val, "<" ,(book[int(self.pages[i])-1]).val)

			if book[int(self.pages[i])-1] not in checked:
				#print(self.val, " ", self.level)
				#print("A")
				book[int(self.pages[i])-1].level = int(self.level) + 1
				checked.append(book[int(self.pages[i])-1])
				#print(book[int(self.pages[i])-1].val)
				book[int(self.pages[i])-1].traversal()
			elif int(self.level) + 1 < int((book[int(self.pages[i])-1]).level):
				#print("B")

				#print(self.level, "<" ,int((book[int(self.pages[i])-1]).level))
				book[int(self.pages[i])-1].level = int(self.level) + 1
				#print(book[int(self.pages[i])-1].val)
				book[int(self.pages[i])-1].traversal()

length = len

pages = int(input())
book = []
checked = []
#check input 
for i in range(pages):
	temp = input().split()
	temp_con = []	
	for q in range(length(temp)-1):
		temp_con.append(temp[q+1])
	book.append(Node(i+1, temp_con))
	#print(book[i].print())

book[0].level = 1
checked.append(book[0])
book[0].traversal()



if len(checked) == pages:
  print("Y")
else:
  print("N")

print(smallest_level)