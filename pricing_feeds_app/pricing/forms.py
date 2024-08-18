from django import forms
from .models import PricingRecord
import csv
from io import StringIO

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

    def save(self):
        csv_file = self.cleaned_data['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        for row in reader:
            PricingRecord.objects.update_or_create(
                store_id=row['Store Id'],
                sku=row['SKU'],
                product_name=row['Product name'],
                defaults={'price': row['Price'], 'date': row['Date']},
            )

class PricingRecordForm(forms.ModelForm):
    class Meta:
        model = PricingRecord
        fields = '__all__'