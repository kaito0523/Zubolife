from django.shortcuts import render, get_object_or_404
from .models import Recipe, Memo
from accounts.models import CustomUser, UserManager
from .forms import RecipeForm, MemoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def cooklist(request):
    recipes = Recipe.objects.all()
    context = { "recipes" : recipes }
    return render(request, 'app/cooklist.html', context)

def detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    context = { "recipe" : recipe }
    return render(request, 'app/detail.html', context)

@login_required
def followPlace(request, id):
    """場所をお気に入り登録する"""
    recipe = get_object_or_404(Recipe, pk=id)
    request.user.favorite_recipe.add(recipe)
    return redirect('app:favorite')

@login_required
def favorite(request):
    # 現在ログインしているユーザーのお気に入りレシピを取得
    user_instance = request.user
    recipes = user_instance.favorite_recipe.all()  # 修正: user_instance を使用
    context = { "recipes": recipes }
    return render(request, 'app/favorite.html', context)

@login_required
def newrecipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.image = request.FILES['image']
            recipe_form.save()
            recipes = Recipe.objects.all()
            context = { "recipes" : recipes }
            return render(request, "app/cooklist.html", context)
    recipe_form = RecipeForm()
    context = { "recipe_form" : recipe_form }
    return render(request, "app/newrecipe.html", context)

@login_required
def memo(request):
    memos = Memo.objects.all()
    context = { "memos" : memos }
    return render(request, "app/memolist.html", context)

@login_required
def memo_detail(request, id):
    memo = get_object_or_404(Memo, pk=id)
    context = { "memo" : memo }
    return render(request, 'app/memo_detail.html',context)


@login_required
def newmemo(request):
    if request.method == "POST":
        memo_form = MemoForm(request.POST)
        if memo_form.is_valid():
            memo_form.save()
            memos = Memo.objects.all()
            context = { "memos" : memos }
            return render(request, "app/memolist.html", context)
    memo_form = MemoForm()
    context = { "memo_form" : memo_form }
    return render(request, "app/newmemo.html", context)

@login_required
def newmemo2(request):
    if request.method == "POST":
        memo_form = MemoForm({"content":request.POST["zairyou"]})
        context = { "memo_form" : memo_form }
        return render(request, "app/newmemo.html",context)

