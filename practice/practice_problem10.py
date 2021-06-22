def reorderSpaces( text: str) -> str:
        words = text.split()
        len_words = len(words)
        spaces = text.count(' ')

        """
        Base Case: one word
        - Return word with spaces trailing, if any.
        """
        if len_words == 1:
            return ''.join([words[0],  ' ' * spaces])

        """
        General Case: two or more words
        - Create separator to divide spaces evenly between words.
        - Create trailing to capture remaining spaces
        - Combine words, separators, and trailing and return
          result
        """
        separator = ' ' * (spaces // (len_words - 1))
        trailing = ' ' * (spaces % (len_words - 1))
        sentence = separator.join(words)
        return ''.join([sentence, trailing])


 
string="  this   is  a sentence "
print(reorderSpaces(string))