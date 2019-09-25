Find the sentence containing the largest number of words in some given text.

Text is specified as string **S** consisting of **N** characters: letters, spaces, dots(.), question marks(?),
and exclamation marks(!).

- text can be divided into sentences by splitting it at dots, ?, and !;
- sentence can be divided into words by splitting at spaces;
- sentence without words is valid, but valid word must contain at least one letter.

`S = "We test coders. Give us a try?"` should `return 4`.

`S = "forget CVs. . Save time. x x"` should `return 2`.
