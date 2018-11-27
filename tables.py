from flask_table import Table, Col, LinkCol

class Results(Table):
	id = Col('Id', show=False)
	title = Col('Title')
	subject_matter = Col('Subject Matter')
	publisher = Col('Publisher')
	media_type = Col('Media Type')
	owner = Col('Owner')
	edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
	delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))