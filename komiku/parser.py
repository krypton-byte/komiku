import re
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from bs4 import BeautifulSoup as bs
from requests import Session
requests = Session()
requests.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
class InvalidUrl(Exception):
    pass
class ImageX:
    def __init__(self, listBytesIO) -> None:
        self.images = listBytesIO
        self.image = None
    @property
    def generate_pdf(self):
        height = sum([ i.height for i in self.images])
        width  = max([ i.width for i in self.images])
        self.image=Image.new("RGB", (width, height), color=(255, 255,255)).convert("RGBA")
        itera = 0
        for i in self.images:
            self.image.paste(i, (int(0 if i.width == width else (width/2)-(i.width/2)), itera), i.convert("RGBA"))
            itera+=i.height
        return self.image
    def save(self, filename=False, format="pdf"):
        if not self.image:
            self.generate_pdf
        if isinstance(filename, str):
            self.image.convert("RGB").save(filename, format=format)
        else:
            sio=BytesIO()
            self.image.convert("RGB").save(sio, format=format)
            return sio
    def __repr__(self) -> str:
        return f"<[ {self.images.__len__()} page ]>"
class searchManga:
    def __init__(self, query, post_type="manga") -> None:
        self.query = query
        self.fetch = [byUrl(f"https://komiku.id{i}") for i in re.findall("(/ch/.*?)/", requests.get("https://data2.komiku.id/cari/", params={"post_type":post_type, "s":query}).text)]
    def __str__(self) -> str:
        return f"<[ count: {self.fetch.__len__()}]>"
    def __repr__(self) -> str:
        return self.__str__()

class byUrl:
    def __init__(self, url) -> None:
        try:
            self.url = url
            self.imagesObj = []
            self.title = re.search("\/ch\/(.*?)\/?$",url).group(1).replace("-", " ")
        except Exception:
            raise InvalidUrl("Title Not Match")
    def __str__(self) -> str:
        return f"<[title: \"{self.title}\"]>"
    def __repr__(self) -> str:
        return self.__str__()
    @property
    def images(self):
        return [i["src"] for i in bs(requests.get(self.url).text, "html.parser").find_all("img", attrs={"class":"klazy ww"})]
    def download(self, workers=5):
        data = []
        with ThreadPoolExecutor(max_workers=workers) as wth:
            for i in self.images:
                data.append(Image.open(BytesIO(wth.submit(requests.get, i).result().content)))
        return ImageX(data)