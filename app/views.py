from flask import render_template, redirect, url_for
from . import app, db
from .forms import FeedbackForm
from .models import Category, News


@app.route('/')
def index():
    global news_list
    news_list = News.query.all()
    return render_template("index.html", news=news_list)


@app.route('/news')
def news():
    return 'Новости'


@app.route('/news_detail/<int:id>')
def news_detail(id):
    global news_list
    news_detail = News.query.get(id)
    new = (news_list[id-1])
    return render_template("news_detail.html", new=new)


@app.route('/category/<string:name>')
def category_detail(name):
    return f'Категория {name}'


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = FeedbackForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_news.html',
                           form=form)