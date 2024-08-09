from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Policy
from django.contrib.auth.models import User


def user_login(request):
	msg = ""
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return render(request ,'policy_detail.html')
		else:
			msg='Username OR password is incorrect'
	return render(request ,'login.html',{'msg':msg})

def admin_login(request):
	msg = ""

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			if user.is_superuser:
				login(request, user)
				return redirect('all_policy')
			else:
				msg='Not a admin'		
		else:
			msg='Username OR password is incorrect'
	return render(request ,'admin_login.html',{'msg':msg})

def register(request):
	msg = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		password2 =request.POST.get('password2')
		
		if password == password2:
			user = User.objects.create_user(username=username,  password=password)
			user.save()
			return redirect('user_login')
		else:
			msg = "password did't match"
	return render(request ,'register.html',{'msg':msg})

def change_password(request):
	msg = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		oldpassword = request.POST.get('oldpassword')
		password =request.POST.get('password')
		password2 =request.POST.get('password2')
		
		if password == password2:
			user = authenticate(request, username=username, password=oldpassword)
			if user is not None:
				user.set_password(password)
				user.save()
				return redirect('user_login')
			else:
				msg='Username OR password is incorrect'
			
		else:
			msg = "password did't match"
	return render(request ,'change_password.html',{'msg':msg})

def logoutUser(request):
	logout(request)
	return redirect('user_login')

@login_required(login_url="/")
def add_policy(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        account_no = request.POST.get('account_no')
        date = request.POST.get('date')
        customer_id = request.POST.get('customer_id')
        branch = request.POST.get('branch')
        mobile = request.POST.get('mobile')
        adhar_sub = request.POST.get('adhar_sub')
        adhar_nom = request.POST.get('adhar_nom')
        insured_name = request.POST.get('insured_name')
        nom_account = request.POST.get('nom_account')
        nom_name = request.POST.get('nom_name')
        bank = request.POST.get('bank')
        status = request.POST.get('status')
        photo = request.FILES.get('photo')
        
        if len(mobile) == 10:
            Policy.objects.create(
                name=name,
                account_no=account_no,
                date=date,
                customer_id=customer_id,
                branch=branch,
                mobile=mobile,
                adhar_sub=adhar_sub,
                adhar_nom=adhar_nom,
                insured_name=insured_name,
                nom_account=nom_account,
                nom_name=nom_name,
                bank=bank,
                status=status,
                photo=photo)
            return redirect('all_policy')
        else:
            msg = "Please check mobile number"

    return render(request, 'add_policy.html', {'msg': msg})


@login_required(login_url="/")
def edit_policy(request, id):
    policy = Policy.objects.get(id=id)  # Handle case if the policy doesn't exist

    if request.method == 'POST':
        name = request.POST.get('name')
        account_no = request.POST.get('account_no')
        date = request.POST.get('date')
        customer_id = request.POST.get('customer_id')
        branch = request.POST.get('branch')
        mobile = request.POST.get('mobile')
        adhar_sub = request.POST.get('adhar_sub')
        adhar_nom = request.POST.get('adhar_nom')
        insured_name = request.POST.get('insured_name')
        nom_account = request.POST.get('nom_account')
        nom_name = request.POST.get('nom_name')
        bank = request.POST.get('bank')
        status = request.POST.get('status')
        photo = request.FILES.get('photo')

        if len(mobile) == 10:
            # Assigning values correctly
            policy.name = name
            policy.account_no = account_no
            policy.date = date
            policy.customer_id = customer_id
            policy.branch = branch
            policy.mobile = mobile
            policy.adhar_sub = adhar_sub
            policy.adhar_nom = adhar_nom
            policy.insured_name = insured_name
            policy.nom_account = nom_account
            policy.nom_name = nom_name
            policy.bank = bank
            policy.status = status
            policy.photo = photo

            policy.save()  # Save the updated policy object
            return redirect('all_policy')
        else:
            msg = "Please check the mobile number"
            return render(request, 'edit_policy.html', {"policy": policy, "msg": msg})

    return render(request, 'edit_policy.html', {"policy": policy})


@login_required(login_url="/")
def view_policy(request,id):
	policy = Policy.objects.get(id=id)
	policy.photo = str(policy.photo).replace("static/",'')
	return render(request ,'policy_detail.html',{'policy':policy})

@login_required(login_url="/")
def delete_policy(request,id):
	policy = Policy.objects.get(id=id).delete()
	return redirect('all_policy')

@login_required(login_url="/")
def all_policy(request):
	policies = Policy.objects.all()
	return render(request ,'client_listing.html',{'policies':policies})

@login_required(login_url="/")
def search_policy(request):
    search_by = request.GET.get('search_by')
    search_value = request.GET.get('search_value')
    policy = []
    if search_by and search_value:
        if search_by == 'account_no':
            policy = Policy.objects.filter(account_no__icontains=search_value)
        elif search_by == 'customer_id':
            policy = Policy.objects.filter(customer_id__icontains=search_value)
        elif search_by == 'mobile':
            policy = Policy.objects.filter(mobile__icontains=search_value)
        elif search_by == 'adhar_sub':
            policy = Policy.objects.filter(adhar_sub__icontains=search_value)
        elif search_by == 'adhar_nom':
            policy = Policy.objects.filter(adhar_nom__icontains=search_value)
        elif search_by == 'insured_name':
            policy = Policy.objects.filter(insured_name__icontains=search_value)
        elif search_by == 'nom_account':
            policy = Policy.objects.filter(nom_account__icontains=search_value)
    
    return render(request ,'policy_detail.html',{'policy':policy[0]})