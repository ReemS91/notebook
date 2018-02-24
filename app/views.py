from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def note(request, note_id):
	note = Note.objects.get(id=note_id)
	context = {
		'note': note
	}
	return render(request, 'note.html', context)

def notebook(request):
	notes = Note.objects.all()
	context = {
		'notes': notes
	}
	return render(request, 'notebook.html', context)

def update(request , note_id):
	note_obj = Note.objects.get(id=note_id) 	# get note object
	note_obj.title = request.POST.get('title') 	# update its data
	note_obj.body = request.POST.get('body')
	note_obj.save() 							# save note object
	
	return redirect('/notebook/') 				# take user back to notebook page

def new_note(request):
	return render(request, 'newnote.html', {})

def create(request):
	# make new note
	title_var = request.POST.get('title')	# get title from submitted form
	body_var = request.POST.get('body')		# get body from submitted form
	note_obj = Note.objects.create(
					title=title_var,
					body=body_var)			# create new note object

	return redirect('/notebook/')			# take the user to the notebook page

def delete(request, note_id):
	Note.objects.get(id=note_id).delete()
	return redirect("/notebook/")