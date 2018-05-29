from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from apps.forum.models import Profile
 
# this worked after putting this file into a tests directory 
# then explicitly setting models path all they way up to apps folder.

class TestProfileModel(TestCase):
 
    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(
            username="forum_user", password="forum_user_password")
        # Check that a Profile instance has been crated
        self.assertIsInstance(user.profile, Profile)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instace
        user.save()
        self.assertIsInstance(user.profile, Profile)