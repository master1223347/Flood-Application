from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
@app.route('/')
def login_page():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    zipcode = request.form['zipcode']
    email = request.form['email']
    
    # Store user information in session
    session['username'] = username
    session['zipcode'] = zipcode
    session['email'] = email
    
    # Redirect to the language selection page
    return redirect('/select_language')
@app.route('/select_language')
def language_selection():
    return render_template('language.html')
@app.route('/select_language', methods=['POST'])
def select_language():
    selected_language = request.form['language']
    session['language'] = selected_language
    
    # Redirect to the welcome page
    return redirect('/welcome')
@app.route('/welcome')
def welcome():
    # Retrieve user information from session
    username = session.get('username')
    zipcode = session.get('zipcode')
    email = session.get('email')
    selected_language = session.get('language')
    
    # Redirect to the respective language welcome page
    if selected_language == 'english':
        return redirect('/welcome')
    elif selected_language == 'spanish':
        return redirect('/span')
    elif selected_language == 'chinese':
        return redirect('/chi')
    else:
        return "Invalid language selection"
@app.route('/eng.html')
def english_page():
    # Retrieve user information from session
    username = session.get('username')
    zipcode = session.get('zipcode')
    email = session.get('email')
    
    return render_template('welcome.html', username=username, zipcode=zipcode, email=email)
@app.route('/span.html')
def spanish_page():
    # Retrieve user information from session
    username = session.get('username')
    zipcode = session.get('zipcode')
    email = session.get('email')
    
    return render_template('span.html', username=username, zipcode=zipcode, email=email)
@app.route('/chi.html')
def chinese_page():
    # Retrieve user information from session
    username = session.get('username')
    zipcode = session.get('zipcode')
    email = session.get('email')
    
    return render_template('chi.html', username=username, zipcode=zipcode, email=email)

@app.route('/descript.html')
def descript():
    return render_template('descript.html')

if __name__ == '__main__':
    app.run(debug=True)

