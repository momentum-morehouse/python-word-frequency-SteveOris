import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def flatten_lol(lol):
  flat_list = []
  for l in lol:
    for word in l:
      flat_list.append(word)
  return flat_list


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    
    first = []
    frequency = {}
    #empty contianers ^

    with open(file) as f:
      for items in f:
          first.append(items)
          # ^ grabbing the item/words out of the text file
      cleaned_text = []
      for w in first:
        clean = re.sub(r"[!?.,]","", w.lower())
        cleaner = clean.split()
        cleaned_text.append(cleaner)
        # ^ removing the punctuation from the text 
    
      working_list = flatten_lol(cleaned_text)
      # ^ running the cleaned text through my flatten function

      for word in list(working_list):  
          if word in STOP_WORDS:
           working_list.remove(word)
           for word in working_list:
             count = frequency.get(word,0)
             frequency[word] = count + 1
     
             frequency_list = frequency.keys()
 
             for words in frequency_list:
               # ^ counting words in text
              print(words, '|' ,frequency[words]) 


    
  
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)