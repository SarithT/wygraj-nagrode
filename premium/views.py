from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from start.forms import AnswerForm
from start.forms import CodeForm
from django.template import loader
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from start.models import Answer
# Create your views here.

def user_is_premium(user):
    return user.profile.premium

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def premium(request):
    return render(request, 'premium.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def dowcipy(request):
    return render(request, 'dowcipy.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def tapety(request):
    return render(request, 'tapety.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def nagrody(request):
    return render(request, 'tapety.html')


@login_required
@user_passes_test(user_is_premium, login_url='/get-premium')
def chargePoints(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        user = request.user
        if form.is_valid():
            code = form.save(commit=False)
            code.user = user
            code.save()
            messages.success(request, 'Jeśli wprowadziłeś ......')
    else:
        form = CodeForm()
    return render(request, 'charge-points.html', {'form': form})

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def exchangePointsToVouchers(request):
    user = request.user
    vouchersQuantity = int(request.POST['vouchers'])
    points = int(user.profile.points)
    if points >= vouchersQuantity * 100:
        user.profile.exchanchePointsToVouchers(vouchersQuantity)
        messages.success(request, 'Vouchery zostały dodane do twojego konta.')
    else:
        messages.error(request, 'Nie masz wystarczającej liczby punktów.')
    return redirect('/premium/vouchers')



@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def vouchers(request):
    answers = Answer.objects.filter(user=request.user).order_by('-pub_date')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        user = request.user
        print(form)
        if form.is_valid():
            if user.profile.vouchers > 0:
                answer = form.save(commit=False)
                answer.user = user
                user.profile.exchangeVoucherToAnswer()
                answer.save()
                return redirect('/premium/vouchers')
            else:
                messages.error(request, 'Niestety nie masz już voucherów.')
    else:
        form=AnswerForm()
    # indexTemplate = loader.get_template('vouchers.html')
    context = {
        'answers': answers,
        'form' : form,
    }
    return render(request, 'vouchers.html', context)





@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def ranking(request):
    last_ten = User.objects.filter(profile__premium='True').order_by('-profile__points')[:10]
    indexTemplate = loader.get_template('ranking.html')
    context = {
        'last_ten': last_ten,
    }
    return HttpResponse(indexTemplate.render(context, request))


@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def prizes(request):
    return render(request, 'prizes.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def howItWorks(request):
    return render(request, 'howItWorks.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def getCode(request):
    return render(request, 'get-code.html')

@user_passes_test(user_is_premium, login_url='/get-premium')
@login_required
def aboutPremium(request):
    return render(request, 'aboutContest.html')