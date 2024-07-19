News Summarizer
This is a Python application that uses Tkinter for the graphical user interface (GUI) to summarize news articles, translate summaries, and fetch more articles based on user input. It utilizes the newspaper3k library to parse and summarize articles, and googletrans for translations.

Features
Summarize Articles: Provide a URL to a news article and get a summarized version of the article.
Translate Summaries: Translate the summary of the article to Hindi.
Fetch More Articles: Get more articles based on the area of interest and date range provided by the user.
Display Article Metadata: Show the title, author, and publishing date of the article.
Open Original Article: Open the original article in a web browser.

Requirements
Python 3.x
Tkinter
newspaper3k
googletrans==4.0.0-rc1
requests

Installation
Clone the repository:
git clone https://github.com/YourUsername/YourRepository.git
cd YourRepository
Install the required packages:
pip install tkinter newspaper3k googletrans==4.0.0-rc1 requests

Usage
Run the application:
python code.py
Using the Application:

URL: Enter the URL of the news article you want to summarize.
Summarize: Click the "Summarize" button to get the summary.
Increase: Click the "Increase" button to increase the length of the summary.
Translate: Click the "Translate" button to translate the summary to Hindi.
Reset: Click the "Reset" button to clear the URL input.
Original Article: Click the "Original Article" button to open the article in a web browser.
More Articles...: Click the "More Articles..." button to open a new window where you can fetch more articles based on your area of interest and date range.

Contributing
Fork the repository

Create a new branch:
git checkout -b feature-branch

Make your changes and commit them:
git commit -m 'Add some feature'

Push to the branch:
git push origin feature-branch

Submit a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README.txt provides a basic overview of the application, its features, installation instructions, usage, and contribution guidelines. Adjust the URL in the cloning step to point to your actual repository.






