# Auto-suggest

## Introduction
Based on a predefined list of phrases and a partial input string, a program named auto_suggest provides auto-suggestions. It is commonly used to assist users in finishing their words or searches in text editors and search engines.

## Approach
The auto-suggest function is implemented using the auto_suggest Python method. The function takes two inputs: a list of words and a partial input string. It then looks for matches in the list of terms by filtering the partial input string. Two matching algorithms are used: precise substring matching and wildcard pattern matching, depending on whether the input string contains wildcard characters ({'*'}).

The function creates a regular expression pattern in order to accurately match the partial input string as a substring.

## Testing
The program includes a set of test cases to automate testing using the unittest framework. These test cases cover various scenarios, including:

Exact subword matches
Wildcard matches
No matches
Case-insensitive matches
Empty input
