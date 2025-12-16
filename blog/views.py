from django.shortcuts import render

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail
from django.contrib import messages
from .models import Post
from .forms import ContactForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # wysyłka e-maila (w konsoli dzięki console backend)
            send_mail(
                subject=f"[Kontakt z bloga] {form.cleaned_data['subject']}",
                message=f"Od: {form.cleaned_data['full_name']} <{form.cleaned_data['from_email']}>\n\n{form.cleaned_data['message']}",
                from_email=form.cleaned_data['from_email'],
                recipient_list=['twoj@email.pl'],  # zmień na swój
                fail_silently=False,
            )
            messages.success(request, 'Wiadomość została wysłana!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})