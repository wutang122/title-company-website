    # coding:utf-8

from django.utils.encoding  import *
from urllib2 import *
from re import *
from results.models import *
import unicodedata
global checkbox_list
global checkbox_list_crossref
from forms import *
from views import *

def delete_all ():
	whichsite.objects.all().delete()
	postinglisting.abjects.all().delete()
	posting_system.abjects.all().delete()


potential_usernames = ['blazerodwildebeest'
,'redstonewhiting'
,'potatobass'
,'melonteal'
,'flowerpotwoodcock'
,'slimeballavocet'
,'bedrockshads'
,'vinesmare'
,'wheatbison'
,'stringjaguar'
,'carrotspartridge'
,'sulphurbobcat'
,'gravelhorse'
,'shearsbutterfly'
,'catdiscturtle'
,'lavagelding'
,'signpostseahorse'
,'torchantelope'
,'sugarcanepilchard'
,'anvilgoshawk'
,'claysquirrel'
,'appledonkey'
,'airox'
,'myceliummole'
,'signlocust'
,'bonemealorangutan'
,'spongeguillemot'
,'birchwoodmeerkat'
,'clockgull'
,'bookshelfbadger'
,'portalcrocodile'
,'fireauk'
,'stickyak'
,'eggwaterfowl'
,'mapbongo'
,'railshawk'
,'cauldronraven'
,'flintgrouse'
,'furnacedingo'
,'potatoescockroach'
,'icecolt'
,'dandelionraccoon'
,'tripwirebloodhound'
,'obsidianponie'
,'sugarmackerel'
,'fernguineafowl'
,'snowballpolecats'
,'tntwildcat'
,'lilypadoryx'
,'trapdoormussel']




def replacer(kim):
	kima = kim.replace('\n','')
	kima = kima.replace('\t','')
	kima = kima.replace('\r','')
	return kima

def find_ebay_aref(self):
	lor = findall('<a href.*?/a>',self)
	return lor

def kill_objects():
	whichsite.objects.all().delete()

def ebay(term,high_price, zipcode,distance, user):
	#kill_objects()
	checkbox_list = []
	if " " in term:
		term = term.replace(" ","%20")

	url = "http://www.ebay.com/sch/i.html?_sacat=0&_ftrt=901&_ftrv=1&_sabdlo&_sabdhi&_samilow&_samihi&_sop=12&_dmd=1&_ipg=100&_stpos=" + str(zipcode) + "&_sadis=" + str(distance) + "&_fspt=1&_nkw=" + term + "&LH_PrefLoc=99&_dcat=139973&rt=nc&_pppn=r1&_mPrRngCbx=1&_udlo&_udhi=" + str(high_price)

	#url = "http://www.ebay.com/sch/i.html?_sacat=0&_ftrt=901&_ftrv=1&_sabdlo&_sabdhi&_samilow&_samihi&_sop=12&_dmd=1&_ipg=100&_stpos=" + zipcode + "&_sadis=" + distance + "&_fspt=1&_nkw=" + term + "&LH_PrefLoc=99&_dcat=139973&rt=nc&_pppn=r1&_mPrRngCbx=1&_udlo&_udhi=" + high_price
	#url = "http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.Xwatch&_nkw=watch&_sacat=0"
	req = Request(url, headers={'User-Agent' : "Magic Browser"})

	kora = urlopen(req)

	kor = kora.read()
	kora.close()
	cor = findall('sresult lvresult clearfix.*?li>',kor, re.MULTILINE|re.DOTALL)
	for ti in cor:
		aor = replacer(ti)
		a_ref = find_ebay_aref(aor)
		a_ref = str(a_ref).strip('[]')
		a_ref = str(a_ref).strip("''")
		dima = findall('<a href.*?</a>',a_ref)
		a_ref = dima[0]
		a_ref_name = dima[1]
		#price = findall('"g-b">(.*?)</span>',aor, re.MULTILINE|re.DOTALL)
		price = findall('"g-b">\$(\d*\.\d*?)</span>',aor, re.MULTILINE|re.DOTALL)
		price = str(price)
		price = price.replace('[','')
		price = price.replace(']','')
		price = price.replace("'","")
		try:
			actprice = float(price)
			actprice = '%.2f' % actprice
		except ValueError:
			actprice = 5
		price_pres = '$' + str(price)
		#print zipcode


		p = whichsite(user = user, site = 'Ebay' , item = term, a_ref = a_ref, a_ref_name = a_ref_name, price_pres = price_pres, price = actprice, zipcode = zipcode, distance = distance)

		#p = whichsite(user = user, site = 'Ebay' , item = term, a_ref = a_ref, a_ref_name = a_ref_name,price_pres = price_pres, price= actprice,condition = aor, zipcode = zipcode)
		p.save()
	#checkbox_list.append(['Amazon','Amazon'])
	#checkbox_list_crossref.append('Amazon')
	print whichsite.objects.all()


def amazon(term,location):
	if " " in term:
		term = term.replace(" ","+")
        url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + term
        req = Request(url, headers={'User-Agent' : "Magic Browser"})
        kora = urlopen(req)

        kor = kora.read()
        kora.close()
	cor = findall('sult_\d*?.*?<li id="res',kor, re.DOTALL|re.MULTILINE)

	for ti in cor:
                aor = replacer(ti)
		a_ref = findall('<img alt.*?>',aor, re.MULTILINE|re.DOTALL)
		a_ref_name = findall('<a class="a-link-normal s-access-detail-page a-text-normal".*?</a>',aor, re.MULTILINE|re.DOTALL)
		#a_ref_name = findall('<h3 class="newaps">(.*?</a>)',aor,re.MULTILINE|re.DOTALL)
		a_ref_name = str(a_ref_name).strip('[]')
		a_ref_name = str(a_ref_name).strip("''")
	        a_ref_name = a_ref_name.replace("h2","p")

		a_ref = str(a_ref).strip('[]')
                a_ref = str(a_ref).strip("''")
                price = findall('<span class="a-size-base a-color-price s-price a-text-bold">(.*?)</span>', aor, re.MULTILINE|re.DOTALL)
		#price = findall('"bld lrg red">.*\$(\d*\.\d*?)</span>', aor, re.MULTILINE|re.DOTALL)
                price = str(price)
                price = price.replace('[','')
                price = price.replace(']','')
                price = price.replace("'","")
		price = price.strip("$")
                try:
                        actprice = float(price)
                        actprice = '%.4f' % actprice
			price_pres = '$' + str(price)
                except ValueError:
		 	io = 1

			actprice = findall('\$(\d*\.\d*?)',str(price))
			actprice = search('\$(\d*\.\d*)',str(price))
			if actprice == None:
				price_pres = "error"
				actprice = 5
			else:
				actprice = actprice.group()
				actprice = float(actprice.strip("'$"))
				#actprice = 5

                		price_pres = '$' + str(price)
                p = whichsite(site = 'Amazon' , item = term, a_ref = a_ref, a_ref_name = a_ref_name,price_pres = price_pres, price= actprice)
                p.save()
        return whichsite.objects.all(),'Amazon'

def google_shopping(term,location):
	if " " in term:
                term = term.replace(" ","+")
	url = "https://www.google.com/search?num=100&safe=off&output=search&tbm=shop&q=" + term
	req = Request(url, headers={'User-Agent' : "Magic Browser"})
        kora = urlopen(req)
        kor = kora.read()
        kora.close()
 	cor = findall('<div class="psliimg">(.*?)<div class="pslires">',kor, re.DOTALL|re.MULTILINE)
        for ti in cor:
		aor = replacer(ti)
        	tim = findall('<a href.*?</a>',aor)
		if len(tim)==2:
			a_ref = tim[0]
			a_ref_name = tim[1]
                #a_ref_name = findall('<h3 class="newaps">(.*?</a>)',aor,re.MULTILINE|re.DOTALL)
                #a_ref_name = str(a_ref_name).strip('[]')
                #a_ref_name = str(a_ref_name).strip("''")
                #a_ref_name = a_ref_name.replace("h2","p")

                #a_ref = str(a_ref).strip('[]')
                #a_ref = str(a_ref).strip("''")
                price = findall('<div class="_OA"><div><b>(.*?)</b>',aor)
                #price = findall('"bld lrg red">.*\$(\d*\.\d*?)</span>', aor, re.MULTILINE|re.DOTALL)
                price = str(price)
                price = price.replace('[','')
                price = price.replace(']','')
                price = price.replace("'","")
                price = price.strip("$")
                try:
                        actprice = float(price)
                        actprice = '%.4f' % actprice
                except ValueError:

                        actprice = 5
                price_pres = '$' + str(price)
		#a_ref = a_ref)
		#a_ref_name = unicode(a_ref_name)
		#price_pres = unicode(price_pres)
		#a_ref = force_text(a_ref, encoding='utf-8', strings_only=False, errors='strict')
		#a_ref_name = force_text(a_ref_name, encoding='utf-8', strings_only=False, errors='strict')
		#price_pres = smart_text(price_pres, encoding='utf-8', strings_only=False, errors='strict')

		p = whichsite(site = 'Google Shopping', item = term)
		#p = whichsite(site = 'Google Shopping', item = term, a_ref = a_ref, a_ref_name = a_ref_name, price_pres = price_pres, price=actprice)
                p.save()
        return whichsite.objects.all(),'Google Shopping'



global forma
global active_user
global search_term
global filter_term
global checkbox_term
global sort_term
global filter_form
global check_form
global checkbox_form
global sort_form
global aska
global termdict
global price_low
global price_high
#global ebay
#global amazon
global checkbox_list
global checkbox_list_crossref

#class checkbox_form(forms.Form):
#    sites = forms.MultipleChoiceField(label='From Which Sites:', required=False,widget=forms.CheckboxSelectMultiple(), choices=checkbox_list)


def clean_data():
    global termdict
    termdict = {}
    forma = []


def tryer():

    globalize()
    global forma
    global active_user
    global search_term
    global filter_term
    global checkbox_term
    global sort_term
    global filterform
    global checkform
    global sortform
    global aska
    global contactform
    global price_low
    global price_high
    global poor

    poor = False
    try:
	checkbox_list
    except NameError:
        checkbox_list = []



    try:
	checkbox_list_crossref
    except NameError:
        checkbox_list_crossref = []

    try:
	active_user
    except NameError:
	active_user  = ''

    try:
	termdict
    except NameError:
	termdict = {}
    try:
        price_low
    except NameError:
        price_low = 0

    try:
        price_high
    except NameError:
        price_high = 0

    try:
	filter_term
    except NameError:
	filter_term = ''

    try:
	checkbox_term
    except NameError:
	checkbox_term = ''

    try:
	sort_term
    except NameError:
	sort_term = ''

    try:
	search_term
    except NameError:
	search_term = ''

    try:
	forma
    except NameError:
	forma = []

    if forma:
	termdict['forma'] = forma
    else:
	termdict['forma'] = 'no'


    if len(active_user)>1:
	termdict['active_user'] = active_user
    else:
	termdict['active_user'] = active_user

    if len(search_term)>1:
	contactform = Contact_Form(initial={'subject':search_term})
	termdict['contactform'] = contactform
    	termdict['search_term'] = search_term
    else:
	contactform = Contact_Form()
	termdict['contactform'] = contactform
	termdict['search_term'] = search_term



    if price_high>0 or price_low>0:

  	if price_high>0:
		filterform = filter_form(initial={'pricehigh': price_high})
	if price_low>0:
		filterform = filter_form(initial={'pricelow': price_low})
        if price_high>0 and price_low>0:
		filterform = filter_form(initial={'pricelow': price_low, 'pricehigh': price_high})
        termdict['price_high'] = price_high
	termdict['price_low'] = price_low
	termdict['filterform'] = filterform
    else:
        filterform = filter_form()
        termdict['filterform'] = filterform
	termdict['price_low'] = 0
	termdict['price_high'] = 0



    if len(checkbox_term)>1:
        checkboxform = checkbox_form(initial={'sites': checkbox_term})
	checkboxform = checkbox_form()
	termdict['checkboxform'] = checkboxform
    	termdict['checkbox_term'] = checkbox_term
    else:
        checkboxform = checkbox_form()
	termdict['checkboxform'] = checkboxform
        #termdict['testa'] = checkbox_term


    if len(sort_term)>1:
        sortform = sort_form(initial={'which':sort_term})
	termdict['sortform'] = sortform
	termdict['sort_term'] = sort_term
    else:
    	sortform = sort_form()
	termdict['sortform'] = sortform
	termdict['sort_term'] = ''
    return termdict

def filter_reset():
    global search_term
    global price_high
    global price_low
    global sort_term
    global checkbox_term
    global forma
    #checkbox_term = "test"

    termdict = tryer()

    if price_high>0 or price_low>0 or len(sort_term)>0 or len(checkbox_term)>0:
	forma = whichsite.objects.all()

	if termdict['price_high']>1:
		price_high = termdict['price_high']
		try:
			price_high = int(price_high)
			forma = forma.filter(price__lte=price_high)
		except ValueError:
			io = 1

		if len(termdict['sort_term'])>0:
			if sort_term=='low':
                        	forma = forma.order_by('-price')
                	if sort_term=='high':
                        	forma = forma.order_by('price')
                	if sort_term=='rev':
                        	forma = forma.order_by('a_ref_name')


	if termdict['price_low']>1:
		price_low = termdict['price_low']
		try:
			price_low = int(price_low)
			forma = forma.filter(price__gte=price_low)
		except ValueError:
			io=1

		if len(termdict['sort_term'])>0:
                        if sort_term=='low':
                                forma = forma.order_by('-price')
                        if sort_term=='high':
                                forma = forma.order_by('price')
                        if sort_term=='rev':
                                forma = forma.order_by('a_ref_name')
    return forma

def globalize():
    global forma
    global active_user
    global search_term
    global filter_term
    global checkbox_term
    global sort_term
    global filter_form
    global checkbox_form
    global sort_form
    global aska
    global filterform
    global checkboxform
    global sortform
    global signinform
    global price_high
    global price_low
    filterform = filter_form()
    checkboxform = checkbox_form()
    sortform = sort_form()



#def new_home(request):
#	if request.method == "POST":
#		if request.path_info.find('#form_a_action'):
#			process this form
#		else if ...


def new_user(request):
    global poor
    globalize()
    global forma
    global active_user

    try:
	poor
    except NameError:
	poor = False

    io = 1
    #message = "error"
    formt = new_user_form()
    forms = new_user_form(request.POST)
    if forms.is_valid():
	usernamea = forms.cleaned_data['username']
        passworda = forms.cleaned_data['password']
	first_name = forms.cleaned_data['first_name']
	last_name = forms.cleaned_data['last_name']
	email_addressa = forms.cleaned_data['address']
	try:
		timea = User.objects.get(username = usernamea)
		message = (u'Username "%s" already exists' % usernamea)
		return render(request, 'new_user.html', {'new_user':forms, 'message':message})
	except User.DoesNotExist:
		io = 0
		try:
			userb = User.objects.create_user(usernamea, email_addressa, passworda)
			userb.save()
			active_user = usernamea

			termdict = tryer()
                	contactform = termdict['contactform']
                	filterform = termdict['filterform']
                	checkboxform = termdict['checkboxform']
                	sortform = termdict['sortform']
			forma = termdict['forma']
			contactform = Contact_Form()
			signinform = sign_in_form()

			return render(request, 'aa.html', {'contactform':contactform,'active_user':usernamea,'sign_in_form':signinform,'sortform':sortform, 'forma': forma, 'filter':filterform,'check':checkboxform})
		except ValueError:
			message = 'valueerror'

		return render(request, 'new_user.html', {'new_user':forms, 'message':message})


	return render(request, 'new_user.html', {'new_user':forms,'message':message})


    if poor:
    	message = "please fill out all fields"
    	return render(request, 'new_user.html', {'new_user':forms, 'message':message})
    else:
	poor = True
    	message = poor
	return render(request, 'new_user.html', {'new_user':formt, 'message':message})
