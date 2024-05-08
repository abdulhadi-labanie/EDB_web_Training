from website import create_app

app = create_app()
app.config['SECRET_KEY'] = 'adslkjfilgjoiewj.dasfLKFHE'

if __name__ == '__main__':
    app.run(debug=True, port =7050)
