<details>
 <summary>Personal Introduction</summary>
    hi, im wonkmanbad (wonkmangood on git). im a dude in North USA who flunked college twice and can barely concept basic
   maths. i originally went for a degree related to photography and was later diagnosed with a rare eye disorder that hindered
   my ability to really pursue that. i went again a few years later for a general degree in computer science but once again,
   flunked due to low motivation. while i did withdraw from college, i grew really passionate about programming and its related
   topics; specifically topics related to Security and Network Engineering. a good start in those fields was python and too which,
   i found cs50. its been an on and off journey with you guys. my git repo is private, but theres a significant 2 months gap from
   when i dropped interest in this class and finished it. and im glad to say, i more or less finished it.


   nonetheless, heres my final project! hope you enjoy and give me many A+'s.
</details>


# **wonkCIPHER**: mimic of randomart for text
#### **Video Demo**:  <URL HERE>
#### **Description**:
wonkCIPHER is a clone of [randomart](https://github.com/ansemjo/randomart) with functionality
strictly to text-inputs with more intractability; offering terminal outputs, random gen, etc.


The original plan for my final was a POS system used in food service, but found that rather hard to run against pytest. So alas, here we are with plan B. Be thankful it wasn't plan C.   :)


While yes, it is not a rather *efficient* way of means to cipher data, but more so a proof of concept. While tested rigorously, I am sure certain inputs or interactions with this program are less than efficient. wonkCIPHER is a collection of the knowledge I've gained in cs50 edX's Python Course and my own personal research.




***


Functions and their descriptions are as follows:


#### **open_cipher():**
The 'core' function needed for nearly all other functions. open_cipher() uses the csv package to open the related file in this repository called 'dictionary.csv' as the 'cipher key.' Subsequentually opening it as a dictionary within a list.


#### **main():**
The initial function. It prompts a user to enter a choice via number menu. Entering a single character number listed beforehand in the terminal will call the function related to their choice. If an incorrect input is entered, it simply recalls main().




#### **encrypt() and random():**
Both these functions use the same guts to do what they do. encrypt() asks the user for an input anywhere from 1 - 25 characters; else raises errors. open_cipher() is hardcoded into these functions for better interfacibility with pytest. After referencing the cipher to the input, I wrote a ~50ish line block that takes the translated length and outputs the cipher in a multiline format with a bit of styling; rather close to randomart. While yes, it could've been shorter and more simple; but the damn thing took me a near week to conceptualize and write. Throughout this entire project, there's lots of evidence of oversights and 'small brain' moments. I apologize. Nonetheless, upon translating, both functions return the value that's printed upon completion. random() does the same thing with the same code but with random imported and randomint() used with a range of 1, 50. (1 inputted text == 2 cipher text, thus where 50 comes from. 25*2)


#### **decrypt():**
For user accessibility, I was unable to figure a way to pytest this function correctly. decrypt() takes five inputs; each a line of the coded cipher and joins them together as one long string. Afterwards, it runs every 2 characters through a for-loop until completing the original text. Then returning it to the terminal. This function is the only function to use open_cipher().


#### **clear()**
clear() simply runs a terminal clearing command depending on the OS.

** **

Enjoy, and thanks for all the fish.
-WonkManBad(Good)(W)