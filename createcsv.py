# Import the english_words and PyDictionary modules
from english_words import get_english_words_set
from PyDictionary import PyDictionary as words
import csv
from threading import Thread
import time

class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
 
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
             
    def join(self, *args):
        start_time = time.time()
        Thread.join(self, *args)
        end_time = time.time()
        if end_time - start_time > 60:
            print(f"Thread {self.name} took more than a minute to process, skipping.")
        return self._return
    
def get_definition(word):
    meanings_data = words.meaning(word, True)
    meanings = ""
    if meanings_data:
        count = 0
        for key, value in meanings_data.items():
            if count == 0:
                try:
                    meanings = str(value[0])
                except:
                    meanings = str(value)
                count += 1
            else:
                try:
                    meanings = meanings + "; " + str(value[0])
                except:
                    meanings = meanings + "; " + str(value)
    return [word, meanings]

def main():

    # Get a set of English words and convert all the words to lowercase
    web2lowerset = get_english_words_set(['web2'], lower=True)
    five_letter_words = [word for word in web2lowerset if len(word) == 5]
    six_letter_words = [word for word in web2lowerset if len(word) == 6]
    data = []

    threads = []
    for word in five_letter_words:
        thread = CustomThread(target=get_definition, args=(word,))
        threads.append(thread)
        thread.start()
        print(f"{len(threads)} five letter words added...", end="\r")

    print('')
    progress = 0
    for thread in threads:
        value = thread.join()
        if value is not None:
            data.append(thread.join())
            progress += 1
        print(f"{progress}/{len(threads)} five letter words processed...", end="\r")

    # Create a CSV writer object.
    print('')
    print("Saving to CSV")
    with open("words.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the data to the CSV file.
        for row in sorted(data):
            writer.writerow(row)

    print("Five letter words saved to words.csv")

    threads = []
    for word in six_letter_words:
        thread = CustomThread(target=get_definition, args=(word,))
        threads.append(thread)
        thread.start()
        print(f"{len(threads)} six letter words added...", end="\r")

    print('')
    progress = 0
    for thread in threads:
        value = thread.join()
        if value is not None:
            data.append(thread.join())
            progress += 1
        print(f"{progress}/{len(threads)} six letter words processed...", end="\r")

    # Create a CSV writer object.
    print('')
    print("Saving to CSV")
    with open("words.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the data to the CSV file.
        for row in sorted(data):
            writer.writerow(row)

    print("Complete")

if __name__ == "__main__":
    main()
