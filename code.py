import tkinter as tk
from newspaper import Article, article
from googletrans import Translator

import webbrowser

def summarize():
    url = urltext.get('1.0', "end").strip()
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publishDate.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0',"end")
    title.insert('1.0',article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    publishDate.delete('1.0', "end")
    publishDate.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    title.config(state='disabled')
    author.config(state='disabled')
    publishDate.config(state='disabled')
    summary.config(state='disabled')

def increase():
    url = urltext.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publishDate.config(state='normal')
    summary.config(state='normal')

    title.insert('1.0', article.title)
    default_summary = article.summary
    desired_length = 7
    sentences = default_summary.split('.')
    custom_summary = '.'.join(sentences[:desired_length])
    summary.insert('1.0', custom_summary)
    author.insert('1.0', article.authors)
    publishDate.insert('1.0', article.publish_date)

    summary.config(state='disabled')
    title.config(state='disabled')
    author.config(state='disabled')
    publishDate.config(state='disabled')

def translate():
    url = urltext.get('1.0', "end").strip()
    article = Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()
        # language=language_var.get()
        default_summary = article.summary
        translator = Translator()
        output=translator.translate(default_summary,dest='hi').text
        tr.config(state='normal')
        tr.delete('1.0',"end")
        tr.insert('1.0',output)

    except Exception as e:
        tr.config(state='normal')
        tr.delete('1.0',"end")
        tr.insert('1.0',f"Error:{str(e)}")

    finally:
        tr.config(state='disabled')

def open_link():
    url = urltext.get('1.0',"end").strip()
    webbrowser.open(url)

def more_articles():
    new_window=tk.Toplevel(root)
    new_window.title("More Articles...")
    new_window.geometry('500x600')
    import requests

    def display_news():
        area_of_interest = AreaofInterest.get("1.0", tk.END).strip()
        start_date = StartTime.get("1.0", tk.END).strip()
        end_date = EndDate.get("1.0", tk.END).strip()
        api_key = "e34b8aff60194e49b6a0818871b4889e"

        if area_of_interest:
            try:
                get_news(area_of_interest, start_date, end_date, api_key)
            except requests.exceptions.HTTPError as e:
                LatestLinks.config(state='normal')
                LatestLinks.delete("1.0", tk.END)
                LatestLinks.insert(tk.END, f"HTTPError: {e}")
                LatestLinks.config(state='disabled')
        else:
            LatestLinks.config(state='normal')
            LatestLinks.delete("1.0", tk.END)
            LatestLinks.insert(tk.END, "Please enter an area of interest.")
            LatestLinks.config(state='disabled')

    def get_news(query, start_date, end_date, api_key):
        base_url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "from": start_date,
            "to": end_date,
            "sortBy": "publishedAt",
            "apiKey": api_key,
            "language": "en"
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            articles = data.get("articles", [])
            if not articles:
                print("No articles found.")
                return

            counter = 0
            LatestLinks.config(state='normal')
            LatestLinks.delete("1.0", tk.END)  # Clear previous links
            for article in articles:
                title = article.get('title', '')
                link = article.get('url', '')
                LatestLinks.insert(tk.END, f"Title: {title}\n")
                LatestLinks.insert(tk.END, f"Article Link: {link}\n")
                LatestLinks.insert(tk.END, "---------\n")
                counter += 1
                if counter == 10:  # Break the loop after displaying 10 links
                    break
            LatestLinks.config(state='disabled')
        else:
            print(f"Error: {response.status_code}")
            print(data)
            LatestLinks.config(state='normal')
            LatestLinks.delete("1.0", tk.END)  # Clear previous links
            LatestLinks.insert(tk.END, f"An error occurred while fetching news. Status Code: {response.status_code}")
            LatestLinks.config(state='disabled')


    ALabel = tk.Label(new_window, text="Area of Interest")
    ALabel.pack()
    AreaofInterest = tk.Text(new_window, height=1, width=120)
    AreaofInterest.config(bg='#C6C3C3')
    AreaofInterest.pack()

    BLabel = tk.Label(new_window, text="Start Date")
    BLabel.pack()
    StartTime = tk.Text(new_window, height=1, width=50)
    StartTime.config(bg='#C6C3C3')
    StartTime.pack()

    CLabel = tk.Label(new_window, text="End Date")
    CLabel.pack()
    EndDate = tk.Text(new_window, height=1, width=50)
    EndDate.config(bg='#C6C3C3')
    EndDate.pack()

    btn = tk.Button(new_window, text="Display", command=display_news)
    btn.pack()

    aLabel = tk.Label(new_window, text="Latest Links")
    aLabel.pack()
    LatestLinks = tk.Text(new_window, height=20, width=120)
    LatestLinks.config(state='disabled', bg='#C6C3C3')
    LatestLinks.pack()


root=tk.Tk()

root.title("__News Summarizer__")
root.geometry('1600x900')

uLabel=tk.Label(root,text="URL:")
uLabel.pack()
urltext=tk.Text(root,height=1,width=120)
urltext.pack()

tLabel=tk.Label(root,text="Title")
tLabel.pack()
title=tk.Text(root,height=1,width=120)
title.config(state='disabled',bg='#C6C3C3')
title.pack()
aLabel=tk.Label(root,text="Author")

aLabel.pack()
author=tk.Text(root,height=1,width=120)
author.config(state='disabled',bg='#C6C3C3')
author.pack()
pLabel=tk.Label(root,text="Publishing Date")

pLabel.pack()
publishDate=tk.Text(root,height=1,width=60)
publishDate.config(state='disabled',bg='#C6C3C3')
publishDate.pack()

sLabel=tk.Label(root,text="Summary")
sLabel.pack()
summary=tk.Text(root,height=10,width=120)
summary.config(state='disabled',bg='#C6C3C3')
summary.pack()

translabel=tk.Label(root,text="Translated Summary")
translabel.pack()
tr=tk.Text(root,height=10,width=120)
tr.config(state='disabled',bg='#C6C3C3')
tr.pack()

# languages = ['English','Hindi', 'French', 'German', 'Spanish']
# language_var = tk.StringVar()
# language_dropdown = tk.Combobox(window, textvariable=language_var, values=languages)
# language_dropdown.grid(row=0, column=0, padx=10, pady=10)
# language_dropdown.current(0)
def reset():
    urltext.delete('1.0',tk.END)


btn=tk.Button(root,text="Summarize",command=summarize)
btn.place(x=700,y=550)

btn1=tk.Button(root,text="Increase",command=increase)
btn1.place(x=780,y=550)

btn2=tk.Button(root,text="Reset",command=reset)
btn2.place(x=650,y=550)

btn3=tk.Button(root,text="Translate",command=translate)
btn3.place(x=850,y=550)

button = tk.Button(root, text="Original Article", command=open_link)
button.place(x=540,y=550)

new_window_btn=tk.Button(root,text="More Articles...",command=more_articles)
new_window_btn.place(x=950,y=550)

root.mainloop()
