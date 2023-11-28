from rest_framework import status
from core.fixtures.user import user
from core.fixtures.post import post


class TestUserViewset:
    endpoint = '/api/user/'

    def test_list(self, client, user):
        response = user.objects.all()
        
    def test_retrieve(self, client, user):
        pass
    def test_create(self, cient, user):
        pass
    def test_update(self, client, user):
        pass
