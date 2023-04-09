from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# view
@login_required
def product_list(request):
    # 등록 된 상품의 리스트를 볼 수 있는 view
    pass

@login_required
def product_create(request):
    # 상품 등록 view
    pass