from django.shortcuts import render, redirect
from .forms import ProductSchemeForm
from datetime import datetime, timedelta

def product_scheme_manage(request):
    if request.method == 'POST':
        form = ProductSchemeForm(request.POST)
        if form.is_valid():
            scheme = form.save(commit=False)
            scheme.start_date = datetime.now()
            scheme.end_date = scheme.start_date + timedelta(days=form.cleaned_data['days'])
            scheme.save()
            return redirect('payment_screen')
        else:
            print(f"Form errors: {form.errors}")  # Debugging line
    else:
        form = ProductSchemeForm()
    
    return render(request, 'product_scheme_manage.html', {'form': form})

def payment_screen(request):
    return render(request, 'payment.html')
