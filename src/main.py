import score_classes as scores
import processing_classes as nlp_process
import os
analysis = scores.Scores()

def store_score_between(us: nlp_process.UserStory, html: nlp_process.HTML):
    matched_chunks = list()
    matched_weight = 0
    for token, weight in us.processed.items():
        if token in html.processed:
            matched_chunks.append(token)
            matched_weight += weight
    
    score = matched_weight / us.total_weight
    file_match = scores.FileMatch(
        html.filename,
        score,
        matched_chunks
    )
    analysis.add_file(file_match)

def get_relevant_files(description: str, root_folder: str):
    us = nlp_process.UserStory(description)
    for root, _, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                html = nlp_process.HTML(filepath)
                store_score_between(us, html)

def include_ts(files):
    for ts_file in files:
        ts_file = ts_file[:-4] + 'ts'
        if os.path.isfile(ts_file):
            files.append(ts_file)
    return files


def main():
    description = """
    GIVEN the user is on the Association fruit home page
    WHEN he informs FN, selects his favorite fruit and click in SAVE ASSOCIATION
    THEN the message 'Saved!' should appear
    """
    root_folder = "./data/html"
    
    get_relevant_files(description, root_folder)

if __name__ == "__main__":
    main()

    analysis.sort()
    for i, f in enumerate(analysis.files):
        print(f"File: {f.filename}")
        print(f"Score: {f.score}")
        print(f"Matches ({len(f.matched_chunks)}): {f.matched_chunks}\n")
        if i == 4:
            break