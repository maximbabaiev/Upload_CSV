import csv
import datetime
import io

from django.contrib import messages
from django.shortcuts import render

from .forms import *


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Файл должен быть типа .csv')
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for i, col in enumerate(csv.reader(io_string)):
                if i == 10:
                    break
                _, created = GameModel.objects.update_or_create(
                    name=col[1],
                    platform=col[2],
                    year=col[3],
                    genre=col[4],
                    publisher=col[5],
                    na_sales=col[6],
                    eu_sales=col[7],
                    jp_sales=col[8],
                    other_sales=col[9],
                    global_sales=col[10],
                )
            return render(request, 'upload_data.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'upload_data.html', {'form': form})


def show_all(request):
    games = GameModel.objects.all()
    return render(request, 'all.html', {'games': games})
