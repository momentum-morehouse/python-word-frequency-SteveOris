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

    wordfreq = []
    bhop = []
    
    with open(file) as f:
      for items in f:
          bhop.append(items)
      cleaned_text = []
      for w in bhop:
        clean = re.sub(r"[!?.,]","", w.lower())
        cleaner = clean.split()
        cleaned_text.append(cleaner)
    
      working_list = flatten_lol(cleaned_text)
      for word in list(working_list):  
          if word in STOP_WORDS:
           working_list.remove(word)
      for word in working_list:
        wordfreq.append(working_list.count(word))
        print("Pairs\n" + str(list(zip(working_list, wordfreq))))
    


  
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