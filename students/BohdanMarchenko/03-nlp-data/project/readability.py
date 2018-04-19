import os
import requests
from boilerpipe.extract import Extractor
for filename in os.listdir('scrape_result3'):
    try:
        with open('scrape_result3/'+filename, 'r') as fl:
            while True:
                url = fl.readline().replace('\n', '')
                if not url:
                    break
                extractor = Extractor(extractor='ArticleExtractor', url=url)
                extracted_text = extractor.getText()
                print(extracted_text)
                print(url)
                # response = requests.get('https://seekingalpha.com/article/4132686-exxon-mobil-changes-course-climate-disclosures')
                import ipdb; ipdb.set_trace()
    except Exception as ex:
        print(ex)

        # import ipdb; ipdb.set_trace()
# doc = Document(response.text)
