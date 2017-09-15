#CSV

import random

csv_file = open("occupations.csv", 'r')
csv_lines = csv_file.readlines()

#basic unweighted job output
def gimmie_job():
    #line makes it so that a random line is chosen
    random_line = csv_lines[random.randint(1, len(csv_lines)-2)]

    #This block deals with commas and splicing
    if random_line.find('''",''') == -1:
        random_job = random_line.split(",")[0]
        percentage = random_line.split(",")[1]

    else:
        random_job = random_line.split('''",''')[0][1:]
        percentage = random_line.split('''",''')[1]

    print "---------------------------------------"
    print random_line
    print random_job
    print percentage
    print "---------------------------------------"



#testing program
def run():
    for x in range(0,10):
         gimmie_job()


run()        
