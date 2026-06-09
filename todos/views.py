from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    form = TodoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todos:list")

    todos = Todo.objects.all()
    remaining_count = todos.filter(completed=False).count()

    return render(
        request,
        "todos/todo_list.html",
        {
            "form": form,
            "todos": todos,
            "remaining_count": remaining_count,
        },
    )


@require_POST
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save(update_fields=["completed"])
    return redirect("todos:list")


@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todos:list")
