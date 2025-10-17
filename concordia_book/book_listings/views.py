from django.shortcuts import render
from .models import Textbook


def textbook_list(request, course_code):
    # Filter textbooks by course_code and availability
    textbooks = Textbook.objects.filter(
        course_code__iexact=course_code,  # Case-insensitive match
        availability=True
    )

    context = {
        'textbooks': textbooks,
        'course_code': course_code,
        'no_results': len(textbooks) == 0  # Helper variable for template
    }

    return render(request, 'book_listings/textbook_list.html', context)
