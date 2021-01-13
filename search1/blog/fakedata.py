import random


class Papers():
    def __init__(self):
        self.papers = []

    def searchpapers(self, type, req, topnum):
        # random.seed(1)

        for i in range(topnum):
            paper = {
                '_id': i + 1,
                'title': '[Oral at NeurIPS 2020] DVERGE: Diversifying Vulnerabilities for Enhanced Robust ',
                "authors": "Huanrui Yang, Jingyang Zhang, Hongliang Dong, Nathan Inkawhich, Andrew Gardner",
                "abstract": "Recent research finds CNN models...",
                "publicationOrg": "NeurIPS",
                "year": 2020,
                "pdfUrl": "...",
                "pdfPath": ".../searcher/data/PDFs/xx.pdf",
                "publicationUrl": "https://papers.nips.cc/paper/2020/hash/3ad7c2ebb96fcba7cda0cf54a2e802f5-Abstract.html",
                "codeUrl": "https://github.com/zjysteven/DVERGE",
                "datasetUrl": "https://drive.google.com/drive/folders/1i96Bk_bCWXhb7afSNp1t3woNjO1kAMDH?usp=sharing",
                "videoUrl": "",
                "videoPath": ".../searcher/data/videos/xx.*",
                "pdfText": "Alternatively, ensemble methods are proposed to induce sub-models...",
                "videoStruct": [
                    {
                        "timeStart": "hh-mm-ss",
                        "timeEnd": "hh-mm-ss",
                        "sentence": "Only small clean accuracy drop is observed in the process."
                    }
                ]
            }
            # paper['_id'] = i
            self.papers.append(paper)
        return self.papers
