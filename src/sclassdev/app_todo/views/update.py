from django.shortcuts import render, redirect
from app_todo.utility import query

def view(request, id):
    post = query("SELECT * FROM todo_post WHERE id = %s", [id])
    print(post)

    if not post:
        return render(request, 'app_todo/notfound.html', status=404)
        
    if request.method == 'POST':
        post = post[0]

        title = request.POST.get('title')
        content = request.POST.get('content')

        query("UPDATE todo_post SET title = %s, content = %s WHERE id = %s", [title, content, id])

        return redirect(f"/todo/read/{id}/")
    
    return render(request, 'app_todo/update.html', {'post': post})