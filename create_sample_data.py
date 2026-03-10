import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_portal.settings')
django.setup()

from events.models import Event
from blog.models import BlogPost
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Create sample events
events_data = [
    {
        'title': 'Tech Conference 2024',
        'description': 'Annual technology conference featuring the latest innovations in AI, cloud computing, and software development.',
        'location': 'Convention Center, Downtown',
        'event_date': timezone.now() + timedelta(days=30),
        'capacity': 500
    },
    {
        'title': 'Music Festival',
        'description': 'Three-day music festival featuring local and international artists across multiple genres.',
        'location': 'City Park Amphitheater',
        'event_date': timezone.now() + timedelta(days=45),
        'capacity': 2000
    },
    {
        'title': 'Business Summit',
        'description': 'Network with industry leaders and learn about the latest business trends and strategies.',
        'location': 'Grand Hotel Conference Room',
        'event_date': timezone.now() + timedelta(days=60),
        'capacity': 200
    }
]

for event_data in events_data:
    Event.objects.get_or_create(
        title=event_data['title'],
        defaults=event_data
    )

# Create sample blog posts
blog_posts_data = [
    {
        'title': '5 Tips for Successful Event Planning',
        'content': '''Planning an event can be overwhelming, but with the right approach, it can be a rewarding experience. Here are five essential tips:

1. Start Early: Give yourself plenty of time to plan and organize every detail.
2. Set a Budget: Determine your budget early and stick to it.
3. Know Your Audience: Understand who you're planning for and tailor the event accordingly.
4. Create a Timeline: Break down tasks into manageable steps with deadlines.
5. Have a Backup Plan: Always prepare for unexpected situations.

Remember, successful events are all about attention to detail and proper planning.''',
        'author': User.objects.first()
    },
    {
        'title': 'The Future of Virtual Events',
        'content': '''Virtual events have transformed the way we connect and engage with audiences. As technology continues to evolve, we're seeing exciting trends:

- Hybrid events combining in-person and virtual experiences
- AI-powered networking and matchmaking
- Immersive VR and AR experiences
- Interactive gamification elements
- Real-time analytics and engagement metrics

The future of events is undoubtedly digital, and organizations that adapt to these changes will thrive in the coming years.''',
        'author': User.objects.first()
    },
    {
        'title': 'Networking Strategies for Professionals',
        'content': '''Effective networking is crucial for professional growth. Here are proven strategies:

1. Be Genuine: Authentic connections last longer than superficial ones.
2. Listen More: Focus on understanding others rather than just talking about yourself.
3. Follow Up: Send personalized messages within 24 hours of meeting someone.
4. Provide Value: Look for ways to help others before asking for favors.
5. Stay Consistent: Regularly attend industry events and maintain relationships.

Remember, networking is about building meaningful relationships, not just collecting contacts.''',
        'author': User.objects.first()
    }
]

for blog_data in blog_posts_data:
    BlogPost.objects.get_or_create(
        title=blog_data['title'],
        defaults=blog_data
    )

print("Sample data created successfully!")
print(f"Created {Event.objects.count()} events")
print(f"Created {BlogPost.objects.count()} blog posts")
