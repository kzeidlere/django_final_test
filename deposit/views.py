from django.shortcuts import render
from django.db import IntegrityError
from django.views.generic import ListView, FormView, View, DetailView
from deposit.models import Deposit
from deposit.forms import DepositForm


class DepositListView(ListView):
    model = Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):
    models = Deposit
    template_name = 'deposit_detail.html'


class AddDepositView(FormView):
    form_class = DepositForm
    template_name = 'add_new_deposit.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response
