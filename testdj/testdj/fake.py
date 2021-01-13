import json


def get_detail(id):
    data = json.dumps(
        {
            "_id": id,
            "title": "[Oral at NeurIPS 2020] DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles",
            "authors": "Huanrui Yang, Jingyang Zhang, Hongliang Dong, Nathan Inkawhich, Andrew Gardner, Andrew Touchet, Wesley Wilkes, Heath Berry, Hai Li",
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
    )
    return data


def get_title(id):
    data = {"_id": id,
            "title": "hh"}
    return data


def searchpapers(query):
    import random
    random.seed(1)
    papers = []
    titlelist = ["Disparity-Aware Domain Adaptation in Stereo Image Restoration",
                 "Hardware-in-the-Loop End-to-End Optimization of Camera Image Processing Pipelines",
                 "Fine-Grained Image-to-Image Transformation Towards Visual Recognition",
                 "Learning to Restore Low-Light Images via Decomposition-and-Enhancement",
                 "Unsupervised Adaptation Learning for Hyperspectral Imagery Super-Resolution",
                 "Image2StyleGAN++: How to Edit the Embedded Images?",
                 "Disentangled Image Generation Through Structured Noise Injection"]
    authorlist = ["Huanrui Yang, Jingyang Zhang", "Hongliang Dong, Nathan Inkawhich", "Andrew Gardner, Andrew Touchet",
                  "Wesley Wilkes", "Heath Berry", "Hai Li"]
    pOrg = ["NeurIPS", "AAAI", "CVPR", "ACL", "IEEE", "ICIP", "EMNLP", "NAACL", "IJCNLP", "EACL"]
    pdfurl = ["https://arxiv.org/pdf/2009.14720.pdf", "https://arxiv.org/abs/2006.10739"]
    codeUrl = ["https://github.com/zjysteven/DVERGE", "https://github.com/tancik/fourier-feature-networks",
               "https://github.com/zjysteven/DVERGE"]
    videoUrl = ["https://crossminds.ai/video/5fcac19de84a893b3186a943/",
                "https://crossminds.ai/video/5fb82261890833803bc7e7f8/"]
    abstractlist = ["default abstract default abstract default abstract"]
    if query["type"] == 1:
        q = query["query_text"]
        title = q["title"]
        if title == "":
            title = "default title default title"
        titlelist.append(title)
        author = q["author"]
        if author == "":
            author = "default author"
        authorlist.append(author)
        abstract = q["abstract"]
        if abstract == "":
            abstract = "default abstract default abstract default abstract default abstract "
        abstractlist.append(abstract)
        # content = q["content"]
        operator = query["operator"]
    else:
        q = query["query_text"]
        titlelist.append(q)

    for i in range(query["top_number"]):
        paper = {
            '_id': i + 1,
            'title': titlelist[random.randint(0, len(titlelist) - 1)],
            "authors": authorlist[random.randint(0, len(authorlist) - 1)],
            "abstract": abstractlist[random.randint(0, len(abstractlist) - 1)],
            "publicationOrg": pOrg[random.randint(0, len(pOrg) - 1)],
            "year": random.randint(2000, 2020),
            "pdfUrl": pdfurl[random.randint(0, len(pdfurl) - 1)],
            "pdfPath": ".../searcher/data/PDFs/xx.pdf",
            "publicationUrl": "https://papers.nips.cc/paper/2020/hash/3ad7c2ebb96fcba7cda0cf54a2e802f5-Abstract.html",
            "codeUrl": codeUrl[random.randint(0, len(codeUrl) - 1)],
            "datasetUrl": "https://drive.google.com/drive/folders/1i96Bk_bCWXhb7afSNp1t3woNjO1kAMDH?usp=sharing",
            "videoUrl": videoUrl[random.randint(0, len(videoUrl) - 1)],
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
        papers.append(paper)
    return papers
