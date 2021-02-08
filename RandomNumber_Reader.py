import sys
import matplotlib.pyplot as plt
#reading the file created by Random_python.py as readonly
file_random = open("randomnumbers_to_asci.txt","r")
#reading and printing type of data for debuging
#random_numbers_data = file_random.read()
#print (type(random_numbers_data))

#created the empty list to fill the random number data
#from .txt file
random_list=[]
#reading text line by line
for line in file_random:
    #normally there is /n at the end of the line
    #following code will strip the end of the line
    line =line.strip()
    #print(repr(line))
    #changing the string to float
    random = float(line)

    #print(random)
    #filling the random numbers into a list
    random_list.append(random)
#checking if the numbers are stored correctly
#print(random_list)
#creating the histograms
n, bins, patches = plt.hist(random_list, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Generated Random Number')
plt.grid(True)
#plt.show()
print("saving histograms to file plt.png")
plt.savefig("plot.png")
