from base import ApiBase

# resp.json()['id']

class TestApi(ApiBase):

    def test_create_campaign(self, client):
        name = "Новая кампания " + self.random_string()
        response = self.create_campaign(name)
        id = response.json()['id']
        assert self.check_campaign_presence(name)
        resp_delete = self.delete_campaign(id)
        assert resp_delete.status_code == 204
        assert not self.check_campaign_presence(name)