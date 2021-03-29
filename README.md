# Wiki-Gen
A Python microservice that generates a paragraph of text from Wikipedia 
containing a primary and secondary keyword entered by the user. The generated 
paragraph is then outputted into a csv file. The HTML data is retrieved via 
Wikipedia-API and parsed using Beautiful Soup and Python's standard Regular 
expressions (re) module. The GUI is written with Tkinter and the input/output 
files are read/written with Python's csv module.

![](demo.gif)
## Features
- Users can specify a primary and secondary keyword via ```input.csv```
- Program can be run via GUI, where the generated paragraph is displayed to the 
user, or terminal/command line
## Requirements
- Python 3.4+
- Wikipedia-API needs to be installed with pip (which is prepackaged with 
Python 3.4+) prior to use. 
[Wikipedia-API](https://github.com/martin-majlis/Wikipedia-API/) is created by
Martin Majlis and fixes a bug still present in the main Python Wikipedia 
library where the table of contents is not retrieved properly. To install, run 
the following in the terminal: ```pip install wikipedia-api```
- Beautiful Soup 4 needs to be installed by running the following in the 
terminal: ```pip install bs4``` (if you're on Linux, you may need to run the 
following instead: ```sudo pip install beautifulsoup4```)
## How to use (GUI)
1. Open the repo/folder in your favorite IDE and run 
```content_generator.py```. Alternatively, you can navigate to the same 
directory where the files are located via the terminal and enter the following: 
```python content_generator.py```.
2. Enter a primary and secondary keyword.
3. (Optional) Check the 'Create output.csv' checkbox if you wish to create an
output file containing the generated paragraph. ```output.csv``` will be found 
in the same directory as ```content_generator.py```.
4. Generated paragraph will be displayed in the GUI.
<!-- End of list -->
NOTE: Generated paragraph will contain the WHOLE keywords (case insensitive). 
If your primary and secondary keyword is "cat", the generator will not return a 
paragraph containing only the word "catalog".
## How to use (command line/terminal)
1. Ensure that ```input.csv``` is in the same directory as 
```content_generator.py``` and that its format remains unchanged, with the 
first line containing the header and the second line containing the primary and 
secondary keywords, separated by a semicolon.
2. In the terminal, navigate to the directory where the files are located.
3. Run the following in the terminal: ```python content_generator.py 
input.csv```.
4. ```output.csv``` containing the generated paragraph will be found in the 
same directory as ```content_generator.py```.
<!-- End of list -->
NOTE: Generated paragraph will contain the WHOLE keywords (case insensitive). 
If your primary and secondary keyword is "cat", the generator will not return a 
paragraph containing only the word "catalog".
