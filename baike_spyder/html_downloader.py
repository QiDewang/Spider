import urllib

class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)

        if response.status != 200:
            return None
        return response.read()
