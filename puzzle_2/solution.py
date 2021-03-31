class Solution:
    def isAlienSorted(self, words, order):
        order_dict = {}
        for i, c in enumerate(order):
            order_dict[c] = i
        # trick for dealing with edge case
        order_dict['*'] = -1

        for i, word in enumerate(words[1:]):
            previous_word = words[i]

            l1 = len(previous_word)
            l2 = len(word)

            # trick for dealing with edge case
            if l2 < l1:
                word = word + '*'
                l2 = l2 + 1

            for j in range(min(l1, l2)):
                c2 = order_dict[word[j]]
                c1 = order_dict[previous_word[j]]
                if c2 > c1:
                    break
                elif c2 < c1:
                    return False

        return True


'''Discussion:
In this solution we loop through all words, and compare them to the neighbour
immediately before.
If any pair breaks the order, then the whole sequence is not ordered.
An edge case arises when one word contains another exactly.
For example, 'apple' and 'app'.
Since comparisons between 'a' with 'a', 'p' with 'p',
and 'p' with 'p' again lead to "still ordered" results,
the naive method might naively conclude that it is okay for
'apple' to come before 'app'.
We avoid this by artificially adding a new character to the second word IF
this word is shorter than the first word.
For example, if we are comparing 'apple' and 'app', we turn this into a
comparison between 'apple' and 'app*'.
The newly introduced character '*' is designed to be the smallest of all,
associated with a dict value of -1.
Thus any comparison against * will lead to 'out of order' automatically.
With this approach, we don't have to check every single time if we reached out
the end of the word.
'''
