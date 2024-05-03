import csv

def relative_letter_frequency_csv(filename):
    # Dictionary to store the total frequency of each word
    word_frequencies = {}

    # Read the CSV file
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        total_frequency = 0

        # Process each row in the CSV
        for row in reader:
            word, frequency = row[0], int(row[1])
            if word in word_frequencies:
                word_frequencies[word] += frequency
            else:
                word_frequencies[word] = frequency
            total_frequency += frequency

    # Dictionary to store the relative frequency of each word
    relative_frequencies = {}

    # Calculate relative frequency for each word
    for word, frequency in word_frequencies.items():
        relative_frequencies[word] = frequency / total_frequency

    return relative_frequencies

if __name__ == '__main__':
    #filename = 'unigram_freq.csv'
    filename = 'unigram_freq.csv'
    relative_freq = relative_letter_frequency_csv(filename)

    print(relative_freq)