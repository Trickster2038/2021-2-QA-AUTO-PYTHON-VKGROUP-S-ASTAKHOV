import requests


class ApiClient:

    csrf_token = None
    session = requests.Session()
    cookie = None

    def login_simple(self):
        self.cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; z=tf8lbwkij6i26n0o2ya0c6hekm44ujwy; mc=89deb164612f7a4891318203ffd9aabab265d13134383632; sdc=dsAcBCoxLieagMHN; _gid=GA1.3.809879900.1636105958; _gac_UA-54874995-1=1.1636105958.EAIaIQobChMIgseu0fmA9AIVCrwYCh3hTAGgEAAYASAAEgIvK_D_BwE; _gat_UA-54874995-1=1; tmr_detect=0%7C1636105960312; tmr_reqNum=178"
        self.csrf_token = "ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8"