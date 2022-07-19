# 1 write a program to read an entire the sample.txt file 

def to_read(file_name):
    f = open(file_name, mode='rt')
    print(f.read)
    f.close
    


# 2 write a program to read an first/last n line of the sample.txt file with n and first/last is an argument come from keyboard
def read_n_lines(n, file_name,first_or_last):
    g = open(file_name, mode='rt')
    lines = g.readlines
    if first_or_last == 'first':
        print(lines[n:])
    else:
        print(lines[-n:])
    g.close




# 3 write a program to read line by lines in sample.txt and store them in a list. Sort the list by length of each line
def read_file_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines.sort(key=len)
        for line in lines:
            print(line)


# 4 write a program to append a line to  the sample.txt file with line is the argument come from keyboard. Print the length of file 
# and the line with longest length 

def append_line(message,file_name):
    g = open(file_name, mode='wt')
    g.writelines(message)
    f = open(file_name, mode='rt')
    line = g.readlines()
    line.sort(key=len)
    print(line[-1])
        
# 5 write a program to count frequency of each word in sample.txt 
#def fre_word(a, file_name):
    #g = open(file_name, mode='rt')
    #f = g.readlines()
    #for x in f: 

def word_count(filename):
    word_count = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    print(word_count)    
    
    


# 6 write a program to remove a line which line number is an argument from the keyboard
def delete_line(n, file_name):
    with open(file_name, mode='r') as f:
        lines = f.readlines()
        after_delete = []
        for i, line in lines:
            if i != n: 
                after_delete.append(line)
                print(after_delete)
#------------


# 7 write a program to store the below content in the file name sample_w.txt 
'''
While CMR portrays extreme competency in capturing all data types, here are specific means through which it benefits your enterprise -

1. Automation Scope Expansion
CMR lets you leverage 85% of the untapped and unstructured data prevalent in your organization, imply'''
def store_mess(file_name):
    mess = '''While CMR portrays extreme competency in capturing all data types, here are specific means through which it benefits your enterprise -

1. Automation Scope Expansion
CMR lets you leverage 85% of the untapped and unstructured data prevalent in your organization, imply'''
    with open(file_name, mode='wt') as f: 
        f.writelines(mess)

