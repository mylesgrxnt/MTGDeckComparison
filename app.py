from flask import Flask, render_template, request, redirect, url_for, session
from compare import parse_strings, compare_card_dictionaries

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session storage

@app.route('/', methods=['GET', 'POST'])
def index():
    # Retrieve stored decks from session (if available)
    starting_deck = session.get('starting_deck', '')
    ending_deck = session.get('ending_deck', '')

    if request.method == 'POST':
        starting_deck = request.form.get('starting_deck', '')
        ending_deck = request.form.get('ending_deck', '')

        # Store in session before redirecting
        session['starting_deck'] = starting_deck
        session['ending_deck'] = ending_deck

        starting_dict = parse_strings(starting_deck)
        ending_dict = parse_strings(ending_deck)

        added_list, copyable, removed_list = compare_card_dictionaries(starting_dict, ending_dict)

        # Store results in session
        session['added_list'] = added_list
        session['removed_list'] = removed_list
        session['copyable_list'] = copyable

        return redirect(url_for('results'))

    return render_template('index.html', starting_deck=starting_deck, ending_deck=ending_deck)

@app.route('/results')
def results():
    # Retrieve lists from session
    added_list = session.get('added_list', [])
    removed_list = session.get('removed_list', [])
    copyable_list = session.get('copyable_list', [])

    return render_template('results.html', 
                           added_list=added_list, 
                           removed_list=removed_list, 
                           copyable_list=copyable_list)

if __name__ == '__main__':
    app.run(debug=True)
