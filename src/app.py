from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from markupsafe import Markup

app = Flask(__name__, template_folder='../templates', instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev'
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()

db.init_app(app)


from model import Page

#with app.app_context():
#    db.create_all()
@app.route('/')
def main():
    app.logger.info('main2')
    p = db.session.query(Page)
    return render_template('main.html', pages=p)


@app.route('/new_page', defaults={'page_id': None}, methods=['GET', 'POST'])
@app.route('/edit_page/<string:page_id>', methods=['GET', 'POST'])
def edit_page(page_id):
    if request.method == 'POST':
        if request.form.get('save') == 'Save':
            p_id = save_page(request.form)
            return redirect(url_for('show_page', page_id=p_id))
        elif request.form.get('cancel') == 'Cancel':
            return redirect(url_for('main'))
    p = None
    if page_id:
        p = db.get_or_404(Page, page_id)
    return render_template('page_edit.html', page=p)


@app.route('/page/<string:page_id>')
def show_page(page_id):
    p = db.get_or_404(Page, page_id)
    content = '#' + str(p.title) + '\n'
    content = Markup(markdown.markdown(content + p.content if p.content else '', extensions=['extra', 'sane_lists', WikiLinkExtension(base_url='/page/', end_url='')]))
    return render_template('page.html', page={'content': content, 'tags': p.tags, 'id': p.id})


def save_page(values):
    tags = values['tags']
    if values['id']:
        p = db.get_or_404(Page, values['id'])
        p.title = values['title']
        p.content = content=values['content']
        p.tags = tags
        db.session.commit()
        return p.id
    else:
        p = Page(title=values['title'], content=values['content'], tags=tags)
        db.session.add(p)
        db.session.commit()
        return p.id
