from django.shortcuts import render,redirect         
from django.contrib import messages                            
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()                                                                     # saves the data from the form
            username = form.cleaned_data.get('username')                                    # retrives the data of username
            messages.success(request, f'Account has been created { username }! ')           # sends messages as toaster
            return redirect('login')                                                        # redirecting the page to Blog-home
    else:
        form = UserRegistrationForm()
    return render(request, 'Users/register.html', { 'form': form } )

    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Account has been updated ! ')           # sends messages as toaster
            return redirect('home')    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'Users/update.html', context)