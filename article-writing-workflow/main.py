from flow.article_writing_flow import ArticleWritingFlow


if __name__ == "__main__":
    flow = ArticleWritingFlow()

    with open("./draft/solo_travel_draft.txt", "r") as rough_draft:
        draft = rough_draft.read()
        result = flow.run(draft=draft)
        print(result.content)