from agno.workflow import Workflow
from members.content_enhancer import content_enhancer
from members.meta_drafter import meta_drafter
from members.seo_drafter import seo_drafter
from agno.agent import Agent
from members.writer import writer


class ArticleWritingFlow(Workflow):
    content_enhancer: Agent
    seo_drafter: Agent
    meta_drafter: Agent

    def __init__(self):
        super().__init__()
        self.content_enhancer = content_enhancer()
        self.seo_drafter = seo_drafter()
        self.meta_drafter = meta_drafter()

    def run(self, draft: str):
        print("Running article writing flow...")
        print("Enhancing content...")
        enhanced_draft = self.content_enhancer.run(draft)
        print(f"Draft enhanced. content - {enhanced_draft.content}")
        print("Creating SEO draft...")
        seo_draft = self.seo_drafter.run(enhanced_draft.content)
        print(f"SEO draft created. contnent - {seo_draft.content}")
        print("Creating meta description...")
        meta_draft = self.meta_drafter.run(seo_draft.content)
        print(f"Meta description created. content - {meta_draft.content}")
        print("Article writing flow completed.")
        print("Final draft and meta description ready.")
        return writer(title_and_meta=meta_draft.content, content=seo_draft.content)
