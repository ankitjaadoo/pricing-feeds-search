from django.shortcuts import render, redirect
from .forms import CSVUploadForm, PricingRecordForm
from .models import PricingRecord
from django.db.models import Q

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search_records')
    else:
        form = CSVUploadForm()
    return render(request, 'pricing/upload_csv.html', {'form': form})

def search_records(request):
    query = request.GET.get('q')
    if query:
        records = PricingRecord.objects.filter(
            Q(store_id__icontains=query) |
            Q(sku__icontains=query) |
            Q(product_name__icontains=query)
        )
    else:
        records = PricingRecord.objects.all()
    return render(request, 'pricing/search_records.html', {'records': records})

def edit_record(request, pk):
    record = PricingRecord.objects.get(pk=pk)
    if request.method == 'POST':
        form = PricingRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('search_records')
    else:
        form = PricingRecordForm(instance=record)
    return render(request, 'pricing/edit_record.html', {'form': form})