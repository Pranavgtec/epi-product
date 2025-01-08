from django.shortcuts import render
from decimal import Decimal
from .models import ProductScheme
from datetime import datetime, timedelta

# View to handle Product Scheme Management
def product_scheme_manage(request):
    if request.method == 'POST':
        # Get form data from POST request
        product_id = request.POST.get('product_id')
        investment = Decimal(request.POST.get('investment'))
        total = Decimal(request.POST.get('total'))
        days = int(request.POST.get('days'))

        # Calculate the start and end date
        start_date = datetime.now()
        end_date = start_date + timedelta(days=days)

        # Create a new ProductScheme object and save it to the database
        scheme = ProductScheme.objects.create(
            product_id=product_id,
            investment=investment,
            total=total,
            days=days,
            start_date=start_date,
            end_date=end_date
        )

        # Return the scheme details to be displayed in the popup
        return render(request, 'product_scheme_manage.html', {
            'scheme': scheme,
            'start_date': start_date.strftime('%m/%d/%Y'),
            'end_date': end_date.strftime('%m/%d/%Y')
        })

    # If it's a GET request, just display the empty form
    return render(request, 'product_scheme_manage.html')


def payment_screen(request):
    return render(request, 'payment.html')