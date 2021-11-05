import pytest
from base import ApiBase


class TestApi(ApiBase):

    @pytest.mark.API
    def test_create_n_delete_campaign(self):
        name = "Новая кампания " + self.random_string()
        response = self.create_campaign(name)
        assert response.status_code == 200
        id = response.json()['id']
        assert self.check_campaign_presence(name)
        resp_delete = self.delete_campaign(id)
        assert resp_delete.status_code == 204
        assert not self.check_campaign_presence(name)

    @pytest.mark.API
    def test_create_segment(self):
        name = "Новый сегмент " + self.random_string()
        response = self.create_segment(name)
        assert response.status_code == 200
        assert self.check_segment_presence(name)

    @pytest.mark.API
    def test_delete_segment(self):
        name = "Новый сегмент " + self.random_string()
        response = self.create_segment(name)
        id = response.json()['id']
        assert self.check_segment_presence(name)
        resp_delete = self.delete_segment(id)
        assert resp_delete.status_code == 204
        assert not self.check_segment_presence(name)
