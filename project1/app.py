from flask import Flask, render_template, request, redirect, url_for
import markdown2
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Util function to get the content of the encyclopedia entry
def get_entry_content(title):
    file_path = os.path.join("entries", f"{title}.md")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return None

# Util function to save the content of the encyclopedia entry
def save_entry_content(title, content):
    file_path = os.path.join("entries", f"{title}.md")
    with open(file_path, 'w') as file:
        file.write(content)

# Index page
@app.route('/')
def index():
    entries = os.listdir("entries")
    return render_template('index.html', entries=entries)

# Entry page
@app.route('/wiki/<title>')
def entry(title):
    content = get_entry_content(title)
    if content:
        html_content = markdown2.markdown(content)
        return render_template('entry.html', title=title, content=html_content)
    else:
        return render_template('error.html', message='Entry not found'), 404

# Search
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    entries = [entry[:-3] for entry in os.listdir("entries") if query.lower() in entry.lower()]
    return render_template('search_results.html', query=query, entries=entries)

# New page
@app.route('/new_page', methods=['GET', 'POST'])
def new_page():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if not title or not content:
            return render_template('error.html', message='Title and content are required')
        
        if title + ".md" in os.listdir("entries"):
            return render_template('error.html', message='Entry already exists')
        
        save_entry_content(title, content)
        return redirect(url_for('entry', title=title))
    return render_template('new_page.html')

# Edit page
@app.route('/edit_page/<title>', methods=['GET', 'POST'])
def edit_page(title):
    content = get_entry_content(title)
    if request.method == 'POST':
        new_content = request.form.get('content')
        save_entry_content(title, new_content)
        return redirect(url_for('entry', title=title))
    return render_template('edit_page.html', title=title, content=content)

# Random page
@app.route('/random_page')
def random_page():
    import random
    entries = os.listdir("entries")
    if entries:
        random_entry = random.choice(entries)
        title = random_entry[:-3]
        return redirect(url_for('entry', title=title))
    else:
        return render_template('error.html', message='No entries available'), 404

if __name__ == '__main__':
    app.run(debug=True)
