# forms.py
 
from wtforms import Form, StringField, SelectField
 
class MediaSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Media', 'Media'),
               ('Subject', 'Subject')]
    select = SelectField('Search for media:', choices=choices)
    search = StringField('')
    
class TitleForm(Form):
    media_types = [('Physical Copy', 'Physical Copy'),
                   ('PDF', 'PDF'),
                   ('Other', 'Other')]
    title = StringField('Title')
    subject_matter = StringField('Subject Matter')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
    name = StringField('Owner Name')