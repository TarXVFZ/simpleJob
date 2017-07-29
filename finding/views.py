from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse


def index(request):
	return render(request, 'finding/index.html')

@csrf_exempt
def find(request):
	if request.method == "POST":
		tegs = request.POST['tegs'] + "#"

		teg = []
		st = ""
		for i in tegs:
			if i != "#":
				st = st + i
			elif i == "#" and st != "":
				try:
					teg_one = Perk.objects.get(name=st)
				except:
					st = ""
					continue
				else:
					teg.append(teg_one.id)
					st = ""

		if len(teg) == 0:
			return render(request, 'finding/index.html')

		users_perk = UserPerk.objects.filter(perk=teg[0])
		rating = [0 for x in users_perk]
		ind = 0
		for i in users_perk:
			s = 0
			user = User.objects.get(id=i.user.id)
			perk_of_user = UserPerk.objects.filter(user=user)
			concurrences_of_perks = []
			for j in perk_of_user:
				for ji in teg:
					perk_ji = Perk.objects.get(id=ji)
					if j.perk.name == perk_ji.name:
						concurrences_of_perks.append(j)
					
			for j in concurrences_of_perks:
				s = s + j.percent
			s = s // len(concurrences_of_perks)
			rating[ind] = s
			ind += 1
		print(rating)
		rt = ",".join(str(x) for x in rating)
		return HttpResponse(rt)
	else:
		print("not post")
		return HttpResponse("bad")