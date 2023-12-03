
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(x):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for ch in punctuation_chars:
        x=x.replace(ch,"")
    return x
print(strip_punctuation("#incredible"))              
#calculating how many words in the string are considered positive words
def get_pos(x):
    line1 = strip_punctuation(x)
    line2 = line1.lower()
    line=line2.split() 
    count = 0
    for word in line:
        if word in positive_words:
            count = count + 1      
    return count           

#calculating how many words in the string are considered negative words
def get_neg(x):
    line1 = strip_punctuation(x)
    line2 = line1.lower()
    line=line2.split() 
    count = 0
    for word in line:
        if word in negative_words:
             count = count + 1      
    return count

#Creaing  new csv file and importing data
csv_file = open("resulting_data.csv", "w")
csv_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
csv_file.write('\n')


#reading old file and importing data to new file
old_file1 = open("project_twitter_data.csv", "r")
old_file = old_file1.readlines()
header = old_file[0]
field_names = header.strip().split(',')
print(field_names)

for row in old_file[1:]:
    vals = row.strip().split(',')   
    retweet_count =  int(vals[1])
    reply_count = int(vals[2])
    positive_score =  get_pos(vals[0])
    negative_score =  get_neg(vals[0])
    net_score = positive_score - negative_score
    lst = [retweet_count,reply_count,positive_score,negative_score,net_score]
    line = '{},{},{},{},{}'.format(lst[0],lst[1],lst[2],lst[3],lst[4])               
    #importing information from old file to new file
    csv_file.write(line)
    csv_file.write('\n')
#closing new file
csv_file.close()
