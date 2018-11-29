# main.py
 
from app import app
from db_setup import init_db, db_session
from forms import MediaSearchForm, TitleForm
from flask import flash, render_template, request, redirect
from db_creator import Title, Owner

init_db()
 
@app.route('/', methods=['GET', 'POST'])
def index():
    search = MediaSearchForm(request.form)
    if request.method == 'POST': 
        return search_results(search)
 
    return render_template('index.html', form=search)
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search_string:
        if search.data['select'] == 'Owner':
            qry = db_session.query(Title, Owner).filter(
                Owner.id==Title.owner_id).filter(
                    Owner.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Title':
            qry = db_session.query(Title).filter(
                Title.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Publisher':
            qry = db_session.query(Title).filter(
                Title.publisher.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Title)
            results = qry.all()
    else:
        qry = db_session.query(Title)
        results = qry.all()
 
    if not results:
        flash('Nope, nothing!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)
 
 
@app.route('/new_title', methods=['GET', 'POST'])
def new_title():
    #get info for new title
    form = TitleForm(request.form)
     
    if request.method == 'POST' and form.validate():
        title = Title()
        save_changes(title, form, new=True)
        flash('Title added, thanks a heap!')
        return redirect('/')
     
    return render_template('new_title.html', form=form)
 
def save_changes(title, form, new=False):
    # Get data from form and assign it to correct attributes
    owner = Owner()
    owner.name = form.owner.data
     
    title.title = form.title.data
    title.subject_matter = form.subject_matter.data
    title.publisher = form.publisher.data
    title.media_type = form.media_type.data
    title.file_url = form.file_url.data
    title.owner = owner
     
    if new:
        db_session.add(title)
    
    db_session.commit()
    
@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Title).filter(
        Title.id==id)
    title = qry.first()
 
    if title:
        form = TitleForm(formdata=request.form, obj=title)
        if request.method == 'POST' and form.validate():
            save_changes(title, form)
            flash('You did it!')
            return redirect('/')
        return render_template('edit_title.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
             
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    qry = db_session.query(Title).filter(
        Title.id==id)
    title = qry.first()
 
    if title:
        form = TitleForm(formdata=request.form, obj=title)
        if request.method == 'POST' and form.validate():
            db_session.delete(title)
            db_session.commit()
            flash('Bye forever!')
            return redirect('/')
        return render_template('delete_title.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)
 
if __name__ == '__main__':
    app.debug = True
    app.run()