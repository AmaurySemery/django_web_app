from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
        'listings/band_list.html',  # pointe vers le nouveau nom de modèle
        {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def email_send(request):
   return render(request,
          'listings/email_send.html',)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
  if request.method == "POST":
     # Créer une instance du formulaire et le remplir avec les données POST
     form = ContactUsForm(request.POST)
     if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email_send')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
  
  else:
     # Ceci doit être une requête GET, donc créer un formulaire vide
     form = ContactUsForm()
  return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit
                