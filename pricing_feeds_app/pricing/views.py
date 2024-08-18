import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PricingRecord
from .forms import PricingRecordForm

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse('Invalid file type. Please upload a CSV file.')

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            PricingRecord.objects.create(
                store_id=row['Store Id'],
                sku=row['SKU'],
                product_name=row['Product name'],
                price=row['Price'],
                date=row['Date']
            )
        return redirect('search_records')
    return render(request, 'upload_csv.html')

def search_records(request):
    records = PricingRecord.objects.all()
    if request.method == 'GET':
        store_id = request.GET.get('store_id')
        sku = request.GET.get('sku')
        product_name = request.GET.get('product_name')
        if store_id:
            records = records.filter(store_id=store_id)
        if sku:
            records = records.filter(sku=sku)
        if product_name:
            records = records.filter(product_name__icontains=product_name)
    return render(request, 'search_records.html', {'records': records})

def edit_record(request, pk):
    record = PricingRecord.objects.get(pk=pk)
    if request.method == 'POST':
        form = PricingRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('search_records')
    else:
        form = PricingRecordForm(instance=record)
    return render(request, 'edit_record.html', {'form': form})