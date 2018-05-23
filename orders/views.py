from django.shortcuts import render, redirect
from .models import Order, Collected
from .forms import OrderForm, CollectionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def collections(request):
    collecteds = Collected.objects.all()
    return render(request, 'collections.html', {'collecteds': collecteds})


@login_required
def eggcollections(request):
    if request.POST:
        form = CollectionForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/collect', messages.success(request, 'collection was successfully created.', 'alert-success'))
            else:
                return redirect('/collect', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/collect', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = CollectionForm()
    return render(request, 'collect_now.html', {'form': form})


@login_required
def collectiondestroy(request, collected_id):
    collecteds = Collected.objects.get(id=collected_id)
    collecteds.delete()
    return redirect('/collect', messages.success(request, 'Order was successfully deleted.', 'alert-success'))


@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})


@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})


@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form': form})


@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form': form})


@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))
