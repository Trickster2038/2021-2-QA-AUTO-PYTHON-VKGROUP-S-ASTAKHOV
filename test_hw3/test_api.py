import pytest
from base import ApiBase
from utils.rand import RandString


class TestApi(ApiBase):
    @pytest.mark.API
    def test_create_n_delete_campaign(self):
        name = RandString.generate(prefix="Новый сегмент")
        response = self.api_client.post_create_campaign(name)
        assert response.status_code == 200
        id = response.json()['id']
        assert self.check_campaign_presence(name)
        resp_delete = self.api_client.post_remove_campaign(id)
        assert resp_delete.status_code == 204
        assert not self.check_campaign_presence(name)

    @pytest.mark.API
    def test_create_segment(self):
        name = RandString.generate(prefix="Новый сегмент")
        response = self.api_client.post_create_segment(name)
        assert response.status_code == 200
        assert self.check_segment_presence(name)
        self.api_client.delete_segment(id)

    @pytest.mark.API
    def test_delete_segment(self):
        name = RandString.generate(prefix="Новый сегмент")
        response = self.api_client.post_create_segment(name)
        id = response.json()['id']
        assert self.check_segment_presence(name)
        resp_delete = self.api_client.delete_segment(id)
        assert resp_delete.status_code == 204
        assert not self.check_segment_presence(name)
