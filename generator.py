import csv
from bs4 import BeautifulSoup
from os import path
import re
import tkinter as tk
import wikipediaapi


def generate_GUI(event, fields, options):
    """Retrieve and display paragraph from Wikipedia in GUI.

    Args:
        event (obj): Tkinter event object
        fields (list): List of Tkinter widget objects to interact with
        options (list): List of numbers corresponding to checkbox statuses
    """
    primary = str(fields[0]).lower()
    secondary = str(fields[1]).lower()
    textbox = fields[2]
    output_check = options[0]

    # clears textbox if not empty, return error msg if keyword missing
    if fields_valid(primary, secondary, textbox) is False:
        return

    # searches for page with title containing primary keyword
    wiki, page, soup, paragraphs = find_page(primary)
    if page.exists() is False:
        textbox.insert(tk.END, "Wikipedia page does not exist, please try "
                               "again.")
        return

    # returns message if search leads to disambiguation page
    if "may refer to:" in page.text.lower():
        textbox.insert(tk.END, soup.get_text())
        return

    # searches paragraph in page containing whole keywords
    if find_paragraph("GUI", paragraphs, fields, output_check) is True:
        return

    textbox.insert(tk.END, "Paragraph containing both primary and secondary "
                           "keywords does not exist, please try again.")
    return


def generate_output():
    """Retrieves and stores paragraph from Wikipedia in output file."""
    # check if input.csv in same directory as content_generator.py
    if path.exists('../../Desktop/content-generator-main/input.csv') is True:
        primary, secondary = search_input()
        fields = [primary, secondary]

        # searches for page with title containing primary keyword
        wiki, page, soup, paragraphs = find_page(primary)

        # displays error message if page does not exist
        if page.exists() is False:
            print("Wikipedia page does not exist, please try again.")
            exit()

        # returns message if search leads to disambiguation page
        if "may refer to:" in page.text.lower():
            print(soup.get_text())
            exit()

        # searches paragraph in page containing whole keywords
        if find_paragraph("output", paragraphs, fields, None) is True:
            print("output.csv file created.")
            exit()

        print("Paragraph containing both primary and secondary keywords does "
              "not exist, please try again.")
        exit()

    else:
        print("input.csv not found, please ensure that it is in the same "
              "directory as content_generator.py and try again.")
        exit()


def generate_client(primary, secondary):
    """Retrieves and returns paragraph from Wikipedia to client."""
    primary = str(primary).lower()
    secondary = str(secondary).lower()

    # searches for page with title containing primary keyword
    wiki, page, soup, paragraphs = find_page(primary)
    if page.exists() is False:
        return "Wikipedia page does not exist, please try again."

    # returns message if search leads to disambiguation page
    if "may refer to:" in page.text.lower():
        return "Disambiguation page found, please refine request."

    return find_paragraph("client", paragraphs, [primary, secondary])


def fields_valid(primary, secondary, textbox):
    """Ensures that keywords are provided and textbox is empty.

    Args:
        primary (str): Primary keyword
        secondary (str): Secondary keyword
        textbox (obj): Tkinter textbox object used to display generated content
    """
    text_length = textbox.get("1.0", tk.END)
    if len(text_length) != 0:
        textbox.delete("1.0", tk.END)
    if len(primary) == 0 or len(secondary) == 0:
        textbox.insert(tk.END, "Please enter a primary and secondary "
                               "keyword.")
        return False
    return True


def find_page(primary):
    """Finds Wikipedia page containing primary keyword in title.

    Args:
        primary (str): Primary keyword
    """
    wiki = wikipediaapi.Wikipedia(language='en',
                                  extract_format=wikipediaapi.ExtractFormat.HTML)
    page = wiki.page(primary)
    soup = BeautifulSoup(page.text, 'html.parser')
    paragraphs = soup.find_all('p')
    return wiki, page, soup, paragraphs


def request_census(primary, secondary, textbox):
    """Sends request to Population Generator for state population.

    Args:
        primary (str): Primary keyword
        secondary (str): Secondary keyword
        textbox (obj): Tkinter textbox object used to display generated content
    """
    n = net.Network()
    arr = [primary.capitalize(), secondary]
    response = n.request(arr)
    try:
        response = int(response)
        textbox.insert(tk.END, "Population of " + primary.capitalize() +
                       " in " + secondary + ": " + str(response) + "\n\n")
    except:
        textbox.insert(tk.END, str(response) + "\n\n")


def find_paragraph(mode, paragraphs, fields, output_check=None):
    """Finds paragraph containing keywords in Wikipedia page."""
    primary = fields[0]
    secondary = fields[1]

    for p in paragraphs:
        if re.search(r'\b' + primary + r'\b', str(p).lower()) and \
                re.search(r'\b' + secondary + r'\b', str(p).lower()):
            p = p.get_text()
            if mode == "client":
                return p
            if mode == "GUI" or "output":
                if mode == "GUI":
                    textbox = fields[2]
                    textbox.insert(tk.END, p)
                # creates output.csv file if user checked the checkbox
                if output_check == 1 or mode == "output":
                    p = p.replace('\n', ' ')  # remove newlines
                    with open('output.csv', mode='w', newline='') as \
                            output_csv:
                        csv_writer = csv.writer(output_csv, delimiter=',',
                                                quotechar='"',
                                                quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(
                            ['input_keywords', 'output_content'])
                        csv_writer.writerow(
                            [primary + ';' + secondary, p])
                return True


def search_input():
    """Searches input file for primary and secondary keywords."""
    with open('../../Desktop/content-generator-main/input.csv') as input_csv:
        csv_reader = csv.reader(input_csv, delimiter=';')
        for index, val in enumerate(csv_reader):
            if index == 1:
                if val[0] == '' or val[1] == '':
                    print("Missing a primary or secondary keyword in the "
                          "input file, please try again.")
                    exit()
                else:
                    primary = val[0].lower()
                    secondary = val[1].lower()
                    return primary, secondary
        print("Please reformat the input file and try again.")
        exit()
