# text-mining

Please read the [instructions](instructions.md).

1. Project Overview

For this assignment, I chose The Wealth of Nations by Adam Smith, pulled from Gutenburg Library online. The Wealth of Nations was published in 1776, and my aim was to compare this text to modern text (Pride and Prejudice) in order to examine whether there has been any significant difference in the common words used. Techniques I used were basic python codes which I created in order mainly to count the number of words within the text, mainly based on the "dictionary" and "list" data structures.

2. Implementation

I heavily relied upon dictionary and list data structures in order to obtain a meaningful insight from the text. First of all, the text from Internet had to be converted to readable form by computer which was done by using urllib library and string methods. List data structure was mainly used in order to supplent dictionary data structure, such as changing the order of keys in dictionary.

For most of the functions, I had installed a feature that goes through each line in the text so that I can observe the text as a whole. I thought about partitial analysis as well (i.g. chapter by chapter), yet considering the academic nature of the book, I thought it best to get the whole picture since the tone of the text should stay consisntent throughout the text.

Dictionary data structure is the most important component of this assignement because its power with regard to storing values with respect to keys. Rather than using list, which only store one value per index, and tuple, which is immutable, dictionary data structure truly came in handy due to the aforementioned nature of keys and values. It was appropriate in the context of statistical analysis as well because dictionary data structure can represent the intersection of texts and numbers.

3. Results

It was interesting to see the percentage of uniques words used in the text with regard to the total number of words. At 2.77%, the ratio between unique words and total words signifies how much each word was repeated used in the text. On average, each unique word was used 36.09 times in the text, signifying generality and applicability of the English language, even back in 18th century. It was extremely meaningful to see that the overarching structure of the English language did not change whilist vocabularies used might have been different.

In order to further explore the vocabularies used, I went on to list the top 10 commonly used words in the text. The result was quite surprising because it looked quite identical from the result which we obtained from the analysis of "Pride and Prejudice" in class, consisting of articles such as "the" and "a," and prepositions such as "of" and "to." Here I was able to observe that those less meaningful words have not evolved too much since they are too generic in a sense that they simply support the structure of the language rather than connote a meaning. While the text was published in Scotland, which has a different accent and local jargon, and published while back ago, it was intriguing to see that there is almost no variation between the most commonly used words.

4. Reflection

Since this was very traditional text, I did not deem it appropriate to do sentiment analysis since the work is not very communicative of emotions, but rather quite descriptive. However, I could have explored further methods of natural language processing with regard to academics. I could also have gone to compare the text with other economics books from differnt authers or different eras in order to analyze the different style that each of them has. It was a great opportunity to review and instill into my brain some important data structure concepts, and I was able to display various useful ratios/statistical measures.



