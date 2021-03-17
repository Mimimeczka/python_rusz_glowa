from flask import Flask, render_template, request, escape
from v_search import search_letters_or_vowels
import mysql.connector

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Zapisuje do bazy, wykorzystane na stronie"""
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'justyna',
        'password': '123',
        'database': 'vsearchlogDB'
    }

    conn = mysql.connector.connect(**dbconfig)

    cursor = conn.cursor()

    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res))

    conn.commit()
    cursor.close()
    conn.close()


@app.route("/search",  methods=['POST'])
def search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto twoje wyniki:'
    results = " ".join(search_letters_or_vowels(phrase, letters))
    log_request(request, results)
    return render_template('result.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/') # dekorator route łączy urla z funkcją
@app.route("/entry")
def entry_peage() -> 'html':
    return render_template('entry.html', the_title='Witamy na naszej stronie SEARCH')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log', 'r') as file:
        for line in file:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ['Dane z formularza', 'Adres klienta', 'Agent użytkowanika', 'Wyniki']
    return render_template('viewlog.html',
                           the_title='Widok logu',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)




