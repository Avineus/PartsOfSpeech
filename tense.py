import sys
import spacy
import pyinflect

# VB base form
# VBD past tense
# VBG present participle/continuous
# VBN past participle
# VBP singular present
# VBZ 3rd person singular present


# Usage: python3 tense.py [file name]

# Globals
fname = "verbsList"

if len(sys.argv) > 1:
    #n = int(sys.argv[1])
    fname = sys.argv[1]
else:
    print("Using wordlist file {}". format(fname))

nlp = spacy.load("en_core_web_sm")

file1 = open(fname, 'r')
Lines = file1.readlines()

file2 = open('partOfSpeech.txt', 'w')

print("Started writing to file..")
orig_stdout = sys.stdout
sys.stdout = file2

count = 0
print("%-15s %-15s %-15s %-15s" %( "Present", "Present Cont", "Past", "Past Part"))
for line in Lines:
    #if count == 10:
    #    break
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    text = line.strip()
    doc_dep = nlp(text)
    for i in range(len(doc_dep)):
        token = doc_dep[i]
        if 1: #token.tag_ in ['VBP', 'VBZ', 'VB', 'VBG', 'VBD', 'VBN']:
            #print(token.text, token.lemma_, token.pos_, token.tag_) 
            #text = text.replace(token.text, token._.inflect("VBD"))
            #print(text)
            text_prc = token._.inflect("VBG")
            #print(text_pc)
            text_pas = token._.inflect("VBD")
            #print(text_pas)
            text_pap = token._.inflect("VBN")
            #print(text_pap)
            #print("{} {} {} {}". format(text, text_prc, text_pas, text_pap))
            print("%-15s %-15s %-15s %-15s" %( text, text_prc, text_pas, text_pap))


sys.stdout = orig_stdout

file1.close()
file2.close()

print ("Done...")
