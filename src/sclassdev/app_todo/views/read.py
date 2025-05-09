'''
ID DIDAPAT URL YANG DIMASUKKAN OLEH USER
post = query("SELECT * FROM blog_post WHERE id = %s", [id])

tuliskan logic code untuk melakukan render post yang ditemukan ke frontend atau html

jika tidak ketemu, tampilkan pesan not found
'''

from django.shortcuts import render
from app_todo.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("SELECT * FROM todo_post WHERE id = %s", [id])

        if post:
            return render(request, 'app_todo/read.html', {'post': post[0]})
        
        return render(request, 'app_todo/notfound.html', status=404)