import re

def append_answer(script,ans):
	
	qnum = re.findall('\d\d\d',str(script))
	qnum = int(qnum[0])
	filename = 'C:\\Users\\Dibyanshu\\Desktop\\Project Euler\\Euler solutions\\project_euler_answers.txt'
	with open(filename,'a') as f:
		f.write("\n")
		f.write(str(qnum)+". "+str(ans))
		f.write("\n")
		f.write("*"*20)

if __name__ == "__main__":
	append_answer(script,ans)