import arxiv
from typing import List, Optional
import requests
import time 

class ArXiv:
    def __init__(
        self,
        query: str,
        filter_keys: str,
        max_results: int,
        # id_list: Optional[List],
    ):
        self.query = query
        self.max_results = max_results
        # self.id_list = id_list
        self.filter_keys = filter_keys

    def get_search(self):
        search = arxiv.Search(
            query=self.query,
            max_results=self.max_results,
            # id_list=self.id_list,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        self.show_info(search)
        self.search = self.filter_arxiv(search)

    def filter_arxiv(self, search):
        filter_results = []
        filter_keys = self.filter_keys
        for index, result in enumerate(search.results()):
            abs_text = result.summary.replace('-\n', '-').replace('\n', ' ').replace('ulti-modal', 'ultimodal')
            meet_num = 0
            for f_key in filter_keys.split(" "):
                if f_key.lower() in abs_text.lower():
                    meet_num += 1
            if meet_num >= float(0.6 * len(filter_keys.split(" "))):
                filter_results.append(result)
        return filter_results

    def show_info(self, search):
        for idx, result in enumerate(search.results()):
            print(idx, result.title, result.updated, result.pdf_url)
            self.download_pdf(result)
    
    def info_2_dict(self):
        results = list()
        for idx, result in enumerate(self.search):
            result = {
                "title": result.title,
                "updated": result.updated,
                "published": result.published,
                "pdf_url": result.pdf_url,
                "query": self.filter_keys,
                "doi": result.doi,
                "authors": ', '.join([authors.name for authors in result.authors]),
                "journal_ref": result.journal_ref,
                'summary': result.summary,
            }
            results.append(result)
        return results

    def download_pdf(self, result): 
        t1 = time.time()
        response = requests.get(result.pdf_url)
        if response.status_code == 200:
            filename = f"{result.title.replace(' ', '_')}.pdf"
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"PDF 下载成功: {filename}")
        else:
            print("PDF 下载失败")
        t2 = time.time()
        t = t2 - t1
        print(f"下载时间: {t}s")

if __name__ == '__main__':
    myarxiv = ArXiv(
        query = "Uranium",
        filter_keys="Uranium",
        max_results=100,
    )
    myarxiv.get_search()
    # myarxiv.show_info()
