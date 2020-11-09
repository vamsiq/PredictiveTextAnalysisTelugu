import sqlite3
conn = sqlite3.connect('AA_db.sqlite')
cur = conn.cursor()
class Rama:
    h = ''

    def __init__(self):
        h = 'rama'

    def compute(self):

        # print("rama")
        cur.execute('SELECT value FROM run')
        f = cur.fetchall()
        # print(f)

        file = open("telugu.txt", "r", encoding="utf-8")
        s = file.read()  # for reading file
        s = re.sub(r'[//.]', '. ', s)  # for replacing . with .
        s = re.sub(r'[\n]', ' ', s)  # for replacing new line with space
        s = re.sub(r'[\u200c]', '', s)  # for replacing . with space
        s = re.sub(r'[\u200b]', '', s)  # for replacing . with space
        s = re.sub(r'[\u2028]', '', s)  # for replacing . with space
        s = re.sub(r'[?]', '. ', s)  # for replacing ? with .
        s = re.sub(r'[//,]', ' ', s)  # for replacing , with space
        tag = 1
        d_count = 0
        ent_count = 0

        # sentence tokenization
        sentences = sent_tokenize(s);
        # print("step 1 -> sentense tokenization")
        # print("no of sentences  ", len(sentences))
        # print(sentences)

        two_array = []  # for storing two continous words
        next_possible_occurence = {}  # a dictionary which has word as a key and next possible words set as value
        for sen in sentences:  # reading every sentence
            sen = re.sub(r'[//.]', ' ', sen)  # as word tokenizer considers . as a word we replace it with space
            words = word_tokenize(sen)  # converting sentecne in to words
            v = len(words)
            for j in range(v - 1):
                if (j < v - 1):
                    two_array.append(words[j] + "_" + words[j + 1])

                if (words[j] in next_possible_occurence):

                    sm = next_possible_occurence[str(words[j])]
                    sm |= {str(words[j + 1])}
                    next_possible_occurence[str(words[j])] = sm;


                else:
                    st = {str(words[j + 1])}
                    next_possible_occurence[str(words[j])] = st;




        for one in next_possible_occurence:
            cat=next_possible_occurence[one]
            fan=""
            pen=list(cat)
            for a in pen:
                if(fan==""):
                    fan=a;
                else:
                    fan=fan+"&"+a
            sql = "insert into npw values(?,?)"
            val = (one, fan)
            # print(one)
            cur.execute(sql,val)

        conn.commit()
        # print("\n" * 2)
        # print("step-2 -> joining two words of sentences")
        # # print(two_array)
        # print("\n" * 2)
        # print("step-3 ->  possible chances of all words")


#for counting words
        tokens = [token for token in s.split(" ") if token != ""]
        for tok in tokens:

            sql = "select count from wordcount WHERE word='" + tok + "'"
            cur.execute(sql)
            k = cur.fetchall()

            tag = 0;
            for u in k:
                t = list(u)
                for y in t:
                    co = y
                    tag = 1;
            if (tag == 0):
                sql = "insert into wordcount values(?,?)"
                val = (tok, 1)
                cur.execute(sql, val)

            else:
                co = co + 1
                co = str(co)
                sql = "UPDATE wordcount SET count =" + co + " WHERE word='" + tok + "'"
                cur.execute(sql)

            conn.commit()



        ###


    ###







        for k in two_array:
            sql = "select count from twc WHERE two_words='" + k + "'"
            cur.execute(sql)
            result = cur.fetchall()

            tag = 0;
            for u in result:
                t = list(u)
                for y in t:
                    co = y
                    tag = 1;
            if (tag == 0):
                sql = "insert into twc values(?,?)"
                val = (k, 1)
                cur.execute(sql, val)

            else:
                co = co + 1
                co = str(co)
                sql = "UPDATE twc SET count =" + co + " WHERE two_words='" + k + "'"
                cur.execute(sql)

            conn.commit()






        sql = "select * from npw"
        cur.execute(sql)
        k = cur.fetchall()
        for u in k:
            t = list(u)
            print(t)
            temp1=t[0]
            temp2=t[1]
            data = temp2.split("&")
            print(data)
            co1=0
            co2=0
            for d in data:
             fresh=temp1+"_"+d
             sql="select count from twc where two_words='"+fresh+"'"
             cur.execute(sql)
             res=cur.fetchall()

             for u in res:
                t = list(u)
                for ok in t:
                    co1=ok

             sql = "select count from wordcount where word='" + temp1 + "'"
             cur.execute(sql)
             res2 = cur.fetchall()
             for u in res2:
                t = list(u)
                for ok in t:
                 co2 = ok

             print("co1 "+str(co1)+" co2 "+str(co2))
             pp=(co1)/(co2)

             sql="insert into probability values(?,?)"
             val=(fresh,pp)
             cur.execute(sql,val)
             conn.commit()




        print("hey rama here")

from tkinter import *
from nltk.tokenize import *

root = Tk()
root.title("Text Editor in Telugu")

print("hai")
wo="done"

sql="select val from run where first='"+wo+"'"
cur.execute(sql)
f = cur.fetchall()
print(f)
for k in f:
    m=list(k)
    for l in m:
        if(l==0):
            print("hai")
            c=Rama()
            c.compute()

        else:
            print("hooooo")
            






frame = Frame(root, width=200, height=300)


text2 = Text(frame, height=15, width=200,font=("Mallanna",14))

# for setting scroll bar in frame
text2.grid(column=0,row=0)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)



text2.insert(INSERT,"Hello Welcome to text editor in Telugu\n suggested will appear in orange color\n Press Tab to keep the suggested word\n press any key in keyboard to remove it.\n Press Enter to start using it. ",'instructions') # for setting initial instructions
text2.tag_configure('instructions', foreground='#ff0000') #  setting color for text
text2.tag_configure('predict', foreground='#c63f17') #  setting color for predicted text

text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)



# handling  key events
d_count=0
tag=0
ent_count=0
def key(event):
    global d_count
    global tag
    global ent_count
    print(tag)
#
    if event.keycode == 32 or event.keycode==2359309 :

            if(event.keycode==2359309):
                ent_count=ent_count+1
                if(ent_count<=1):
                    text2.delete('1.0',END)

            if tag == 0:
                data = "end-" + str(d_count) + "c"
                text2.delete(data, "end")
                tag = 1
            else:
                line = text2.get(1.0, END)
                line = re.sub(r'[//.]', ' ', line)
                tok = word_tokenize(line)
                line_length = len(tok)
                check = tok[line_length - 1]
                top1 = 0
                sql="select next from npw where word='"+check+"'"
                cur.execute(sql)
                result=cur.fetchall()
                possible_words=[]
                future=""
                high=0.0
                prediction=""
                for r in result:
                    da=list(r)
                    for d in da:
                        future=d;

                    possible_words = future.split("&")
                    for cool in possible_words:
                        two=check+"_"+cool
                        sql="select prob from probability where two_words='"+two+"'"
                        cur.execute(sql)
                        res=cur.fetchall()
                        for m in res:
                            t=list(m)
                            for u in t:
                                if(u>=high):
                                    high=u;
                                    prediction=cool;

                tag=0


                d_count = len(prediction) + 2
                print("after insetion ", d_count)

                text2.insert(INSERT, " " + prediction, 'predict')
                print("after insertion ", tag)




    elif event.keycode == 3145737:
        if(tag ==0) :
            #data = "end-2c"
            #text2.delete(data, "end")
            print("noworries from second")
            tag=1



    else:
        if tag==0:
                tag=1
                data = "end-" + str(d_count) + "c"
                text2.delete(data, "end")
                print(event.char)
                print(event.keycode)

    print(event.keycode)

text2.bind("<Key>", key)



frame.pack()

root.mainloop()


